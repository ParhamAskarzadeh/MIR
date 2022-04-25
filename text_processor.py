import re


class Analyzer:
    def __init__(self):
        self.namad = {",", ".", "،", "?", "؟", "!", "!", "#", "*", "(", ")", "[", "]", "{", "}", " "}

    def __word_tokenizer(self, text: str):
        word = ''
        words = []
        for letter in text:
            try:
                int(letter)
                if len(word) != 0:
                    words.append(word)
                    word = ''
                continue
            except:
                if letter in self.namad:
                    if len(word) != 0:
                        words.append(word)
                        word = ''
                    continue
                word += letter
        return {'words': words,
                'word_count': len(words)}

    def __mention_count(self, text):
        return list(set(re.findall('@([\w_.]+)', text)))

    def __hashtag_count(self, text):
        return list(set(re.findall('#([\w_]+)', text)))

    def __number_count(self, text: str):
        number = ''
        numbers = []
        for letter in text:
            try:
                int(letter)
            except:
                if len(number) != 0:
                    numbers.append(number)
                    number = ''
                continue
            number += letter
        return len(numbers)

    def __Letter_info(self, text: str):
        letters = []
        namads = []
        for letter in text:
            if letter not in self.namad:
                letters.append(letter)
            elif letter != " ":
                namads.append(letter)
        return {"letter_count": len(letters),
                "namad_count": len(namads)}

    def info_of_text(self, text: str):
        return {'word_count': self.__word_tokenizer(text)['word_count'],
                'number_count': self.__number_count(text),
                'letter_count': self.__Letter_info(text),
                'hashtag_count': len(self.__hashtag_count(text)),
                'mention_count': len(self.__mention_count(text))
                }

    def tokenizer(self, text: str):
        return self.__word_tokenizer(text)['words']


class Normalizer:
    def normalize(self, text: str) -> str:
        text = self.__remove_shapes_and_convert_emojis_to_unicode(text)
        text = self.__character_replacer(text)

        return text.strip()

    def __remove_shapes_and_convert_emojis_to_unicode(self, text):
        shape_list = re.findall(r'[^\w\s,]', text)  # find all shape and emojis
        for shape in shape_list:
            shape_code = shape.encode('unicode-escape').decode('ASCII')
            if 'U000' in shape_code:  # if the shape is an emoji
                text = text.replace(shape, ' {} '.format(shape_code))
            else:
                text = text.replace(shape, ' ')
        return text

    def __character_replacer(self, text: str):
        # Numbers
        text = re.sub(r'[٠⓪⓿０𝟶🄌]', '۰', text)
        text = re.sub(r'[١⓵❶➀➊꘡]', '۱', text)
        text = re.sub(r'[٢②２𝟐]', '۲', text)
        text = re.sub(r'[٣③３𝟛]', '۳', text)
        text = re.sub(r'[٤۴⓸➍𝟒𝟜]', '۴', text)
        text = re.sub(r'[٥⓹❺５𝟝]', '۵', text)
        text = re.sub(r'[٦۶⑥❻６𝟞𝟨]', '۶', text)
        text = re.sub(r'[٧➆➐７𝟟]', '۷', text)
        text = re.sub(r'[٨⑧❽８𝟖]', '۸', text)
        text = re.sub(r'[٩⑨❾𝟗]', '۹', text)

        # Alphabet
        text = re.sub(r'[آأ𞸀]', 'ا', text)
        text = re.sub(r'[بﭒﭓﭔﭕ𞸁]', 'ب', text)
        text = re.sub(r'[ﭗﭘﭙ]', 'پ', text)
        text = re.sub(r'[تﺖﭧ𞸕]', 'ت', text)
        text = re.sub(r'[ثﺙﺚ𞸶𞸖]', 'ث', text)
        text = re.sub(r'[ﺝﺞﺠ𞸢𞸂]', 'ج', text)
        text = re.sub(r'[چﭻﭼﮀ]', 'چ', text)
        text = re.sub(r'[حﺢﺣ𞸇]', 'ح', text)
        text = re.sub(r'[ﺦﺨ𞸗]', 'خ', text)

        text = re.sub(r'[دﺩﺪ]', 'د', text)
        text = re.sub(r'[ذﺫﺬ𞸘]', 'ذ', text)
        text = re.sub(r'[رﺭﺮ𞸓]', 'ر', text)
        text = re.sub(r'[زࢲﺯﺰ𞸆]', 'ز', text)
        text = re.sub(r'[ژﮊﮋ]', 'ژ', text)
        text = re.sub(r'[ﺱﺳﺴ𞸎𞸮]', 'س', text)
        text = re.sub(r'[ﺵﺶﺸ𞸴𞸔]', 'ش', text)
        text = re.sub(r'[ص𞸱𞸑]', 'ص', text)
        text = re.sub(r'[ضﻀ𞸹𞸙]', 'ض', text)
        text = re.sub(r'[ﻂﻃ𞸈]', 'ط', text)
        text = re.sub(r'[ﻆ𞸚]', 'ظ', text)
        text = re.sub(r'[عﻉﻊﻌ𞸯𞸏]', 'ع', text)
        text = re.sub(r'[ﻎﻏﻐ𞸻𞸛]', 'غ', text)
        text = re.sub(r'[ف𞸞𞸐]', 'ف', text)
        text = re.sub(r'[ﻖﻘ𞸟𞸒]', 'ق', text)
        text = re.sub(r'[گﮓﮔﮕ]', 'گ', text)
        text = re.sub(r'[كﮑ𞸊𞸪]', 'ک', text)
        text = re.sub(r'[ﻝﻞﻟ𞸋]', 'ل', text)
        text = re.sub(r'[مﻡﻤ𞸬𞸌]', 'م', text)
        text = re.sub(r'[ﻥ𞸍𞸭]', 'ن', text)
        text = re.sub(r'[ﻭﻮ𞸅ۅﯠ]', 'و', text)
        text = text.replace('وو', 'و')
        text = re.sub(r'[هﮪﻪ𞸤ﻫﻬ]', 'ه', text)
        text = re.sub(r'[ةﺔ]', 'ه', text)
        text = re.sub(r'[ىﻯﻰ𞸉ﯨﯩ]', 'ی', text)
        text = text.replace('ئی', 'یی')
        text = re.sub(r'[ئﺉﺋ]', 'ئ', text)
        text = re.sub(r'[ءﺀ۽]', 'ء', text)
        text = text.replace('﷼', ' ریال ')

        text = text.replace(' می ', ' می\u200c')
        text = text.replace(' نمی ', ' نمی\u200c')
        text = text.replace(' برمی ', ' برمی\u200c')
        text = text.replace(' برنمی ', ' برنمی\u200c')

        # Whitespace
        text = re.sub(r'(\r|\f|\v|\\r|\\n)+', '\n', text)
        text = re.sub(r'\s?\n\s+', '\n', text)
        text = re.sub(r'[\t]+', ' ', text)
        text = re.sub(r' {2,}', ' ', text)

        # semi-space
        text = text.replace('&zwnj;', '\u200c')
        text = re.sub(r'[\u2000-\u200f]+', "\u200c", text)

        return text
