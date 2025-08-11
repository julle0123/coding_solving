a = int(input())
b = int(input())

one = b%10
two = (b//10)%10
three = b//100

print(a*one)
print(a*two)
print(a*three)
print(a*b)