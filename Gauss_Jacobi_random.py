import random
def take_array(n,m):
    arr = []
    for i in range(0,n):
        row = []
        for j in range(0,m):
            row.append(random.randint(1,100))
        arr.append(row)
    return arr

def print_array(arr):
    for i in range(len(arr)):
        print(arr[i])

#Input array
size = 4
dominant_diagonal_array = take_array(size,size)
value_array = take_array(size,1)

#Iteration Matrix
from copy import deepcopy
def calculate_iteration(n,dominant_diagonal_array,value_array):
    iteration_matrix = []
    updt_row = [0]*size
    calc_row = [0]*size
    rowno = 0
    while rowno < n:
        iteration_matrix.append([0]*size)
        for i in range(size):
            sum = 0
            for j in range(size):
                if i != j:
                    sum += dominant_diagonal_array[i][j]*calc_row[j]
            updt_row[i] = (value_array[i][0] - sum)/dominant_diagonal_array[i][i]
        iteration_matrix[rowno] = deepcopy(updt_row)
        calc_row = deepcopy(updt_row)
        #for x in range(size):
        #    if rowno == 0 or (init_row[x] - iteration_matrix[rowno-1][x]) > 0.001:
        #        break
        rowno += 1
    return iteration_matrix

result_iteration = calculate_iteration(10,dominant_diagonal_array,value_array)

print("Input Array")
print_array(dominant_diagonal_array)

print("Value Array")
print_array(value_array)

print("Iteration Matrix")
print_array(result_iteration)