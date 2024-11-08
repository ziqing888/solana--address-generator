from solana.keypair import Keypair
from base58 import b58encode
from config import config

def generate_wallet():
    """生成钱包，返回公钥和私钥。"""
    keypair = Keypair.generate()
    public_key = str(keypair.public_key)
    secret_key_base58 = b58encode(keypair.secret_key).decode('utf-8')
    return {"public_key": public_key, "secret_key": secret_key_base58}

def matches_address(address: str, start: str, end: str) -> bool:
    """检查地址是否符合指定的开始和结束条件。"""
    return (start == "" or address.startswith(start)) and (end == "" or address.endswith(end))
