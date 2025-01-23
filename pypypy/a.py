# a = 10
# print(a)


# intA = 10
# strB = '10'

# print(intA, type(intA))
# print(strB, type(strB))


# intA=10
# print(intA, type(intA))

# intA = intA+1
# print(intA, type(intA))

# strB = strB+'a'
# print(strB, type(strB))

# a = [1,2,3]
# a = a + [4]
# print(a, type(a[1]))
# print(len(a))


# #딕셔너리
# dust={'영등포구' : 58, '강남구': 40}
# print(dust)
# 객체 비교는 is => a is b
# import random
# a,b,c,d,e,f,g,h,i = map(int,input().split())
# listA=[a,b,c,d,e,f,g,h,i]

# randomlist = random.choice(listA,)
# if sum(randomlist) == 100:
#        print(randomlist)

matrix = [
        ['0, 1', '0, 2', '0, 3'], 
        ['1, 0', '1, 1', '1, 2', '1, 3'], 
        ['2, 0', '2, 1', '2, 2', '2, 3', '2, 4'], 
        ['3, 0', '3, 1'], 
        ['4, 0', '4, 1', '4, 2'], 
        ['5, 0']
    ]
# 아래애 코드를 작성하시오.
matrix_len = 0

for i in matrix:
    matrix_len += 1 
print(matrix_len)


for number in matrix:
    temporary_len = 0
    for j in number:
        temporary_len +=1
    print(f'{number}리스트는 {temporary_len}개 만큼의 요소를 가지고 있습니다')


for x in range(len(matrix)):
    for y in range(len(matrix[x])):
        print(f'matrix의{x},{y}번째 요소의 값은 {matrix[x][y]}입니다')

