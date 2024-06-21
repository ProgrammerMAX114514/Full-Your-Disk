# 磁盘爆满工具 - Full Your Disk

### 警告：该程序具有类似病毒的功能，在运行前请务必备份好所有重要资料文件。如非必要，请勿用该程序填充C盘或系统盘，否则可能造成系统崩溃等突发危险状况。
### 总之，该工具仅供学习参考，请勿用于非法用途或改编为非法计算机软件，否则可能面临法律问责！

这是一个简单的Python脚本工具，旨在帮助用户快速填满或恢复指定磁盘的空间。通过本工具，你可以检查磁盘容量是否有问题（如：扩容盘）。
## 特性

- **磁盘填充**：按需创建大文件以占满指定磁盘空间。
- **空间恢复**：删除之前创建的隐藏目录及其内容，恢复磁盘空间。

## 依赖

- Python 3.x
- [psutil](https://pypi.org/project/psutil/)：非标准库，在这个程序中用以获取磁盘分区、剩余空间信息。
- Windows操作系统：本工具只能在Windows操作系统下运行。

## 安装指南

### 安装Python与psutil

1. **确保Python 3.x已安装**。可以在[Python官网](https://www.python.org/downloads/)下载安装。
2. 打开命令行工具（Windows用户可以按`Win + R`，输入`cmd`后回车）。
3. （可选，但推荐）为了加速下载，可以设置pip使用国内镜像源，如清华大学镜像源：
   `pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple`
4. 安装`psutil`库：
   `pip install psutil`

### 使用说明

1. 将本项目克隆到本地：
   `git clone https://github.com/ProgrammerMAX114514/Full-Your-Disk.git`
2. 进入项目目录：
   `cd Full-Your-Disk`
3. 运行脚本：
   `python main.py`

4. 按照提示操作即可。

## 注意事项

- 在执行磁盘填充操作前，请确保所选磁盘有足够的非重要数据可以被覆盖或有备份，以防数据丢失。
- 使用此工具请谨慎，不当操作可能导致数据丢失或其他系统问题。

---
