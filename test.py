dict_01 = {}
output_01 = dict_01.setdefault('test', 101)
output_02 = dict_01.get('home', False)
output_03 = dict_01.get('test', False)
print("dict_01 =", dict_01)
print('output_01 =', output_01)
print('output_02 =', output_02)
print('output_03 =', output_03)

if dict_01.get('home', False):
    print('test_01 complited')
else:
    print('test_01 no complited')

if dict_01.get('test', False):
    print('test_02 complited')
else:
    print('test_02 no complited')


print()
print('---')
print('generator')

def generator (n: int):
    for i in range(n):
        yield i

print(tuple(generator(5)))