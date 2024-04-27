from dataclasses import dataclass

import requests
from selenium import webdriver


@dataclass(slots=True)
class Proxy:
    ip: str
    port: str
    is_alive: bool = False


proxy_servers = [
    Proxy("222.111.18.67", "80"),
    # Proxy("3.37.125.76", "3128"),
    Proxy("3.39.235.191", "51860"),
    Proxy("3.39.235.191", "52636"),
    Proxy("3.39.235.191", "57581"),
    Proxy("119.196.168.183", "80"),
    Proxy("203.228.28.153", "80"),
    Proxy("158.180.68.39", "3128"),
    Proxy("183.100.14.134", "8000"),
    Proxy("59.31.175.137", "80"),
    Proxy("118.42.113.37", "443"),
    Proxy("59.7.73.76", "80"),
    Proxy("221.153.92.39", "80"),
    Proxy("121.159.146.251", "80"),
    Proxy("175.213.76.24", "80"),
    Proxy("61.79.73.225", "80"),
    Proxy("110.12.211.140", "80"),
    Proxy("61.254.81.88", "9000"),
    Proxy("116.125.141.115", "80"),
    Proxy("121.182.138.71", "80"),
    Proxy("218.153.133.202", "8080"),
    Proxy("59.7.73.213", "80"),
    Proxy("14.50.81.64", "80"),
    Proxy("61.110.5.2", "80"),
    Proxy("222.103.50.47", "80"),
    Proxy("121.164.200.18", "8118"),
    Proxy("58.234.116.197", "8193"),
    Proxy("211.234.125.3", "443"),
    Proxy("211.234.125.5", "443"),
    Proxy("211.43.214.205", "80"),
    Proxy("203.253.142.176", "8080"),
    Proxy("220.77.195.132", "80"),
    Proxy("220.77.191.154", "3128"),
    Proxy("211.222.177.244", "3128"),
    Proxy("121.139.218.165", "31409"),
]


# @using_thread
def check_alive_proxy(proxy: Proxy):
    try:
        res = requests.get(f"http://{proxy.ip}:{proxy.port}", timeout=5)
        res.raise_for_status()
    except (
        requests.HTTPError,
        requests.Timeout,
        requests.ConnectionError,
        requests.ConnectTimeout,
        Exception,
    ):
        proxy.is_alive = False
    else:
        proxy.is_alive = True


url = "https://sanggi-jayg.tistory.com/entry/Gradle-Gradle-dependency-%EA%B7%B8%EB%9E%98%EB%93%A4-%EC%A2%85%EC%86%8D%EC%84%B1-%EC%84%A0%EC%96%B8"

if __name__ == "__main__":

    for proxy in proxy_servers:
        check_alive_proxy(proxy)
        if not proxy.is_alive:
            continue

        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
        chrome_options.add_argument("--disable-logging")
        # chrome_options.add_argument("--lang=en")
        # chrome_options.add_argument("--headless")
        chrome_options.add_argument("--log-level=3")
        chrome_options.add_argument("--disable-extensions")
        chrome_options.add_argument("--mute-audio")
        chrome_options.add_argument("--disable-dev-shm-usage")

        # how to set proxy, https://stackoverflow.com/questions/65156932/selenium-proxy-server-argument-unknown-error-neterr-tunnel-connection-faile
        webdriver.DesiredCapabilities.CHROME["proxy"] = {
            "httpProxy": f"{proxy.ip}:{proxy.port}",
            "ftpProxy": f"{proxy.ip}:{proxy.port}",
            "sslProxy": f"{proxy.ip}:{proxy.port}",
            "proxyType": "MANUAL",
        }
        webdriver.DesiredCapabilities.CHROME["acceptSslCerts"] = True

        chrome = webdriver.Chrome(options=chrome_options)
        chrome.get(url)
        chrome.close()
