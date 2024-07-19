from random import randint
from os import system as cmd

def warning():
    print("用户协议",end="")
    text = """
警告
该程序具有类似病毒的功能，在运行前请务必备份好所有重要资料文件。
如非必要，请勿用该程序填充C盘或系统盘，否则可能造成系统崩溃等突发危险状况。
总之，该工具仅供学习参考，请勿用于非法用途或改编为非法计算机软件，否则可能面临法律问责！
请仔细阅读上述文本。"""
    red_bold = '\033[1;31m'
    reset = '\033[0m'
    print(f"{red_bold}{text}{reset}")
    print("若您同意上述内容，请在下方输入：\"我同意上述用户协议，并自愿承担运行后造成的所有后果。\"")
    print("若不同意，按CTRL+C退出程序。")
    ans = input("请输入：")
    if ans == "我同意上述用户协议，并自愿承担运行后造成的所有后果。":
        print("已同意用户协议。")
        print("请回答下列问题，以确认你是人类。")
        a = randint(1, 100)
        b = randint(1, 100)
        correctans = a + b
        userans = input(f"{a} + {b} = ")
        if int(userans) == correctans:
            print("回答正确，继续运行。")
            cmd("cls") 
        else:
            print("回答错误，程序退出。")
            exit(-1)
    else:
        print("用户协议未同意，程序退出。")
        exit(-1)

if __name__ == "__main__":
    warning()