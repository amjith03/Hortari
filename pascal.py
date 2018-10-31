n = str(input())
n = n.split()
numbers = [int(i) for i in n]
print(numbers)
n = len(numbers)
for i in range(0,n):
	for j in range(0,i+1):
		print(numbers[j],end=" ")
	print("\r")


