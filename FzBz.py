

s = open("cnt.txt", "w+")
x = input('give me nmbr 1-100')
x = int(x)
for x in range (1, x+1):

    if x % 3==0 and x % 5==0:
        print('fizbuzz')
    elif  x % 3 == 0:
        print('fizz')
    elif x % 5 == 0:
        print('buzz')
    else:
        print(x)
    s.write(x)
    s.close()