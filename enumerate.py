# enumerate -> 리스트의 원소에 순서값을 부여해 주는 함수 -> for문과 함께 자주 사용
a = [1, 2, 3]
for i in enumerate(a):
    print(i)

b = enumerate(a)
print(b, type(b))

for i, j in enumerate(a):
    print('{}번째 값은 {}입니다.'.format(i, j))