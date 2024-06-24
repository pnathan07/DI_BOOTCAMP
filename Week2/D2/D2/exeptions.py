# print('Hello world')) = Syntax Error

# age = int(input('what\'s your age?'))
# print(age + 10)  #This will crash the program

try:
    age = int(input('what\'s your age?'))
    print(age + 10)
except:
    print('invalid age')
    age = int(input('try again. What is your age?'))
    print(age + 10)

#exercise

my_list = [2,3,1,2,"four",42,1,5,3,"imanumber"]

#without try except:
# total = 0
# for num in my_list:
#     if isinstance(num,int):
#         total += num
#     else:
#         continue

# print(total)
# print(sum(my_list))

total = 0
for num in my_list:
    try:
        total += num
    except:
        continue
    else: #else will happen when the except doesn't happen
        print(num)
    finally: #finally will happen all the iterations. Even if the excepted block happened
        print('happens even if there is no except')

print(total)


