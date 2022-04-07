class Formatter:
    def __init__(self):
        pass

    def normalizer(self, text: str):
        pass


class Analyzer:
    def __init__(self):
        #todo: اضافه کردن نیم فاصله
        self.namad = {",", ".", "،", "?", "؟", "!", "!", "#", "*", "(", ")", "[", "]", "{", "}", " "}

    def __word_count(self, text: str):
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
        return len(words)


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
        return {'word_count': self.__word_count(text),
                'number_count': self.__number_count(text),
                'letter_count': self.__Letter_info(text)}


if __name__ == '__main__':
    print(Analyzer().info_of_text(
        "#چکاپا آقا بفروشید بخدا راجب این سهم حتی فکر هم نکنید بنده از زمانی که اومد تو بورس با قیمت 150 دائم خرید فروش میکردم این آخری که نزدیک 3 سالو خوردی پولم بود بجز اون رشد فضایی بازار اخر 98 که همه سهم ها رشد داشتن هیچ اتفاق قابل توجهی دیگه ای تو این نیافتاده البته با توجه به تورم میگم کلا پولتون اینجا بی ارزش میشه گفتم بدونید این سهم آش غ ا ل رو تحریم کنید")
    )