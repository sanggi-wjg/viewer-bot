from selenium import webdriver

from app.utils.proxy import PROXY_SERVERS

url = "https://sanggi-jayg.tistory.com/entry/Gradle-Gradle-dependency-%EA%B7%B8%EB%9E%98%EB%93%A4-%EC%A2%85%EC%86%8D%EC%84%B1-%EC%84%A0%EC%96%B8"

if __name__ == "__main__":

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
    chrome_options.add_argument("--disable-logging")
    # chrome_options.add_argument("--lang=en")
    # chrome_options.add_argument("--headless")
    chrome_options.add_argument("--log-level=3")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--mute-audio")
    chrome_options.add_argument("--disable-dev-shm-usage")

    chrome = webdriver.Chrome(options=chrome_options)

    for proxy in PROXY_SERVERS:
        # how to set proxy, https://stackoverflow.com/questions/65156932/selenium-proxy-server-argument-unknown-error-neterr-tunnel-connection-faile
        webdriver.DesiredCapabilities.CHROME["proxy"] = {
            "httpProxy": f"{proxy.ip}:{proxy.port}",
            "ftpProxy": f"{proxy.ip}:{proxy.port}",
            "sslProxy": f"{proxy.ip}:{proxy.port}",
            "proxyType": "MANUAL",
        }
        webdriver.DesiredCapabilities.CHROME["acceptSslCerts"] = True

        chrome.get(url)
        chrome.implicitly_wait(2)
