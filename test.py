f=[1,[0,1,2],3]
e = f
f[1][0] = 9
# print(id(f), id(e))
# print(f is e)
print(f, e)

h=f[::]
f[1][0] = 9
# print(id(f), id(h))
# print(f is h)
print(f, h)

import copy
g = copy.deepcopy(f)
f[1][0] = 9
# print(id(f), id(g))
# print(f is g)
print(f, g)

l = f[::]
f[1] = 9
# print(id(f), id(l))
# print(f is l)   
print(f, l)

# 논리연산자는 참 거짓을 저장하는게 아니라 데이터값을 저장한다

a = [1,2,3]
print(not a)