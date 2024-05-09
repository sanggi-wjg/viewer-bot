import requests

from app.utils.proxy import Proxy

# url = "https://sanggi-jayg.tistory.com/entry/Gradle-Gradle-dependency-%EA%B7%B8%EB%9E%98%EB%93%A4-%EC%A2%85%EC%86%8D%EC%84%B1-%EC%84%A0%EC%96%B8"
url = "https://www.howsmyssl.com"

if __name__ == "__main__":
    # for proxy in PROXY_SERVERS:
    for proxy in [Proxy("210.212.39.138", 8080)]:
        resp = requests.get(
            url,
            proxies={
                "http": proxy.get_address(),
                "https": proxy.get_address(),
            },
            allow_redirects=True,
            # timeout=3,
            headers={
                # "X-Requested-With": "XMLHttpRequest",
                "Accept": "*/*",
                "Accept-Language": "en-US,en;q=0.9,ko-KR;q=0.8,ko;q=0.7",
                "Referer": "www.google.com",
                "Host": "www.google.com",
                "Connection": "keep-alive",
                "Pragma": "no-cache",
                "Cache-Control": "no-cache",
                "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
            },
        )
        print(resp.status_code, resp.text)
