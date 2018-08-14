sum = 1
a = 0
b = 0
s = 0
while(sum < 4000000):
    b = sum
    sum += a
    a = b
    # print (sum, end='  ')
    if (sum % 2 == 0):
        s += sum
print (s)
