import hashlib


def fingerprint(url):

    h = hashlib.md5()

    h.update(url.encode())

    return h.hexdigest()
