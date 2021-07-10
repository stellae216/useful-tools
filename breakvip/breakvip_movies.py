import os
import sys
import re
import argparse
import requests


def get_web_content(web_url: str) -> str:
    """获取web内容"""
    headers = {
        "User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
    }
    response = requests.get(web_url, headers=headers)
    if response.status_code == 200:
        return response.text
    sys.exit('web地址不存在！')


def find_mv_source_url(html: str) -> str:
    """获取电影基本地址信息"""
    # re.S去除空白，()中的内容为抓取内容
    pattern = re.compile('video: {url: "(.*?)/pl\.m3u8"', re.S)
    targets = re.findall(pattern, html)
    if not targets:
        sys.exit('获取电影地址失败！')
    return targets[0]


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--address", help="input breakvip online address")
    args = parser.parse_args()
    if not args.address:
        sys.exit('请将影院地址作为参数传入，例如：--address www.google.com')
    web_content = get_web_content(args.address)
    source_url = find_mv_source_url(web_content)
    mv_name = source_url.rsplit('/', 1)[-1]
    mv_save_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), mv_name + '.ts')
    with open(mv_save_path, 'wb') as f:
        i = 0
        flag = None
        while True:
            if flag is True:
                break
            part_url = f'{source_url}/{mv_name}.{i:>06}.ts'
            print(f'{i}.request {part_url}')
            r = requests.get(part_url)
            code = r.status_code
            if code == 200:
                f.write(r.content)
                flag = False
            elif code == 404:
                # 可能出现开始起始资源404的情况。修改策略为：成功下载资源后，再次出现404为结束。
                if flag is False:
                    flag = True
            else:
                print(f'下载失败：{part_url}')
                sys.exit(0)
            i = i + 1

    print(f'下载完成，电影保存位置：{mv_save_path}')


