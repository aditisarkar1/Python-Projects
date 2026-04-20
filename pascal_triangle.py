n=int(input("Enter the no of terms:"))

for i in range(1,n+1):
    #space
    for j in range(1,n-i+1):
        print(" ",end="")
    #star
    c=1
    for k in range(1,i+1):
        print(c,end=" ")
        c=c*(i-j)//j
    print()