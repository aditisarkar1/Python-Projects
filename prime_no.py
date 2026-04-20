num=int(input("Enter the number to check it's prime or not:"))
if num<=1:
    print(False)
for divisor in range(2, num):
    if num % divisor == 0:
        print(False)#false for not prime
        break
else:
    print(True)#true for prime

    