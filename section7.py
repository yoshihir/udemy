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
# 82. メッソドのオーバーライドとsuperによる親のメソッドの呼び出し
# 83. プロパティーを使った属性の設定
class Car(object):
    def __init__(self, model=None):
        self.model = model

    def run(self):
        print('run')


class ToyotaCar(Car):
    def run(self):
        print('fast')


class TeslaCar(Car):
    def __init__(self, model='Model S',
                 enable_auto_run=False,
                 passwd='123'):
        # 毎回modelを書くのが大変なのでsuper()を書くと親の関数(今回はinit)を呼び出せる
        # self.model = model
        super().__init__(model)
        self._enable_auto_run = enable_auto_run
        self.passwd = passwd

    # propertyと書くと読み込むことはできるがsettingはできない
    @property
    def enable_auto_run(self):
        return self._enable_auto_run

    # propertyを書いたけど、setterもしたいとき
    @enable_auto_run.setter
    def enable_auto_run(self, is_enable):
        if self.passwd == '456':
            # _をつけると外部から読み込めないよという意思表示になる。__二個だとクラス内からしか呼べなくなる
            self._enable_auto_run = is_enable
        else:
            raise ValueError

    def run(self):
        print(self.__)
        print('super fast')

    def auto_run(self):
        print('auto run')


tesla_car = TeslaCar('Model S', passwd='111')
tesla_car.auto_run()


# 84. クラスを構造体として扱う時の注意点
## 下記みたいにclassからobjectを生成した後にパラメータを追加できる
## __を使っても__を指定すれば上書きできてしまうので注意
class T(object):
    pass


t = T()
t.name = 'Mike'
t.age = 20
print(t.name, t.age)

# 85. ダックタイピング
# 86. 抽象クラス
# 87. 多重継承
