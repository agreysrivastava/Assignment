def take_array(n,m):
    arr = []
    for i in range(0,n):
        row = []
        for j in range(0,m):
            row.append(int(input()))
        arr.append(row)
    return arr

#Input array
size = int(input("Enter Size: "))
dominant_diagonal_array = take_array(size,size)
value_array = take_array(size,1)

#Iteration Matrix
from copy import deepcopy
iteration_matrix = []
init_row = [0]*size
rowno = 0
no_exit = True
while no_exit:
    iteration_matrix.append([0]*size)
    no_exit = False
    for i in range(size):
        sum = 0
        for j in range(size):
            if i != j:
                sum += dominant_diagonal_array[i][j]*init_row[j]
        init_row[i] = (value_array[i][0] - sum)/dominant_diagonal_array[i][i]
    iteration_matrix[rowno] = deepcopy(init_row)
    for x in range(size):
        if rowno == 0 or (init_row[x] - iteration_matrix[rowno-1][x]) > 0.001:
            no_exit = True
            break
    rowno += 1

print(iteration_matrix)