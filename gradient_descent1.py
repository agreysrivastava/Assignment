import random
from my_library import print_array
def take_array_random(n,m):
    arr = []
    for i in range(0,n):
        row = []
        for j in range(0,m):
            row.append(random.randint(1,100))
        arr.append(row)
    return arr

str = input("Enter lst 4 digits of our phone number: ")
str = str.replace("0","3")
while len(str) != 4:
    print("Exactly 4 digits required")
    str = input("Enter lst 4 digits of our phone number: ")
    str = str.replace("0","3")
m = int(str[0:2])
n = int(str[2:4])
print(m,n)

random_array = take_array_random(m,n)
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