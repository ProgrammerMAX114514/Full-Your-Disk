from platform import system
from os import system as cmd

def checksys():
    """
    检查当前是否为Windows环境。
    如果不是Windows环境，则输出错误信息。
    """
    os_name = system()
    if os_name != "Windows":
        print(f"该程序无法在{os_name}环境下运行")
        cmd("pause") 
        exit(-1)

if __name__ == "__main__":
    checksys()