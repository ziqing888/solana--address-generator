from datetime import datetime

def log_progress(process_id, attempts, config):
    """记录进度日志，每隔指定次数输出一次。"""
    if config["show_log"] and attempts % config["log_count"] == 0:
        print(f"进程 {process_id}: 尝试生成 {attempts} 次")

def save_wallet_to_file(wallet, address_start):
    """将钱包信息保存到文件。"""
    filename = f"{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}_{address_start}.txt"
    with open(filename, "w", encoding='utf-8') as f:
        f.write(f"地址: {wallet['public_key']}\n")
        f.write(f"私钥 (Base58): {wallet['secret_key']}\n")
    print(f"信息已保存到文件: {filename}")
