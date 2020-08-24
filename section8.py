# 91. ファイルの作成
# 92. withステートメントでファイルをopenする
with open('test.txt', 'w') as f:
    f.write('Test\n')
print('My', 'name', 'is', 'Mike', sep='#', end='!', file=f)

# 93. ファイルの読み込み
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


