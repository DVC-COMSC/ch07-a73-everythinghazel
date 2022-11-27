

number = [5, 20, 30, 35, 50]

# insval = int(input('Enter the insertion value: '))
# ******************************
# number = list(map(int,input().split()))
insval = int(input())
for i in range(len(number)):
    if insval <= number[i]:
        number.insert(i,insval)
        break
else:
    number.append(insval)
# ******************************

print (number)
