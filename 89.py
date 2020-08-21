# 89. クラスメソッドとスタティックメソッド
class Person(object):
    kind = 'human'

    def __init__(self):
        self.x = 100

    @classmethod
    def what_is_your_kind(cls):
        return cls.kind

    # あんまり使う機会はないかも
    @staticmethod
    def about(year):
        print('about human {}'.format(year))

# ()をつけるとobjectになる
a = Person()
print(a.x)
# ()がないとまだclassのままなのでxは呼べないがkindは呼べる
# b = Person
# print(b.kind)

# @classmethodを作るとobject生成前にクラスメソッドが呼べる
print(Person.kind)
print(Person.what_is_your_kind())

Person.about(1999)
