import sys
import argparse

from typing import List


class MyArgParse(object):
    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.argv = []

    def set_argparse(self, argv: List[str], help_msg: str):
        """
        设置请求命令行选项、参数和子命令解析器
        :param argv: 解析关键字参数
        :param help_msg: 帮助说明信息
        :param error_msg: 参数错误提示信息
        :return:
        """
        if not argv:
            sys.exit("请添加argparse参数")
        self.parser.add_argument(*argv, help=help_msg)
        self.argv.extend(argv)

    def get_arg_value(self, name: str) -> str:
        """
        获取命令行参数值
        :param name: 参数名
        :return:
        """
        args = self.parser.parse_args()
        val = args.__getattribute__(name)
        if not val:
            msg = "please add args..."
            for arg in self.argv:
                if name == arg.replace("-", ""):
                    msg = "please add args: " + arg
            sys.exit(msg)
        return val
