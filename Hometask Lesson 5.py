
#a = int(input('Enter the value of a: '))
#b = int(input('Enter the value of b: '))
#c = int(input('Enter the value of c: '))
#
#if a > 10 and b > 10 and c > 10 and a % 3 == 0 and b % 3 == 0:
#    print('yes')
#else:
#    print('no')
#exit()



a = int(input('Enter the value of a: '))
b = int(input('Enter the value of b: '))
c = int(input('Enter the value of c: '))
max = int('0')

if a >= b and a >= c:
    max = a
    print(max)
elif b >= a and b >= c:
    max = b
    print(max)
elif c >= a and c >= b:
    max = c
    print(max)
exit()
