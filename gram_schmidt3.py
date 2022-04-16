from my_library import * 
from copy import deepcopy
#transpose
def transpose(mat,row,col):
    transpose_arr = []
    for i in range(col):
        temp = []
        for j in range(row):
            temp.append(mat[j][i])
        transpose_arr.append(temp)
    print_array(transpose_arr)
    return transpose_arr

#Subtract vectors
def subtract_vectors(a,b):
    newarr = [0]*len(a)
    for i in range(len(a)):
        newarr[i] = a[i]- b[i]
    return newarr

#Add Vectors
def add_vectors(a,b):
    newarr = [0]*len(a)
    for i in range(len(a)):
        newarr[i] = a[i]+ b[i]
    return newarr

#Scalar Multiplic
def scalar_multiplication(k,arr):
    newarr = [0]*len(arr)
    for i in range(len(arr)):
        newarr[i] = arr[i]*k
    return newarr

#vector multiplication
def vector_multplication(vecA,vecB):
    sum = 0
    for i in range(len(vecA)):
        sum += vecA[i] * vecB[i]
    return sum


#Q calcultion
def calcQ(mat,row,col):
    mat = transpose(mat,row,col)
    q_mat = []
    q_mat.append(mat[0])
    for i in range(1,col):
        temp_arr = [0]*row
        for j in range(i):
            k = vector_multplication(mat[i],q_mat[j])/vector_multplication(q_mat[j],q_mat[j])
            k_vector = scalar_multiplication(k, q_mat[j])
            temp_arr = add_vectors(temp_arr,k_vector)
        q_mat.append(subtract_vectors(mat[i],temp_arr))
    return q_mat


#Input array
m = int(input("Enter Rows"))
n = int(input("Enter Columns"))

random_array = take_array(m,n)
print_array(random_array)
rank_of_mat = rankOfMatrix(deepcopy(random_array),m,n)

if rank_of_mat < n:
    print("Re- Enter Matrix, Grm Schmidt cannot be applied on this one")
    random_array = take_array(m,n)
result_matrix = calcQ(random_array,m,n)
print_array(result_matrix)


