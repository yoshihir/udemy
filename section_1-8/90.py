# 90. 特殊メソッド
class Word(object):
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return 'Word!!!!!'

    def __len__(self):
        return len(self.text)

    def __add__(self, word):
        return self.text.lower() + word.text.lower()

    def __eq__(self, word):
        return self.text.lower() == word.text.lower()



w = Word('text')
w2 = Word('###############')
print(len(w))
print(w + w2)
