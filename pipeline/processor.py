from bs4 import BeautifulSoup


def process_page(url, html):

    soup = BeautifulSoup(html, "html.parser")

    title = ""

    if soup.title:
        title = soup.title.string

    text = soup.get_text()

    return {
        "url": url,
        "title": title,
        "text": text
    }
