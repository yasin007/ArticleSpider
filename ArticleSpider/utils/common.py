"""
create by 维尼的小熊 on 2018/7/16

"""
__autor__ = 'yasin'

import hashlib


def get_md5(url):
    if isinstance(url, str):
        url = url.encode("utf-8")
    m = hashlib.md5()
    m.update(url)
    return m.hexdigest()
