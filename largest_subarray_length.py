n=abs(int(input("Enter the number of terms:")))
numbers=[]
for i in range(n):
    val=int(input(f"Enter the {i+1}th number:"))
    numbers.append(val)
print("Here is the list:",numbers)
if n==0:
    max_length=0
    current_length=0
else:
    max_length=1
    current_length=1 # cause atleast 1 number will be the max
for j in range(1,n):
    if numbers[j]>numbers[j-1]:
        current_length+=1
    else:
        current_length=1

    if current_length>max_length:
        max_length = current_length
print("Longest Continuous Increasing Subarray Length is:", max_length)
