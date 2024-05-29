import requests
from bs4 import BeautifulSoup
from lxml import etree

if __name__ == "__main__":

    headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/124.0.0.0 Safari/537.36',
            'Hots': 'account.xiaomi.com'
        }
    resp = requests.get("https://account.xiaomi.com", headers=headers)
    soup = BeautifulSoup(resp.text, "lxml")
    print(soup.text)
    # title_lists = [tl.text.strip() for tl in soup.find_all("span", class_="title")]
    # other_lists = [tl.text.strip() for tl in soup.find_all("span", class_="other")]
    #
    # print([(x,y) for x,y in zip(title_lists, other_lists)])