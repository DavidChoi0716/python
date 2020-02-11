# lambda 인자리스트: 표현식
# (lambda 인자리스트: 표현식)(인자들)
# map(함수, 리스트)

def sum(x, y):
    return x + y

sum = lambda x, y: x + y
print(sum(10, 20))

print((lambda x, y: x +y)(10, 20))


def power(n):
    return n*n

new_list = map(power,[1,2,3,4,5])
print(list(new_list))

new_list = map(lambda x: x*x, [1,2,3,4,5])
print(list(new_list))


