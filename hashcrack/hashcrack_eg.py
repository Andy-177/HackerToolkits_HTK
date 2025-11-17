from hash_cracker import hashCrack

if __name__ == "__main__":
    try:
        # 示例使用，您可以根据需要修改参数
        result = hashCrack(
            type="sha256",
            length=5,
            charset=("0-9", "a-z"),
            hash="36bbe50ed96841d10443bcb670d6554f0a34b761be67ec9c4a8ad2c0c44ca42c"
        )
        print("破解结果:", result)
    except ValueError as e:
        print("错误:", e)
