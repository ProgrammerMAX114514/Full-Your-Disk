from os import system as cmd

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

if __name__ == "__main__":
    print("你不应该直接运行此文件。")