import hashlib
import itertools
import string

def build_charset(charset_options):
    charset = ""
    if "0-9" in charset_options:
        charset += string.digits  # 添加数字
    if "a-z" in charset_options:
        charset += string.ascii_lowercase  # 添加小写字母
    if "A-Z" in charset_options:
        charset += string.ascii_uppercase  # 添加大写字母
    if "symbols" in charset_options:
        charset += string.punctuation  # 添加常用符号
    return charset

def hash_cracker(hash_type, target_hash, max_length, charset):
    for length in range(1, max_length + 1):
        for guess in itertools.product(charset, repeat=length):
            guess_str = ''.join(guess)
            # 计算哈希值
            if hash_type == 'md5':
                hashed_guess = hashlib.md5(guess_str.encode()).hexdigest()
            elif hash_type == 'sha1':
                hashed_guess = hashlib.sha1(guess_str.encode()).hexdigest()
            elif hash_type == 'sha256':
                hashed_guess = hashlib.sha256(guess_str.encode()).hexdigest()
            else:
                raise ValueError("不支持的哈希类型")
            
            # 比较计算出的哈希值与目标哈希值
            if hashed_guess == target_hash:
                return guess_str
            
    return None

def hashCrack(type, length, charset, hash):
    # 构建字符集
    charset = build_charset(charset)

    if not charset:
        raise ValueError("未选择任何字符集")

    # 开始破解
    result = hash_cracker(type, hash, length, charset)
    
    if result:
        return result
    else:
        return "未能找到匹配的原始字符串。"
