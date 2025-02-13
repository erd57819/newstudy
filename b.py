def factorial(n):
    if n == 0:
        return 1  # 기본 종료 조건
    else:
        return n * factorial(n - 1)  # 자기 자신을 호출

result = factorial(5)
print(result)

def f(i,n):
    if i ==n:
        return
    else:
        print(arr[i])
        f(i+1,N)