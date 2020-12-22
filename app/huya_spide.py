import requests
import re
from app import huya_real_url as real
from bs4 import BeautifulSoup

def get_page(url):

    """  获取页面  """

    # 设置请求头
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/80.0.3987.132 Safari/537.36 Edg/80.0.361.66',
        'Referer': 'https://www.huya.com/'
    }
    response = requests.get(url, headers=header)

    if response.status_code == 200:
        return response.text
    return None


def get_fan(url):
    # 设置请求头
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/80.0.3987.132 Safari/537.36 Edg/80.0.361.66',
        'Referer': 'https://www.huya.com/'
    }
    r = requests.get(url, headers=header)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    html = BeautifulSoup(r.text, 'html.parser')
    funs = html.find('div', id='activityCount').get_text()
    return funs


def parse_html(html):

    """  利用正则表达式解析网页  """

    pattern = re.compile(
        '"gameFullName".*?"(.*?)",.*?totalCount".*?"(.*?)",.*?roomName".*?"(.*?)",.*?nick".*?"(.*?)",'
        '.*?introduction".*?"(.*?)",.*?profileRoom".*?"(.*?)"', re.S
    )
    items = re.findall(pattern, html)
    for index, item in enumerate(items):
        yield {
            '当前页序号': index,
            '类别': item[0].encode('utf-8').decode('unicode_escape'),  # 解码encode('utf-8').decode('unicode_escape')
            # '标题': item[2].encode('utf-8').decode('unicode_escape'),
            '主播': item[3].encode('utf-8').decode('unicode_escape'),
            '关注数': get_fan('https://www.huya.com/' + str(item[5])),
            '人气': item[1],
            '直播介绍': item[4].encode('utf-8').decode('unicode_escape'),
            '房间号': str(item[5]),
            '直播间源地址': real.get_real_url(str(item[5]))

        }


def main(page_no):
    # url = 'https://www.huya.com/cache.php?m=LiveList&do=getLiveListByPage&gameId=1&tagAll=0&page=' + str(page_no)
    # gameId=1 1是英雄联盟  2是地下城   删掉gameID参数为混合列表
    url = 'https://www.huya.com/cache.php?m=LiveList&do=getLiveListByPage&tagAll=0&page=' + str(page_no)
    html = get_page(url)
    # 网页解析返回yield生成器类型
    n = 0
    for item in parse_html(html):
        n += 1
        print(item)
        if n > 5:
            break


if __name__ == '__main__':
    for i in range(1, 10):
        main(page_no=i)
