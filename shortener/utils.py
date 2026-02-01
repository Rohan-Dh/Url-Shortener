ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

def base62_encode(num: int) -> str:
    if num == 0:
        return ALPHABET[0]
    base = len(ALPHABET)
    out = []
    while num > 0:
        num, rem = divmod(num, base)
        out.append(ALPHABET[rem])
    return "".join(reversed(out))
