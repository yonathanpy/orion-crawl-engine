import sqlite3


class PageRepository:

    def __init__(self, db="pages.db"):

        self.conn = sqlite3.connect(db)

        self._create()

    def _create(self):

        c = self.conn.cursor()

        c.execute("""
        CREATE TABLE IF NOT EXISTS pages(
            id INTEGER PRIMARY KEY,
            url TEXT,
            title TEXT,
            text TEXT
        )
        """)

        self.conn.commit()

    def save(self, page):

        c = self.conn.cursor()

        c.execute(
            "INSERT INTO pages(url,title,text) VALUES(?,?,?)",
            (page["url"], page["title"], page["text"])
        )

        self.conn.commit()
