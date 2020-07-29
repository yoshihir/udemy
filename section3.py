# 8 変数宣言
num = 1
name = 'Mike'
is_ok = True

print(num, type(num))
print(name, type(name))
print(is_ok, type(is_ok))

num1 = '1'
new_num = int(num1)
print(new_num, type(new_num))

## 型宣言はできるが上書きできてしまう(var)
num2: int = 1

## 変数の先頭に数字は使えない

# 9 まずはprintで出力
print('Hi', 'Mike', sep=',', end='.\n')

# 10 数値
## terminalだとprintと打たなくて良い
## 17 // 3 整数only
## 17 % 3 余り
## 5 ** 2 べき乗

## round関数
pie = 3.141592
print(round(pie, 2))  # 3.14

## math関数
import math

result = math.sqrt(25)
print(result)

y = math.log2(10)
print(y)
## help関数 ライブラリを入れるとhelpが出る
print(help(math))


# 11 文字列
##


