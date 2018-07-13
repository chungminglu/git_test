number = []
for i in range(1,1000,1):
    if i%3 == 0:
        number.append(i)
    elif i % 5 == 0 :
        number.append(i)
    elif i % 15 ==0:
        number.append(i)
dictinct = set(number)
sum = 0
for n in dictinct :
    sum += n
print(sum)