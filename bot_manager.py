import random

from rahavard_crawler import TweetCrawler
from text_processor import SelfNormalizer, Analyzer



class Manager:
    def __init__(self):
        self.crawler = TweetCrawler()
        self.self_normalizer = SelfNormalizer()
        self.analyzer = Analyzer()

    def _select_symbol_of_bourse(self, content: str):
        symbols = {'وتجارت', 'وپارس', 'فملی', 'وبصادر', 'کترام', 'فاذر', 'شراز', 'چکاپا', 'آپ', 'لابسا', 'کاما',
                   'پکویر', 'ثبهساز', 'کلر', 'پترول',
                   'ورنا', 'لکما', 'بترانس', 'کسرا', 'خفنر', 'ذوب', 'خدیزل', 'شستا', 'شاراک', 'فولاد', 'شپترو',
                   'وشهر',
                   'قاسم', 'پالایش', 'خساپا', 'پاسا', 'فسبزوار', 'وبرق', 'غزر', 'سفار', 'نوری', 'زگلدشت', 'ولساپا',
                   'وغدیر', 'سپید', 'وآیند', 'بکاب', 'وسالت', 'کیسون', 'تپکو', 'بجهرم', 'فروی', 'ختراک', 'همراه',
                   'غبشهر',
                   'غنوش', 'کیمیاتک', 'فلوله', 'تفارس-پذیره', 'آرام', 'خفولا', 'بالاس', 'غدشت', 'ثشاهد',
                   'کتوکا', 'کفپارس', 'زماهان', 'شفن', 'دی', 'خپارس', 'غصینو', 'مادیرا', 'زاگرس', 'قچار', 'کرمان',
                   'شکلر', 'شپلی', 'خکرمان', 'کدما', 'طلا', 'خنصیر', 'وهامونح', 'شلرد', 'برکت', 'کمند', 'وسین',
                   'سجام',
                   'مفاخر', 'شوینده', 'خکار', 'شیشه01ن', 'افق', 'شپدیس', 'خاور', 'تمحرکه', 'کالا', 'صبا', 'سیمرغ',
                   'سمگا',
                   'زگلدشتح', 'خکمک', 'فزرین', 'فنفت', 'رتاپ', 'دارا یکم', 'خگستر', 'وآذر', 'ساذری', 'خودکفا',
                   'غالبر',
                   'بزاگرس', 'غشهداب', 'وساپا', 'قنیشا', 'کگاز', 'فولای', 'وپست', 'خودرو', 'شگویا', 'خلنت', 'ثاخت',
                   'شپنا', 'شتران', 'غگرجی', 'وبملت', 'سیتا', 'گشان', 'وگردش', 'وسدید'}

        symbol_of_content = []
        for symbol in symbols:
            if symbol == 'دی':
                if content.startswith('دی ') or content.endswith(' دی') or ' دی ' in content:
                    symbol_of_content.append(symbol)
                else:
                    continue
            if symbol in content:
                symbol_of_content.append(symbol)
        return symbol_of_content

    def crawler_manager(self):
        before_id = 999999999
        while True:
            # crawled_data = self.crawler.crawl_tweets(before_id)
            # before_id = crawled_data['data']['posts'][-1]['id']

            text = self.self_normalizer.normalize(raw_text)

            text_info = self.analyzer.info_of_text(raw_text)
            result = self._select_symbol_of_bourse(text)
            print(f'raw content : {raw_text}\n'
                  f'content information: {text_info}\n'
                  f'normal content: {text}\n')
            if len(result) != 0:
                symbols_str = ''
                for symbol in set(result):
                    symbols_str += f"{symbol},"
                print(f'this text relate to {symbols_str} symbol')
            else:
                print('this text relate to nothing symbol')

            decide = input('Do you want to continue? (please enter yes/no)')
            if decide == 'yes':
                continue
            elif decide == 'no':
                break
