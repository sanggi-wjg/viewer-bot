from dataclasses import dataclass

import requests
import urllib3.exceptions


@dataclass(slots=True, order=True)
class Proxy:
    ip: str
    port: int
    is_alive: bool = False

    def get_address(self):
        return f"http://{self.ip}:{self.port}"

    def get_secured_address(self):
        return f"https://{self.ip}:8123"


_proxy_servers = [
    # korea proxy
    # Proxy("222.111.18.67", 80),
    # Proxy("3.37.125.76", 3128),
    # Proxy("3.39.235.191", 51860),
    # Proxy("3.39.235.191", 52636),
    # Proxy("3.39.235.191", 57581),
    # Proxy("119.196.168.183", 80),
    # Proxy("203.228.28.153", 80),
    # Proxy("158.180.68.39", 3128),
    # Proxy("183.100.14.134", 8000),
    # Proxy("59.31.175.137", 80),
    Proxy("118.42.113.37", 443),
    # Proxy("59.7.73.76", 80),
    # Proxy("221.153.92.39", 80),
    # Proxy("121.159.146.251", 80),
    # Proxy("175.213.76.24", 80),
    # Proxy("61.79.73.225", 80),
    # Proxy("110.12.211.140", 80),
    # Proxy("61.254.81.88", 9000),
    # Proxy("116.125.141.115", 80),
    # Proxy("121.182.138.71", 80),
    # Proxy("218.153.133.202", 8080),
    # Proxy("59.7.73.213", 80),
    # Proxy("14.50.81.64", 80),
    # Proxy("61.110.5.2", 80),
    # Proxy("222.103.50.47", 80),
    # Proxy("121.164.200.18", 8118),
    # Proxy("58.234.116.197", 8193),
    # Proxy("211.234.125.3", 443),
    # Proxy("211.234.125.5", 443),
    # Proxy("211.43.214.205", 80),
    # Proxy("203.253.142.176", 8080),
    # Proxy("220.77.195.132", 80),
    # Proxy("220.77.191.154", 3128),
    # Proxy("211.222.177.244", 3128),
    # Proxy("121.139.218.165", 31409),
]


def _check_is_alive(proxies: [Proxy]):
    for proxy in proxies:
        print(f"{proxy.ip}:{proxy.port}", end="\t\t\t\t")

        try:
            requests.get(
                proxy.get_address(),
                timeout=2,
            ).raise_for_status()

        except (
            requests.exceptions.ProxyError,
            requests.exceptions.SSLError,
            requests.exceptions.Timeout,
            ConnectionError,
        ) as e:
            proxy.is_alive = False
            print(f"fail, {e}", flush=True)

        else:
            proxy.is_alive = True
            print("ok", flush=True)

    return proxies


# PROXY_SERVERS = [proxy for proxy in _check_is_alive(_proxy_servers) if proxy.is_alive]
