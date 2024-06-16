#Syntax
# def say_hello():
#     print('Hello there!')

# say_hello()


#Arguments
# def say_hello(name):
#     print(f'Hello, {name}')

# # name = "Max"
# say_hello("Max")

#More than 1 argument


def say_hello(username:str, language = 'EN')->None:
    '''prints a greting depending on the username's language'''
    if language == 'EN':
        print(f'Hello, {username}')
    elif language == 'PT':
        print(f'Oi, {username}')
    elif language == 'RU':
        print(f'Privet, {username}')
    elif language == 'FR':
        print(f'Salut, {username}')
    elif language == 'HE':
        print(f'Shalom, {username}')
    else:
        print(f'Sorry, there is no language {language}')

# say_hello('Juliana', 'PT') #positional argument
# say_hello(username = 'Olga', language = 'RU')#Keyword Arguments
# say_hello('Yehonathan', language = 'FR')#both: the first one has to be positional
# say_hello('Adam', 'HE')

#Default values
say_hello('Juliana')


#Usecase for positional + keyword arguments
# def user_info(username = 'none', email = 'gmail', age = 18, password = 123):
#     print('user info:', username, email, age, password)

# user_info('Maria', password = 555)

count = 1

def calculation(a,b):
    # global count
    result = a+b
    # count = 5
    return result

# calculation(5,2)
# print(count)


def sum_total():
    calc1 = calculation(5,3)
    calc2 = calculation(10,4)
    result_add = calc1 + calc2
    result_sub = calc1 - calc2
    return result_add, result_sub
    
print(sum_total())
add, sub = sum_total()
print(add)
print(sub)