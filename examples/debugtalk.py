import hashlib
import hmac
import random
import string

SECRET_KEY = "DebugTalk"
DFIRE_KEY = "BoivJgAlmBUO05yoxD6RU/SZ/nhLvpXT40v2ceqKJ1s="

def gen_random_string(str_len):
    random_char_list = []
    for _ in range(str_len):
        random_char = random.choice(string.ascii_letters + string.digits)
        random_char_list.append(random_char)

    random_string = ''.join(random_char_list)
    return random_string

def get_sign(*args):
    content = ''.join(args).encode('ascii')
    sign_key = SECRET_KEY.encode('ascii')
    sign = hmac.new(sign_key, content, hashlib.sha1).hexdigest()
    return sign

def get_2dfire_sign(**kwargs):
    keys = list(kwargs.keys())
    print(keys)
    keys.sort()

    query = []

    for key in keys:
        if key not in ("sign", "method", 'appKey', "v", "format", "timestamp"):
            value = kwargs.get(key)
            if value:
                query.append(key)
                query.append(value)

    return md5encode("".join(query) + DFIRE_KEY)


def md5encode(origin):
    m2 = hashlib.md5()
    m2.update(origin.encode("utf8"))
    print("签名：" + m2.hexdigest())
    return m2.hexdigest()


