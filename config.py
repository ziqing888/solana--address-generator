import multiprocessing

config = {
    "address_start": "12",  # 地址开头匹配
    "address_end": "",      # 地址结尾匹配
    "num_processes": multiprocessing.cpu_count() - 2,  # 使用的进程数
    "show_log": True,       # 是否显示日志
    "log_count": 5000       # 每隔多少次生成显示一次日志
}
