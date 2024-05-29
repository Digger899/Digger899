import requests
from fake_useragent import UserAgent
import http.cookiejar as ckj
if __name__ == "__main__":


    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/124.0.0.0 Safari/537.36',
        'Hots': 'movie.douban.com'
    }
    url = "http://192.168.2.95:8700/#/system/organizationr"
    # postdata = {
    #     'account: '17374131136',
    #     'password': 'zyqq1234',
    #     'grant_type': 'password',
    #     'scope': 'server'
    # }
    session = requests.session()
    session.cookies = ckj.LWPCookieJar(filename='./cookies')
    res = requests.get(url, headers=headers)
    # login = session.post(url, data=postdata, headers=headers)
    print(res.status_code)
    print(res.text)
    session.cookies.save()
