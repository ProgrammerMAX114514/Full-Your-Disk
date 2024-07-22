from warning import *
from getoperationchoice import *
from performoperation import *
from checksys import *

cmd("title 磁盘爆满工具")
version="v0.4.0"


# 主程序入口，循环引导用户进行操作
if __name__ == '__main__':
    # 调用函数检查系统环境
    checksys()
    warning()
    while True:
        choice = getoperationchoice(version)
        performoperation(choice)