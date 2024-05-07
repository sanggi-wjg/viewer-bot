import random
import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

# url = "https://sanggi-jayg.tistory.com/entry/Gradle-Gradle-dependency-%EA%B7%B8%EB%9E%98%EB%93%A4-%EC%A2%85%EC%86%8D%EC%84%B1-%EC%84%A0%EC%96%B8"
url = "https://sanggi-jayg.tistory.com/entry/CDC-MySQL-Debezium-Change-Data-Capture-%EB%94%B0%EB%9D%BC%ED%95%B4%EB%B3%B4%EA%B8%B0-3"

proxy_servers = [
    "https://www.blockaway.net",
    "https://www.croxyproxy.com",
    "https://www.croxyproxy.rocks",
    "https://www.croxy.network",
    "https://www.croxy.org",
    "https://www.youtubeunblocked.live",
    "https://www.croxyproxy.net",
]


def random_proxy() -> str:
    return random.choice(proxy_servers)


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

    driver = webdriver.Chrome(
        options=chrome_options,
        # service=Service(
        #     executable_path="driver/114.0.5735.90/chromedriver_mac_arm64/chromedriver"
        # ),
    )
    try:
        for i in range(1, 101):
            print(f"open new tab No.{i}")
            driver.switch_to.window(driver.window_handles[-1])

            driver.execute_script(f"window.open('{random_proxy()}')")
            driver.switch_to.window(driver.window_handles[-1])

            text_box = driver.find_element(By.ID, "url")
            text_box.send_keys(url)
            text_box.send_keys(Keys.ENTER)
            time.sleep(10)

            while driver.execute_script("return document.readyState") != "complete":
                pass

            driver.close()
            print("close tab")
    finally:
        # input("Press Enter to exit...")
        print("close driver")
        driver.quit()
