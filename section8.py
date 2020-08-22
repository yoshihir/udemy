# 91. ファイルの作成
f = open('test.txt', 'w')
f.write('Test\n')
print('My', 'name', 'is', 'Mike', sep='#', end='!', file=f)
f.close()

# 92. withステートメントでファイルをopenする

