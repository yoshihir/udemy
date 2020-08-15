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


