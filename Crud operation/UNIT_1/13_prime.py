n = int(input("Enter a number: "))
flag = 0

if n < 2:
    flag = 1
else:
    for i in range(2, n):
        if n % i == 0:
            flag = 1
            break

if flag == 0:
    print("Prime number")
else:
    print("Not a prime number")
