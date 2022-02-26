import secrets
import string

from tools.myargparse import MyArgParse


class MissLengthParamError(Exception):
    pass


p = MyArgParse()
p.set_argparse(argv=["-n"],
               help_msg="生成随机密码长度")
length = p.get_arg_value("n")
characters = string.ascii_letters + string.digits
bad_password = ''.join(secrets.choice(characters) for _ in range(int(length)))
print(bad_password)
