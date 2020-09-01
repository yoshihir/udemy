# 91. ファイルの作成
# 92. withステートメントでファイルをopenする
with open('test.txt', 'w') as f:
    f.write('Test\n')
print('My', 'name', 'is', 'Mike', sep='#', end='!', file=f)

# 93. ファイルの読み込み
# 94. seekを使って移動する
s = """\
AAA
BBB
CCC
DDD
"""

# with open('test.txt', 'w') as f:
#     f.write(s)

with open('test.txt', 'r') as f:
    while True:
        # 2個ずつ読み込む(パケット読み込みとか決まっているバイト数のときに使う)
        chunk = 2
        line = f.read(chunk)
        print(line)
        if not line:
            break

        ## f.seek(5)で読み込む位置を進めさせられる。でも使わないかも


# 95. 書き込み読み込みモード
## w+やr+で書き込みができ、さらに読み込みができるモードになる。書き込みの場合、seekで初期位置に移動してからreadしないと見れない。使うか?
# with open('test.txt', 'w+') as f:
#     f.write(s)
#     f.seek(0)
#     print(f.read())

