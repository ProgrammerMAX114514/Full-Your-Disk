from os import system as cmd

# 获取用户操作选择，用于在程序中引导用户进行不同的操作
def getoperationchoice(version):
    while True:
        print(f"爆满磁盘工具(Full-Your-Disk) {version} by ProgrammerMAX114514")
        print("该项目已在Github上开源，开源地址：https://github.com/ProgrammerMAX114514/Full-Your-Disk")
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
            cmd("pause")

if __name__ == "__main__":
    print("你不应该直接运行此文件。")