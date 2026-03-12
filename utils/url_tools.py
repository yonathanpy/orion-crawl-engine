from urllib.parse import urljoin


def join_url(base, path):

    return urljoin(base, path)


def normalize(url):

    return url.strip()
