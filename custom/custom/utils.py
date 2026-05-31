import os
import random

_UA_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "user_agents.txt")
_PROXY_FILE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "proxies.txt")

_user_agents = None
_proxies = None


def load_user_agents():
    global _user_agents
    if _user_agents is None:
        with open(_UA_FILE, "r") as f:
            _user_agents = [line.strip() for line in f if line.strip()]
    return _user_agents


def random_user_agent():
    return random.choice(load_user_agents())


def load_proxies():
    global _proxies
    if _proxies is None:
        if not os.path.exists(_PROXY_FILE):
            _proxies = []
        else:
            with open(_PROXY_FILE, "r") as f:
                _proxies = [line.strip() for line in f if line.strip() and not line.startswith("#")]
    return _proxies


def random_proxy():
    proxies = load_proxies()
    return random.choice(proxies) if proxies else None
