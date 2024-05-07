from dataclasses import dataclass

import requests


@dataclass(slots=True)
class Proxy:
    ip: str
    port: int
    is_alive: bool = False

    def get_address(self):
        return f"http://{self.ip}:{self.port}"

    # def get_secured_address(self):
    #     return f"https://{self.ip}:{self.port}"


_proxy_servers = [
    # korea proxy
    # Proxy("222.111.18.67", 80),
    # Proxy("3.37.125.76", 3128),
    # Proxy("3.39.235.191", 51860),
    # Proxy("3.39.235.191", 52636),
    # Proxy("3.39.235.191", 57581),
    Proxy("119.196.168.183", 80),
    Proxy("203.228.28.153", 80),
    # Proxy("158.180.68.39", 3128),
    # Proxy("183.100.14.134", 8000),
    # Proxy("59.31.175.137", 80),
    Proxy("118.42.113.37", 443),
    Proxy("59.7.73.76", 80),
    Proxy("221.153.92.39", 80),
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
    # global proxy
    Proxy("111.59.4.88", 9002),
    Proxy("45.234.61.2", 999),
    Proxy("111.206.0.99", 8181),
    Proxy("24.106.221.230", 53281),
    Proxy("200.116.198.222", 9812),
    Proxy("5.104.174.199", 23500),
    Proxy("13.234.24.116", 1080),
    Proxy("157.245.14.43", 8888),
    Proxy("103.130.145.169", 80),
    Proxy("52.35.240.119", 1080),
    Proxy("51.210.19.141", 80),
    Proxy("162.245.85.220", 80),
    Proxy("44.226.167.102", 3128),
    Proxy("45.43.32.228", 80),
    Proxy("65.21.159.49", 80),
    Proxy("162.223.94.166", 80),
    Proxy("60.205.132.71", 80),
    Proxy("185.49.31.205", 8080),
    Proxy("217.218.248.226", 3128),
    Proxy("185.49.31.207", 8081),
    Proxy("18.228.149.161", 80),
    Proxy("77.68.77.181", 80),
    Proxy("3.78.92.159", 80),
    Proxy("211.222.252.187", 8193),
    Proxy("62.182.204.81", 88),
    Proxy("42.118.202.113", 4006),
    Proxy("18.135.133.116", 1080),
    Proxy("65.1.244.232", 80),
    Proxy("35.154.71.72", 1080),
    Proxy("43.255.113.232", 82),
    Proxy("18.133.16.21", 1080),
    Proxy("18.135.133.116", 3128),
    Proxy("35.178.104.4", 3128),
    Proxy("3.10.93.50", 1080),
    Proxy("154.16.146.43", 80),
]


def _check_is_alive(proxies: [Proxy]):
    for proxy in proxies:
        print(f"{proxy.ip}:{proxy.port}", end="\t\t\t")

        try:
            resp = requests.get(
                proxy.get_address(),
                timeout=2,
                # allow_redirects=False
            )
            resp.raise_for_status()
            # resp2 = requests.get(
            #     proxy.get_address(),
            #     timeout=2,
            #     verify=False,
            #     # allow_redirects=False
            # )
            # if not resp.ok and not resp2.ok:
            #     resp.raise_for_status()
            #     resp2.raise_for_status()
            # if resp.is_redirect or resp2.is_redirect:
            #     raise requests.HTTPError()

        except requests.RequestException as e:
            proxy.is_alive = False
            print(f"fail, {e}", flush=True)
        else:
            proxy.is_alive = True
            print("ok", flush=True)
    return proxies


# PROXY_SERVERS = [proxy for proxy in _check_is_alive(_proxy_servers) if proxy.is_alive]
