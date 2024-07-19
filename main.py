try:
    from psutil import disk_usage, disk_partitions  # 这个模块不在python标准库内，需要自行下载安装。
except ImportError:
    print("无法导入psutil模块，请确认psutil模块是否安装成功。")
    help_text="""具体安装方法：
    1.按下win+r键，输入cmd，回车
    2.输入pip install psutil回车
        若国外源下载过慢，可以使用清华镜像源：pip install -i https://pypi.tuna.tsinghua.edu.cn/simple psutil
    3.等待下载完成
    """
    print(help_text)
from warning import *
from os import remove,rmdir
from os import listdir
from getoperationchoice import *
from checksys import *

cmd("title 磁盘爆满工具")
version="v0.4.0"

# 根据用户选择执行对应的操作，包括填充磁盘和恢复磁盘空间
def performoperation(choice):
    if choice == 1:
        disk = input("输入要爆满磁盘的盘符: ")
        if disk.upper() == "C":
            ans = input("这可能是系统盘，爆满它将会非常危险。是否继续？(y/n) :")
            if ans.lower() == "y":
                dokill=True
            else:
                dokill=False
        else:
            dokill=True
        if dokill:
            createdirectory(disk)
            num = 0
            while True:
                remaining_space = getdiskremaining(disk)
                if remaining_space == 0:
                    print("目标磁盘已被爆满！")
                    break
                print(f"剩余空间: {remaining_space} 字节")
                createfile(disk, remaining_space, num)
                num += 1
        else:
            print("操作已取消。")
    elif choice == 2:
        disk = input("输入要恢复磁盘的盘符: ")
        cmd(f"attrib -s -h {disk}:\\diskkiller") 
        cmd(f"del /q {disk}:\\diskkiller\\*") 
        rmdir(f"{disk}:\\diskkiller") 
        print("磁盘已恢复")
    else:
        exit()
    cmd("pause")
    cmd("cls")


# 在指定磁盘上创建一个隐藏目录，用于后续填充磁盘空间
def createdirectory(disk):
    if not "diskkiller" in listdir(disk + ":\\"):
        cmd(f"mkdir {disk}:\\diskkiller") 
    cmd(f"attrib +s +h {disk}:\\diskkiller") 


# 在指定目录下创建一个大文件，用于消耗磁盘空间
def createfile(disk, size, num):
    file = f"{disk}:\\diskkiller\\{num}"
    command = f"fsutil file createnew {file} {size}"
    ret_code=cmd(command)
    if ret_code == 0:
        print(f"已创建文件{file}，大小为{size}字节")
    else:
        print(f"创建文件{file}失败，错误码为{ret_code}。您的系统可能没有fsutil命令或格式不兼容。请联系开发者寻求帮助")
        cmd("pause") 


# 获取指定磁盘的剩余空间
def getdiskremaining(disk):
    # 检查磁盘盘符是否有效
    if disk.upper() not in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                            'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']:
        raise ValueError(f"无效盘符：{disk}")
    # 获取磁盘使用信息
    partitions = disk_partitions()
    for partition in partitions:
        # 查找指定盘符的分区信息
        if partition.mountpoint.startswith(f"{disk}:\\"):
            # 获取磁盘使用统计
            usage = disk_usage(partition.mountpoint)
            # 返回剩余空间（字节）
            return usage.free

    # 如果没有找到对应的磁盘分区，抛出异常
    raise ValueError(f"没有指定的磁盘: {disk}")


# 主程序入口，循环引导用户进行操作
if __name__ == '__main__':
    # 调用函数检查系统环境
    checksys()
    warning()
    while True:
        choice = getoperationchoice()
        performoperation(choice)