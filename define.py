number_of_book = 100

name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']

def create_user(name,age,address):
    data = {}
    data['name'] = name
    data['age'] = age
    data['address'] = address
    print(f'{name}님 환영합니다!')
    return data

def decrease_book(book):
    global number_of_book
    number_of_book -= book['age']//10
    print(f'남은 책의 수 : {number_of_book}')

def rental_book(info):
    decrease_book(info)
    print(f'{info["name"]}님이 {info["age"]//10}권을  대여하였습니다.')

many_user = list(map(create_user,name, age, address))

infos = list(map(lambda x: {'name': x['name'], 'age': x['age']}, many_user))
list(map(rental_book, infos))





