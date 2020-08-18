# 78. クラスの定義
# 79. クラスの初期化とクラス変数
# 80. コンストラクタとデストラクタ
class Person(object):
    # コンストラクタ
    def __init__(self, name):
        self.name = name
        print('First')

    def say_something(self):
        print('I am {}. hello'.format(self.name))
        self.run(10)

    def run(self, num):
        print('run' * 10)

    # デストラクタ
    def __del__(self):
        print('good bye')

person = Person('Mike')
person.say_something()

del person
print('###################')

# 81. クラスの継承





