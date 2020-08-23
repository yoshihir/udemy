# 91. ファイルの作成
# 92. withステートメントでファイルをopenする
with open('test.txt', 'w') as f:
    f.write('Test\n')
print('My', 'name', 'is', 'Mike', sep='#', end='!', file=f)


