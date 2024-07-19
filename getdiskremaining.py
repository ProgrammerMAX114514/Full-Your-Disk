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

if __name__ == "__main__":
    print("你不应该直接运行此文件。")