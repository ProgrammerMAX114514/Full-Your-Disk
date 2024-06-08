import psutil # 这个模块不在python标准库内，需要自行下载安装，方法如下：
"""
具体安装方法：
1.按下win+r键，输入cmd，回车
2.输入pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple 回车(可选操作，这可以极大提升下载速度)
3.输入pip install psutil 回车
4.等待下载完成
"""
from os import system, listdir

# 获取用户操作选择，用于在程序中引导用户进行不同的操作
def getoperationchoice():
    while True:
        print("1.爆满磁盘\n2.恢复磁盘\n3.退出")
        choice = input("请输入你的选择：")
        if choice == "1":
            return 1
        elif choice == "2":
            return 2
        elif choice == "3":
            return 3
        else:
            print("输入错误，请重新输入")

# 根据用户选择执行对应的操作，包括填充磁盘和恢复磁盘空间
def performoperation(choice):
    if choice == 1:
        disk = input("输入要爆满磁盘的盘符: ")
        createdirectory(disk)
        num=0
        while True:
            remaining_space = getdiskremaining(disk)
            if remaining_space == 0:
                print("目标磁盘已被爆满！")
                break
            print(f"剩余空间: {remaining_space} 字节")
            createfile(disk, remaining_space, num)
            num+=1
    elif choice == 2:
        disk = input("输入要恢复磁盘的盘符: ")
        system(f"attrib -s -h {disk}:\\diskkiller")
        system(f"del /q {disk}:\\diskkiller\\*")
        system(f"rmdir {disk}:\\diskkiller")
        print("磁盘已恢复")
    else:
        exit()

# 在指定磁盘上创建一个隐藏目录，用于后续填充磁盘空间
def createdirectory(disk):
    if not "diskkiller" in listdir(disk + ":\\"):
        system(f"mkdir {disk}:\\diskkiller")
    system(f"attrib +s +h {disk}:\\diskkiller")

# 在指定目录下创建一个大文件，用于消耗磁盘空间
def createfile(disk, size, num):
    file = f"{disk}:\\diskkiller\\{num}"
    command = f"fsutil file createnew {file} {size}"
    system(command)

# 获取指定磁盘的剩余空间
def getdiskremaining(disk):
    # 检查磁盘盘符是否有效
    if disk.upper() not in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']:
        raise ValueError(f"无效盘符：{disk}")
    # 获取磁盘使用信息
    partitions = psutil.disk_partitions()
    for partition in partitions:
        # 查找指定盘符的分区信息
        if partition.mountpoint.startswith(disk + ":\\"):
            # 获取磁盘使用统计
            usage = psutil.disk_usage(partition.mountpoint)
            # 返回剩余空间（字节）
            return usage.free

    # 如果没有找到对应的磁盘分区，抛出异常
    raise ValueError(f"没有指定的磁盘: {disk}")

# 主程序入口，循环引导用户进行操作
if __name__ == '__main__':
    while True:
        choice = getoperationchoice()
        performoperation(choice)