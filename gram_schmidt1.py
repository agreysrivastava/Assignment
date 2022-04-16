import random
def take_array(m,n):
    arr = []
    for i in range(0,m):
        row = []
        for j in range(0,n):
            row.append(random.randint(100,10000)/1000)
        arr.append(row)
    return arr

def print_array(arr):
    for i in range(len(arr)):
        print(arr[i])

#Input array
m = int(input("Enter Rows"))
n = int(input("Enter Columns"))
if m < n:
    m,n = n,m

random_array = take_array(m,n)
print_array(random_array)

#Frobenius Norm

from math import sqrt

def CalculateFrobenius(random_array,m,n):
	sum= 0
	for i in range(m):
		for j in range(n):
			sum += pow(random_array[i][j], 2)


	result = sqrt(sum)
	return round(result, 5)

print("Frobenius Norm")
print(CalculateFrobenius(random_array,m,n))