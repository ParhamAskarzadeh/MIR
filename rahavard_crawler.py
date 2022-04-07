from requests import ReadTimeout, TooManyRedirects, Timeout
from requests.exceptions import ChunkedEncodingError, ConnectionError
import json
import time
import requests


class TweetCrawler:

    def crawl_tweets(self, before_id):
        url = f'https://rahavard365.com/api/moreposts?before_id={before_id}&has_chart=no'
        while True:
            try:
                response = requests.get(url, timeout=25)
                if response.status_code == 429:
                    time.sleep(1)
                    continue
            except (Timeout, ReadTimeout, ConnectionError, TooManyRedirects, ChunkedEncodingError) as e:
                time.sleep(30)
                continue
            except Exception as e:
                print(type(e))
                raise e
            result = json.loads(response.text)
            return result
