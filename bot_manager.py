from rahavard_crawler import TweetCrawler
from text_processor import Normalizer, Analyzer

class Manager:
    def __init__(self):
        self.crawler = TweetCrawler()
        self.normalizer = Normalizer()
        self.analyzer = Analyzer()

    def _select_symbol_of_bourse(self, content: str):
        pass

    def crawler_manager(self):
        before_id = 999999999
        crawled_data = self.crawler.crawl_tweets(before_id)
        raw_tweet = crawled_data['data'].get('posts')
        tweet_info = self.analyzer.info_of_text(raw_tweet)

        tweet = self.normalizer.normalize(raw_tweet)
        result = self._select_symbol_of_bourse(tweet)
        print(f'raw content : {raw_tweet}\n'
              f'content information: {tweet_info}\n'
              f'normal content: {tweet}\n'
              f'symbols in content: {result}')


if __name__ == '__main__':
    Manager().crawler_manager()