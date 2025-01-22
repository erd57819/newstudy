import random
import requests

# a = 3
# b = print(a)
# print(b)

# print(len('asd'), len([2,3,4,5]))
# print(sorted([3,5,8,4]))

# l = [3,5,4,1]
# print(l.sort())
# print(l)



# select = random.choice(menu)
# print(select)


numbers = range(1,46)

select = random.sample(numbers,6)
select.sort()
print(select)