

#Input Matrix
from random import random

from my_library import *
from copy import deepcopy

m = 7
n = 5
rnd_arr = random_array(m,n)
print_array(rnd_arr)

#rank 
rank = rankOfMatrix(deepcopy(rnd_arr),m,n)
if rank < n:
    print("Re- Enter Matrix, Grm Schmidt cannot be applied on this one")
    rnd_arr = random_array(m,n)

#Q mat
q_matrix = calculateQ(rnd_arr,m,n)
q_transpose = transpose(q_matrix,m,n)
print_array(q_transpose)
r_matrix = matrix_multiplication(q_transpose,rnd_arr)

print("\nQ Matrix: ")
print_array(q_matrix)

print("\nR Matrix: ")
print_array(r_matrix)

a_qr = matrix_subtraction(rnd_arr,matrix_multiplication(q_matrix,r_matrix))

#Frobenius Norm

from math import sqrt

def CalculateFrobenius(random_array,m,n):
	sum= 0
	for i in range(m):
		for j in range(n):
			sum += pow(random_array[i][j], 2)
	result = sqrt(sum)
	return round(result, 5)

print("\nFrobenius Norm")
print(CalculateFrobenius(rnd_arr,m,n))