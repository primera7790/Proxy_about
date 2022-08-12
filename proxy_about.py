import requests
from bs4 import BeautifulSoup
# from proxy_info import login, password

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'
}

# Выбираем вариант сообщения прокси: либо через привязку к ip, либо через логин и пароль. На место 'ip:port' прописываем действующие значения.
proxies = {
    'https': 'http://ip:port'
    # 'https': f'http://{login}:{password}@ip:port'
}


def get_location(url):
    req = requests.get(url=url, headers=headers, proxies=proxies)
    soup = BeautifulSoup(req.text, 'lxml')

    ip = soup.find('div', class_='ip').text.strip()
    location = soup.find('div', class_='value-country').text.strip()
    print(f'IP: {ip} \nLocation: {location}')


def main():
    get_location(url='https://2ip.ru')


if __name__ == '__main__':
    main()
