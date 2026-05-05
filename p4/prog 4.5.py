def calculate_sum(numbers):
    total=0
    for num in numbers:
        total+=num
        return total
    list=[]
n=int(input("Enter the number of elements in the list:"))
for i in range(n):
    num=eval(input("Enter element{}:"))
list.append(num)
result=calculate_sum(list)
print("The sum of the list is:",result)
