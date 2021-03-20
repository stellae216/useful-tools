import requests
import sys
import os


url = 'http://idea.medeming.com/jets/images/jihuoma.zip'
filename = 'jihuoma.zip'
r = requests.get(url)
if r.status_code != 200:
    print('激活码下载失败！')
    sys.exit(0)
file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), filename))
with open(file_path, 'wb') as f:
    f.write(r.content)
print('下载成功！激活码保存位置：', file_path)
