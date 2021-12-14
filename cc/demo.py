import requests

proxypool_url = 'http://192.168.99.100:5555/random'
target_url = 'https://kk.hackerjk.top/'


def get_random_proxy():
    """
    get random proxy from proxypool
    :return: proxy
    """
    return requests.get(proxypool_url).text.strip()


def crawl(url, proxy):
    """
    use proxy to crawl page
    :param url: page url
    :param proxy: proxy, such as 8.8.8.8:8888
    :return: html
    """
    proxies = {'http': 'http://' + proxy}
    return requests.get(url, proxies=proxies).status_code


def main():
    """
    main method, entry point
    :return: none
    """
    proxy = get_random_proxy()
    print('get random proxy', proxy)
    status_code = crawl(target_url, proxy)
    print(status_code)


if __name__ == '__main__':
    main()
