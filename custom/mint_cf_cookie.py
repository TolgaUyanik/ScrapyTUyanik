"""Borrow a Cloudflare clearance cookie from your own running Chrome.

alphaarchitect.com sits behind a Cloudflare *managed* challenge that fires on
every request, robots.txt included. Playwright chromium cannot pass it --
headless and headed both loop on "Just a moment..." forever, because the
challenge fingerprints the automation build. A normal Chrome session clears it
in one hop, so the cheap path is to mint the cookie here and let the spiders
crawl over plain HTTP.

    # 1. In Chrome: open chrome://inspect/#remote-debugging, tick
    #    "Allow remote debugging for this browser instance", click Allow.
    # 2. cd custom && python mint_cf_cookie.py

Writes cf_cookies.json next to this file (gitignored). cf_clearance is bound to
the exact User-Agent that earned it and to your public IP, so the UA is stored
alongside the cookie and the spiders must send both. Re-run whenever the
spiders start logging 403s -- clearance typically lasts under an hour.
"""

import json
import os
import pathlib
import urllib.error
import urllib.request

from playwright.sync_api import sync_playwright

SITE = "https://alphaarchitect.com/blog/"
PROBE = "/wp-json/wp/v2/posts?per_page=1&_fields=id"
OUT = pathlib.Path(__file__).resolve().parent / "cf_cookies.json"


def _profile_dirs():
    home = pathlib.Path.home()
    local = os.environ.get("LOCALAPPDATA")
    candidates = [
        os.environ.get("CHROME_USER_DATA_DIR"),
        f"{local}\\Google\\Chrome\\User Data" if local else None,
        home / "Library/Application Support/Google/Chrome",
        home / ".config/google-chrome",
    ]
    return [pathlib.Path(c) for c in candidates if c]


def ws_url():
    """Resolve Chrome's DevTools websocket URL.

    Chrome 147+ returns 404 for /json/version on the default user-data-dir, so
    fall back to the ws path Chrome itself writes into DevToolsActivePort.
    """
    for base in _profile_dirs():
        try:
            lines = (base / "DevToolsActivePort").read_text().splitlines()
        except OSError:
            continue
        port = lines[0].strip() if lines else ""
        path = lines[1].strip() if len(lines) > 1 else ""
        if not port:
            continue
        try:
            with urllib.request.urlopen(f"http://127.0.0.1:{port}/json/version", timeout=2) as r:
                return json.load(r)["webSocketDebuggerUrl"]
        except urllib.error.HTTPError as e:
            if e.code == 404 and path:
                return f"ws://127.0.0.1:{port}{path}"
        except (OSError, KeyError, ValueError):
            continue
    raise SystemExit(
        "No debuggable Chrome found. Open chrome://inspect/#remote-debugging, tick "
        "'Allow remote debugging for this browser instance', click Allow, then re-run."
    )


def main():
    with sync_playwright() as p:
        browser = p.chromium.connect_over_cdp(ws_url(), timeout=15000)
        ctx = browser.contexts[0]
        page = ctx.new_page()
        try:
            page.goto(SITE, wait_until="domcontentloaded", timeout=60000)
            # The challenge can still be running after load, and its interstitial
            # is localised, so poll the API instead of matching on page title.
            status = 0
            for _ in range(30):
                status = page.evaluate(
                    "async u => (await fetch(u, {credentials:'include'})).status", PROBE
                )
                if status == 200:
                    break
                page.wait_for_timeout(2000)
            if status != 200:
                raise SystemExit(
                    f"Challenge not cleared (API returned {status}). Load {SITE} in "
                    "this Chrome window by hand, wait for the post list, then re-run."
                )
            ua = page.evaluate("navigator.userAgent")
            cookies = {
                c["name"]: c["value"]
                for c in ctx.cookies(SITE)
                if c["name"].startswith("cf_")
            }
        finally:
            page.close()  # never close the browser -- it is the user's own Chrome

    if "cf_clearance" not in cookies:
        raise SystemExit("cf_clearance missing after a passing probe -- Cloudflare config changed?")
    OUT.write_text(json.dumps({"ua": ua, "cookies": cookies}, indent=2), encoding="utf-8")
    print(f"wrote {OUT} ({', '.join(cookies)})")


if __name__ == "__main__":
    main()
