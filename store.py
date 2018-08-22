import hashlib
import threading

from models import Page


class MemoryStore:

    def __init__(self) -> None:
        super().__init__()
        self.store = {}

    def get_page(self, page_id):
        return self.store.get(page_id)

    def create_page(self, url):
        page = Page(url)
        page.id = MemoryStore.url_to_id(url)

        if page.id in self.store:
            return None

        self.store[page.id] = page

        thread = threading.Thread(target=page.scrape)
        thread.daemon = True
        thread.start()

        return page

    @staticmethod
    def url_to_id(url):
        return int(hashlib.md5(url.encode('utf-8')).hexdigest(), 16)


# TODO: implement persistent store for Page model
class PostgresStore:
    pass
