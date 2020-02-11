print(range(10))        # range(0, 10)
print(list(range(10)))  # [0, 1, 2, 3, ..., 9]
print(list(range(1, 11)))   # [1, 2, 3, 4, ... 10]
print(list(range(0, 20, 2)))
print(list(range(20, 0, -2)))

for i in range(10, -1, -1):
    print(f'카운트다운:{i}')

add = 0
for i in range(1, 11):
    add = add + i

print(add)

a = range(7)
print(list(a))

a = range(2, 7)
print(list(a))

# for 반복문에서 리스트 range와 함께 사용하기
arr = [1, 2, 3, 4, 5]
for i in range(len(arr)):
    print('{} 번째 값 {}'.format(i, arr[i]))

for i in range(7, -1, -1):
    print(i)

# reversed함수
for i in reversed(range(8)):
    print(i)
    