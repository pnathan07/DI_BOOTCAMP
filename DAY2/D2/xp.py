ages = (33, 45, 12)

total = 0
for age in ages:
    if age > 18:
        total += 15
    elif 8<age<18:
        total += 10
        
print(total)