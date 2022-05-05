import requests
import time
import re

HEADER1 = {
    'Host': 'm.nuaa.edu.cn',
    'Connection': 'close',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Sec-Fetch-Dest': 'empty',
    'X-Requested-With': 'XMLHttpRequest',
    'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 10; TAS-AN00 Build/HUAWEITAS-AN00)',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Origin': 'https://m.nuaa.edu.cn',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-Mode': 'cors',
    'Referer': 'https://m.nuaa.edu.cn/uc/wap/login/check',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cookie': ''
}

DAKA_ADDR = "https://m.nuaa.edu.cn/ncov/wap/default/save"
HEADER2 = {
    "accept": "application/json, text/javascript, /; q=0.01",
    "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,zh-TW;q=0.5,ja;q=0.4",
    "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
    "sec-ch-ua": 'Not A;Brand";v="99", "Chromium";v="101", "Microsoft Edge";v="101',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "macOS",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "x-requested-with": "XMLHttpRequest",
    'Origin': 'https://m.nuaa.edu.cn',
    "cookie": "eai-sess=j7iuosomkv6b6l7162qmama6p0; UUkey=886e61e1ee1d033f8bbf08e23d052550",
    "Referer": "https://m.nuaa.edu.cn/ncov/wap/default/index",
    "Referrer-Policy": "strict-origin-when-cross-origin"
}

import datetime

BODY = "sfzhux=1&zhuxdz=&szgj=&szcs=&szgjcs=&sfjwfh=0&sfyjsjwfh=0&sfjcjwfh=0&sflznjcjwfh=0&sflqjkm=4&jkmys=0&sfjtgfxdq=0&nuaaxgymjzqk=3&dyzjzsj=&bfhzjyq=2&hxyxjzap=2&yjzjsj=&sfjkyc=0&sftjlkjc=&lkjctlsj=&sfsylkjcss=&gjzsftjlkjc=&gjzlkjctlsj=&gjzsfsylkjcss=&ifhxjc=&hsjconetime=&hsjconeplace=&hsjconejg=&hsjctwotime=&hsjctwoplace=&hsjctwojg=&hsjcthreetime=&hsjcthreeplace=&hsjcthreejg=&hsjcfourtime=&hsjcfourplace=&hsjcfourjg=&ywchxjctime=&hsjclist=%7B%7D&njrddz=3460302&gzczxq=2&ifznqgfxljs=&iflsqgfxljs=&zrwjtw=1&jrzjtw=1&jrlvymjrq=&ifcyglq=0&wskmyy=&zhycjgdqifjn=&dqsfzgfxszqs=0&gqsfyzgfxljs=0&gqsfyqzfhryjc=0&sfyjwljqyhg=0&cjfxsfhs=1&bzxyy=&bzxyydesc=&id=25435620&uid=211865&date={}&tw=&sfcxtz=0&sfyyjc=0&jcjgqr=0&jcjg=&sfjcbh=0&sfcxzysx=0&qksm=&remark=&address=%E6%B1%9F%E8%8B%8F%E7%9C%81%E5%8D%97%E4%BA%AC%E5%B8%82%E6%B1%9F%E5%AE%81%E5%8C%BA%E7%A7%A3%E9%99%B5%E8%A1%97%E9%81%93%E7%A0%9A%E4%B8%9C%E8%B7%AF%E5%8D%97%E4%BA%AC%E8%88%AA%E7%A9%BA%E8%88%AA%E5%A4%A9%E5%A4%A7%E5%AD%A6%E5%B0%86%E5%86%9B%E8%B7%AF%E6%A0%A1%E5%8C%BA&area=%E6%B1%9F%E8%8B%8F%E7%9C%81+%E5%8D%97%E4%BA%AC%E5%B8%82+%E6%B1%9F%E5%AE%81%E5%8C%BA&province=%E6%B1%9F%E8%8B%8F%E7%9C%81&city=%E5%8D%97%E4%BA%AC%E5%B8%82&geo_api_info=%7B%22type%22%3A%22complete%22%2C%22position%22%3A%7B%22Q%22%3A31.939615071615%2C%22R%22%3A118.78905381944503%2C%22lng%22%3A118.789054%2C%22lat%22%3A31.939615%7D%2C%22location_type%22%3A%22html5%22%2C%22message%22%3A%22Get+ipLocation+failed.Get+geolocation+success.Convert+Success.Get+address+success.%22%2C%22accuracy%22%3A60%2C%22isConverted%22%3Atrue%2C%22status%22%3A1%2C%22addressComponent%22%3A%7B%22citycode%22%3A%22025%22%2C%22adcode%22%3A%22320115%22%2C%22businessAreas%22%3A%5B%7B%22name%22%3A%22%E5%BC%80%E5%8F%91%E5%8C%BA%22%2C%22id%22%3A%22320115%22%2C%22location%22%3A%7B%22Q%22%3A31.925973%2C%22R%22%3A118.80980399999999%2C%22lng%22%3A118.809804%2C%22lat%22%3A31.925973%7D%7D%5D%2C%22neighborhoodType%22%3A%22%22%2C%22neighborhood%22%3A%22%22%2C%22building%22%3A%22%22%2C%22buildingType%22%3A%22%22%2C%22street%22%3A%22%E5%B0%86%E5%86%9B%E5%A4%A7%E9%81%93%22%2C%22streetNumber%22%3A%2229%E5%8F%B7%22%2C%22country%22%3A%22%E4%B8%AD%E5%9B%BD%22%2C%22province%22%3A%22%E6%B1%9F%E8%8B%8F%E7%9C%81%22%2C%22city%22%3A%22%E5%8D%97%E4%BA%AC%E5%B8%82%22%2C%22district%22%3A%22%E6%B1%9F%E5%AE%81%E5%8C%BA%22%2C%22towncode%22%3A%22320115011000%22%2C%22township%22%3A%22%E7%A7%A3%E9%99%B5%E8%A1%97%E9%81%93%22%7D%2C%22formattedAddress%22%3A%22%E6%B1%9F%E8%8B%8F%E7%9C%81%E5%8D%97%E4%BA%AC%E5%B8%82%E6%B1%9F%E5%AE%81%E5%8C%BA%E7%A7%A3%E9%99%B5%E8%A1%97%E9%81%93%E7%A0%9A%E4%B8%9C%E8%B7%AF%E5%8D%97%E4%BA%AC%E8%88%AA%E7%A9%BA%E8%88%AA%E5%A4%A9%E5%A4%A7%E5%AD%A6%E5%B0%86%E5%86%9B%E8%B7%AF%E6%A0%A1%E5%8C%BA%22%2C%22roads%22%3A%5B%5D%2C%22crosses%22%3A%5B%5D%2C%22pois%22%3A%5B%5D%2C%22info%22%3A%22SUCCESS%22%7D&created=1651222741&sfzx=1&sfjcwhry=0&sfcyglq=0&gllx=&glksrq=&jcbhlx=&jcbhrq=&sftjwh=0&sftjhb=0&fxyy=&bztcyy=&fjsj=0&created_uid=0&sfjchbry=0&sfjcqz=&jcqzrq=&jcwhryfs=&jchbryfs=&xjzd=&sfsfbh=0&sfjcwzry=0&sftjwz=0&jhfjrq=&jhfjjtgj=&jhfjhbcc=&jhfjsftjwh=0&jhfjsftjhb=0&szsqsfybl=0&sfygtjzzfj=0&gtjzzfjsj=&sfsqhzjkk=0&sqhzjkkys=&is_fx_log=0&fxzrwjtw=0&fxjrcjtw=0&fxjrzjtw=0&fxsfzx=0&fxsfcyglq=0&fxsfcxtz=0&sfjzxg=0&skmcolor=1&skmimg=&ifjrglkjc=&gtjjsfhm=&gtjzsfhzl=&sffhddjjgc=&ifjgzgfxq=&jgzgfxrq=&jgzgfxdq=&jgzgfxxxdz=&newwchsjccs=&dsdecjcsj=&dsdechsjcjgtype=&dsdrchsjcdd=&dsdechsjcjg=&zhyccjcsj=&zhycchsjcjgtype=&zhycchsjcdd=&zhycchsjcjg=&hsjczm=&sfmrhs=&gwszdd=&sfyqjzgc=&jrsfqzys=&jrsfqzfy=&ismoved=0"


def login(user, passwd, t=None):
    HEADER1['Cookie'] = ''
    try:
        r = requests.get('https://m.nuaa.edu.cn/uc/wap/login', headers=HEADER1)
        print('get login page:', r.status_code)
        cookie = r.headers['Set-Cookie']
        cookie = re.search(r'eai-sess=([a-zA-Z0-9]+)', cookie).group(0)

        HEADER1['Cookie'] = cookie
        r = requests.get('https://m.nuaa.edu.cn/uc/wap/login/check', headers=HEADER1,
                         data='username={}&password={}'.format(user, passwd))
        print('login...:', r.status_code)

        cookie2 = r.headers['Set-Cookie']
        cookie = cookie + '; ' + re.search(r'UUkey=([a-zA-Z0-9]+)', cookie2).group(0)
        return cookie
    except Exception as e:
        print(f'Login failed. Exception: {e}')
        if t is not None:
            return login(user, passwd, t)
        else:
            return None


def sign(user, passwd):
    cookie = login(user, passwd)
    HEADER2['Cookie'] = cookie
    try:
        td = datetime.date.today()
        addzero = lambda x: f'0{x}' if x < 10 else str(x)
        data = BODY.format(f'{td.year}{addzero(td.month)}{addzero(td.day)}')
        r = requests.post('https://m.nuaa.edu.cn/ncov/wap/default/save',
                          data=data, headers=HEADER2)
        r.encoding = 'utf-8'
        print('sign return:', r.text)
        return u'成功' in r.text
    except Exception as e:
        print(f'Sign failed. Exception: {e}')
        return False


if __name__ == '__main__':
    already = set()
    while True:
        today = datetime.datetime.now()
        tstr = f'{today.year}-{today.month}-{today.day}'
        print(f'Checking {tstr}')
        if tstr not in already:
            print('Try to sign.')
            tried = 0
            succ = False
            while tried < 5:
                tried += 1
                res = sign('SX1122333', 'XXXX')
                if res:
                    succ = True
                    already.add(tstr)
                    print('Succeed!')
                    break
                else:
                    time.sleep(10)
                    print('Failed. Retry in 10 sec.')
            if not succ:
                print('Failed. Retry in next hour.')
        time.sleep(60 * 60)
