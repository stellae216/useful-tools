import requests
import argparse
import sys
import os


class RunArgsError(Exception):
    pass


parser = argparse.ArgumentParser()
parser.add_argument("--url", help="jetbrains code url")
args = parser.parse_args()
url = args.url
if not url:
    raise RunArgsError("运行参数错误")

r = requests.get(url)
if r.status_code != 200:
    print('激活码下载失败！')
    sys.exit(0)
file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "jihuoma.zip"))
with open(file_path, 'wb') as f:
    f.write(r.content)
print('下载成功！激活码保存位置：', file_path)
