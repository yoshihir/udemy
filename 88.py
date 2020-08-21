# 88. クラス変数
class Person(object):
    # 今回のテーマはこれ、クラスでの共通変数の話
    # varなのでlistとかを指定すると間違って2回呼んでしまって増えてしまうってバグが起きる
    # その時は__init__に入れて初期化を必ずすること
    kind = 'human'

    def __init__(self, name):
        self.name = name

    def who_are_you(self):
        print(self.name, self.kind)


a = Person('A')
a.who_are_you()
b = Person('B')
b.who_are_you()
