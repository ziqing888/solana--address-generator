import os
import multiprocessing
import concurrent.futures
from config import config
from wallet_generator import generate_wallet, matches_address
from utils import log_progress, save_wallet_to_file
import time

# ANSI 颜色代码
YELLOW = '\033[93m'
RESET = '\033[0m'

def display_header():
    """清屏并打印带黄色边框的 Logo 和信息"""
    # 清屏
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # 打印带边框的 Logo 信息
    print(f"{YELLOW}╔════════════════════════════════════════╗")
    print(f"{YELLOW}║      🚀  sol地址生成器 🚀             ║")
    print(f"{YELLOW}║  👤    脚本编写：@qklxsqf              ║")
    print(f"{YELLOW}║  📢  电报频道：https://t.me/ksqxszq    ║")
    print(f"{YELLOW}╚════════════════════════════════════════╝{RESET}")
    print()  # 空行

def wallet_search(process_id, stop_event):
    """并行搜索符合条件的钱包地址。"""
    attempts = 0
    while not stop_event.is_set():
        wallet = generate_wallet()
        attempts += 1
        log_progress(process_id, attempts)
        if matches_address(wallet["public_key"], config["address_start"], config["address_end"]):
            stop_event.set()
            save_wallet_to_file(wallet, config["address_start"])
            return wallet

def main():
    display_header()  # 显示带边框的黄色 Logo
    print(f'开始生成地址: {config["address_start"]}...{config["address_end"]} 使用 {config["num_processes"]} 核心')
    input('按 Enter 键开始...')
    start_time = time.time()
    with multiprocessing.Manager() as manager:
        stop_event = manager.Event()
        with concurrent.futures.ProcessPoolExecutor(max_workers=config["num_processes"]) as executor:
            futures = [executor.submit(wallet_search, i + 1, stop_event) for i in range(config["num_processes"])]
            for future in concurrent.futures.as_completed(futures):
                wallet = future.result()
                if wallet:
                    print("找到符合条件的钱包！")
                    print(f"地址: {wallet['public_key']}")
                    print(f"私钥: {wallet['secret_key']}")
                    print(f"总用时: {time.time() - start_time:.2f} 秒")
                    break

if __name__ == "__main__":
    main()
