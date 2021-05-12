# 67. コマンドライン引数
## optionとして引数を渡せる話
## python lesson.py option1 option2

# import sys
# print(sys.argv)

# 68. Import文とAS

# import lesson_package.utils
from lesson_package.tools import utils

# from lesson_package.utils import say_twice # 余り使わない

# r = lesson_package.utils.say_twice('hello')
r = utils.say_twice('hello')
# r = say_twice('hello') # 余り使わない
print(r)

# 69. 絶対パスと相対パスのImport
from lesson_package.talk import human

print(human.sing())

# 70. アスタリスクのインホートと__init__.pyと__all__の意味
## import *のときは__init__.pyに__all__とファイル名を書く
# from lesson_package.talk import * #余り使わない

# 71. ImportErrorの使い所
# ライブラリとして提供するときにversion違いで階層が違うときとかに使う
# try:
#     from lesson_package import utils
# except ImportError:
#     from lesson_package.tools import utils

# 72. setup.pyでパッケージ化して配布する
## pycharm -> tools -> create setup.py
## pycharm -> tools -> run setup.py -> sdist

## commandだとpython setup.py sdist

# 73. 組み込み関数
## https://docs.python.org/ja/3/library/functions.html
ranking = {
    'A': 100,
    'B': 85,
    'C': 95
}
print(sorted(ranking, key=ranking.get, reverse=True))

# 74. 標準ライブラリ
## https://docs.python.org/ja/3/library/index.html

s = 'aaaasyukhlrjfiwertj4'

from collections import defaultdict

d = defaultdict(int)

for c in s:
    d[c] += 1
print(d)

# 75. サードパーティーのライブラリ
## https://pypi.org/
## pip install termcolorとコマンドは一緒
from termcolor import colored

print(colored('test', 'red'))
print(help(colored))

# 76. importする際の記述の仕方
## 最初はpythonのパッケージ(アルファベット順), 次は1行空けてサードパーティ, 次は1行空けて自分たちのパッケージ, 最後はローカルのファイル
import collections
import sys

import termcolor

import lesson_package

import config

print(collections.__file__)
print(termcolor.__file__)
print(lesson_package.__file__)
print(config.__file__)

print(sys.path)

# 77. __name__と__main__
## importすると上からすべての処理をしてしまう(printとか)
## なので、if __name__ == '__main__':と書き、mainだけを呼ぶようにしている
print('config', __name__)


def main():
    print('main')


if __name__ == '__main__':
    main()
