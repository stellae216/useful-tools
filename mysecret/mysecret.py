import secrets
import string
import argparse


class MissLengthParamError(Exception):
    pass


parse = argparse.ArgumentParser()
parse.add_argument("-n", help="生成随机密码长度")
args = parse.parse_args()
if not args.n:
    raise MissLengthParamError("缺少长度参数，try '-n <length>'")
length = int(args.n)
characters = string.ascii_letters + string.digits
bad_password = ''.join(secrets.choice(characters) for _ in range(length))
print(bad_password)
