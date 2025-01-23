numbers = [1, 4, 5, 2, 6, 3, 6, 2]

def my_len(numbers):
    cnt = 0
    for number in numbers:
        # print(number)
        cnt += 1
    return cnt

# print(my_len(numbers))
# print(my_len([2, 3, 4]))
# print(my_len([]))
# print(my_len([1, 1, 1]))

def my_sum(numbers):
    total = 0
    for d in numbers:        
        total += d
        # print(d, total)
    return total

# print(my_sum(numbers))
# print(my_sum([]))
# print(my_sum([1, 1, 1]))
# print(my_sum([-1, -1, 3, 0]))

def my_max1(numbers):
    cur_max = 0 # 입력되는 값 중 제일 작은 값
    for d in numbers:
        # print(d)
        if cur_max < d:
            cur_max = d
        # print(d, cur_max)
    return cur_max

# print(my_max(numbers))
# print(my_max([]))
# print(my_max([10, 2, 3]))
# print(my_max([2, 3, 10]))
# print(my_max([0, 0,0, 0]))

def my_min(numbers):
    cur_min = 100
    for d in numbers:
        # print(d)
        if cur_min > d:
            cur_min = d
        # print(d, cur_min)
    return cur_min

# print(my_min(numbers))
# print(my_min([0, 0, 0]))
# print(my_min([1, 2, 5, 6]))
# print(my_min([1, 2, 5, 6, 1]))


def my_max2(numbers):
    cur_max = 0 # 입력되는 값 중 제일 작은 값
    cur_idx = -1
    for idx in range(my_len(numbers)):
        if cur_max < numbers[idx]:
            cur_max = numbers[idx]
            cur_idx = idx
        print(idx, numbers[idx])
    return cur_max, cur_idx

def my_max(numbers):
    cur_idx = 0
    for idx in range(my_len(numbers)):
        if numbers[cur_idx] < numbers[idx]:
            # cur_max = numbers[idx]
            cur_idx = idx
        print(idx, numbers[idx])
    return numbers[cur_idx], cur_idx    

print(my_max(numbers))
