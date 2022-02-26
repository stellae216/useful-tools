import requests
import sys
import os

from tools.tools import MyArgParse


class RunArgsError(Exception):
    pass


p = MyArgParse()
p.set_argparse(argv=["--url"],
               help_msg="jetbrains code url")
url = p.get_arg_value("url")
r = requests.get(url)
if r.status_code != 200:
    print('激活码下载失败！')
    sys.exit(0)
file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "jihuoma.zip"))
with open(file_path, 'wb') as f:
    f.write(r.content)
print('下载成功！激活码保存位置：', file_path)
