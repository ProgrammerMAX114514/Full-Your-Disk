from os import system as cmd
from os import rmdir

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

