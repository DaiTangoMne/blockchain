import hashlib


def to_hash(text) -> str:
    return hashlib.sha256(text.encode()).hexdigest()


if __name__ == '__main__':
    str = 'tx1'
    st2 = 'tx2'
    str = to_hash(str)
    st2 = to_hash(st2)
    to_hash(str + st2)