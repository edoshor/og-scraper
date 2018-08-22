import datetime
import re

import requests
from bs4 import BeautifulSoup

value_types = {
    'image:width': int,
    'image:height': int,
    'video:width': int,
    'video:height': int,
    'video:duration': int,
    'video:release_date': datetime.datetime.fromisoformat,
    'music:duration': int,
    'music:album:disc': int,
    'music:album:track': int,
    'music:song:disc': int,
    'music:song:track': int,
    'music:release_date': datetime.datetime.fromisoformat,
    'article:published_time': datetime.datetime.fromisoformat,
    'article:modified_time': datetime.datetime.fromisoformat,
    'article:expiration_time': datetime.datetime.fromisoformat,
    'book:release_date': datetime.datetime.fromisoformat,
}


class Page:
    def __init__(self, url) -> None:
        super().__init__()
        self.id = None
        self.url = url
        self.scrape_status = 'pending'
        self.updated_time = None
        self.error = None
        self.og_data = {}

    def to_json(self):
        return {
            **{
                'id': self.id,
                'url': self.url,
                'scrape_status': self.scrape_status,
                'updated_time': self.updated_time.isoformat(timespec='seconds') if self.updated_time else None,
            }, **self.og_data}

    # TODO: support Array of values (http://ogp.me/#array)
    def scrape(self):
        print('scraping {} [{}]'.format(self.url, self.id))

        try:
            resp = requests.get(self.url,
                                timeout=5,
                                headers={'User-Agent': 'edo.shor@keywee.com awesome open graph scraper'})
            resp.raise_for_status()
        except Exception as ex:
            self.scrape_status = 'error'
            print("Request error: ", ex)
        else:
            doc = BeautifulSoup(resp.text, 'html.parser')
            ogs = doc.html.head.findAll(property=re.compile(r'^og:'))

            self.og_data = {}
            for og in ogs:
                value = og['content']
                if not value:
                    continue

                key = og['property'][3:]

                # cast value to appropriate type
                try:
                    typed_value = value_types.get(key, str)(value)
                except Exception as ex:
                    print('Type case error: ', ex)
                    continue

                # group fields into nested dicts (e.g image, video, etc...)
                if key in ['image', 'video', 'audio']:
                    key += ':url'
                key_parts = key.split(':')

                if len(key_parts) == 1:  # simple case
                    self.og_data[key] = typed_value
                else:
                    # make room for all key parts but the last one
                    x = self.og_data
                    for key_part in key_parts[:-1]:
                        if key_part not in x:
                            x[key_part] = {}
                        x = x[key_part]

                    # put value in last key_part
                    x[key_parts[-1]] = typed_value

            self.scrape_status = 'done'
            self.updated_time = datetime.datetime.utcnow()

