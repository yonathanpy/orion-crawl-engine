from bs4 import BeautifulSoup
from utils.url_tools import normalize, join_url


def extract_links(base, html):

    soup = BeautifulSoup(html, "html.parser")

    links = []

    for tag in soup.find_all("a", href=True):

        link = join_url(base, tag["href"])

        links.append(normalize(link))

    return links
