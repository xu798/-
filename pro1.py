import requests
import random
from bs4 import BeautifulSoup


def download_page(url, proxies):
   use_agent = "User-Agent:Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.109 Safari/537.36"
   header = {'User-Agent': use_agent}
   r = requests.post(url, header, proxies)  # 增加headers, 模拟浏览器
  # print(r.status_code)
   soup = BeautifulSoup(r.text, 'html.parser')
   return r.text


def download_next_page(url, proxies):
   use_agent = "User-Agent:Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.109 Safari/537.36"
   header = {'User-Agent': use_agent}
   r = requests.post(url, header, proxies)  # 增加headers, 模拟浏览器
   soup = BeautifulSoup(r.text, 'html.parser')
   return r.text


def get_booktext(book_link, proxy):
    new_url_text = download_next_page(book_link, proxy)
    soup = BeautifulSoup(new_url_text, 'lxml')
    con = soup.find_all('div', class_="article_main arc-no-select")
    for i in con:
        cont = i.get_text()
        save_txt(cont)
        print(cont)


def get_content(url_text, proxy):
    soup = BeautifulSoup(url_text, 'html.parser')
    b_title = soup.find_all('ul', class_="chapterList")
    for i in b_title:
        title = i.find_all('li', class_="chapter")
        for a in title:
            book_title = a.find('span', class_="chapterName").text
            book_link = a.find('a')['href']
            book_link_new = 'https://wwwj.bearead.com'+book_link
            print(book_title)
            print(book_link)
            save_txt(book_title)
            get_booktext(book_link_new, proxy)



def save_txt(*args):
   for i in args:
       with open('2.txt', 'a', encoding='utf-8') as f:
           f.write(i)

##


def get_ip_list(url):
    headers = {
        'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36"
    }
    web_data = requests.post(url=url, headers=headers)
    soup = BeautifulSoup(web_data.text, 'html.parser')
    ips = soup.find_all('tr', class_="odd")
    ip_list = []
    for i in ips:
        tds = i.find_all('td')
        ip_list.append(tds[1].text + ':' + tds[2].text)
    return ip_list


def get_random_ip(ip_list):
    proxy_list = []
    for ip in ip_list:
        proxy_list.append('https://' + ip)
     #   proxy_list.append('https://' + ip)
    proxy_ip = random.choice(proxy_list)
    proxies = {'http': proxy_ip}
    print(proxies)
    return proxies


def get_ip(ip_url):
    ip_list = get_ip_list(ip_url)
    proxies = get_random_ip(ip_list)
    return proxies

##


def main():
    ip_url = 'http://www.xicidaili.com/nn/'
    proxy = get_ip(ip_url)
    url = input('请输入网站名：')
    url_text = download_page(url, proxy)
    get_content(url_text, proxy)


if __name__ == '__main__':
   main()