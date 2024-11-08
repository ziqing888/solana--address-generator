# SOL钱包生成器

一个简单的 Solana 地址生成器，支持多进程并行处理，并提供自定义的地址前缀和后缀匹配功能。
---

## 安装步骤

：下载或克隆此项目代码
```bash
git clone https://github.com/ziqing888/solana--address-generator

```

 ```bash
cd solana--address-generator

  ```
###  安装依赖：

脚本使用了几个 Python 库来生成 Solana 地址和管理依赖。请确保系统已安装 Python 环境，然后运行以下命令：

```bash
pip install -r requirements.txt

  ```
### 配置生成条件

在 config.py 文件可以根据需要修改以下参数：
```bash
# config.py
import multiprocessing

config = {
    "address_start": "77",  # 地址开头匹配
    "address_end": "",      # 地址结尾匹配
    "num_processes": multiprocessing.cpu_count() - 2,  # 使用的进程数
    "show_log": True,       # 是否显示日志
    "log_count": 5000       # 每隔多少次生成显示一次日志
}

  ```
address_start：设置生成地址的开头字符。
address_end：设置生成地址的结尾字符。
num_processes：并行进程数，建议设置为 CPU 核心数 - 1，提高生成效率。
show_log：是否显示生成进度的日志。
log_count：每隔 log_count 次生成显示一次进度。
### 执行以下命令启动地址生成器：
```bash
python main.py
 ```
### 查看生成文件

文件保存到当前目录，文件名格式为：YYYY-MM-DD_HH-MM-SS_<address_start>.txt。

可以使用以下命令查看生成文件内容：
```bash
cat <filename>.txt
 ```
### 注意事项
生成符合条件的地址可能会耗时较长，具体时间取决于设置的 address_start 和 address_end 的条件。
确保生成的私钥文件安全存放，防止泄露。
项目在多核 CPU 上运行效果最佳，单核系统可能会影响生成效率。
如果条件匹配过于严格（例如，地址要求4位或更多的指定后缀），生成时间可能会显著增加。
