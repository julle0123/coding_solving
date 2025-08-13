start = int(input())
before = int(input())
after = int(input())

money = start
month = 1
while money < 70:
    money += before
    money +=1
while money < 100:
    money += after
    month += 1
print(month)