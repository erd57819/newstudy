# list = [1,2,3,4,5]
# for i in list:
#     print(5)
#     print(50)


# a = int(input())

# for i in range(a):
#     a +=1
#     print(a)

# t= list(range(a))
# print(max(t))

# num = [3,6,7,5,2,4,9]
# cnt = 0
# even = 0
# for num  in num:
#     if num % 2 == 1:
#         cnt = cnt +1
#     else:
#         even = even +1    
# print(f"홀수의 개수는{cnt}개 짝수의 개수는{even}개")      


# a =int(input().split())

# a = list(map(int,input().split()))
# print(a)

# cnt = 0
# cnt2 = 0
# cnt4 = 0
# cnt5 = 0
# for a in a:
#     cnt += 1
#     cnt2 += a
#     cnt3 = cnt2 / cnt
#     if a % 2 == 0:
#         cnt4 += a
#     else:
#         cnt5 += a    
# print(f"짝수의 합은{cnt4} 홀수의 합은{cnt5}")    

# idx = 0
# ant = cnt = -1
# for a in a:
#     if a % 2 == 1:
#         cnt = a 
#         ant = idx
#     idx += 1    
# print(cnt, ant)

i = 0 

# for i  in range(len(a)):
#     if a[i]% 2 == 1:
#         odd_a = a[i]
#         odd_i = i
#     i += 1
# print(odd_a,odd_i)        

n,m =(map(int,input().split()))
rok = 0
for i in range(n):
    s = list(input())
    print(s)
    for c in s :
        if c == 'o':
            rok += 1
print(rok)    