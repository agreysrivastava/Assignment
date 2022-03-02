import random
def take_array(n,m):
    arr = []
    for i in range(0,n):
        row = []
        for j in range(0,m):
            row.append(random.randint(10000,100000)/10000)
        arr.append(row)
    return arr

additions ,multiplications, divisions  = 0,0,0
pivot_additions ,pivot_multiplications, pivot_divisions = 0,0,0
def find_first_nonzero(array):
    nonzero =-1
    for ind in range(len(array)):
        if array[ind] != 0:
            nonzero = ind
            return nonzero

def subtract_vectors(a,b):
    newarr = [0]*len(a)
    for i in range(len(a)):
        newarr[i] = a[i]- b[i]
    return newarr

def scalar_multiplication(k,arr):
    newarr = [0]*len(arr)
    for i in range(len(arr)):
        newarr[i] = arr[i]*k
    return newarr

def print_array(arr):
    for i in range(len(arr)):
        print(arr[i])

def pivoting(matrix,array):
    max_ind = 0
    for i in range(len(matrix)):
        for j in range(i,len(matrix)):
            if matrix[j][i] > matrix[max_ind][i]:
                max_ind = j
                break
        matrix[i] , matrix[max_ind] = matrix[max_ind],matrix[i]
        array[i], array[max_ind] = array[max_ind], array[i]
    return matrix,array

#Without pivoting
def without_pivot(matrix,array):
    solution_array = [0]*len(array)
    for i in range(len(matrix)):
        if matrix[i][i] ==0 :
            for j in range(i,len(matrix)):
                if matrix[j][i] !=0:
                    matrix[i] , matrix[j] = matrix[j],matrix[i]
                    array[i], array[j] = array[j], array[i]
                    break
    #solving using gauss elimination
    size = len(array)
    for i in range(len(matrix)):
        nonzero = find_first_nonzero(matrix[i])        
        for j in range(i+1,len(matrix)):
            if(matrix[j][nonzero] != 0):
                const = matrix[j][nonzero]/matrix[i][nonzero]
                temp_row = scalar_multiplication(const,matrix[i])
                matrix[j] = subtract_vectors(matrix[j],temp_row)
                array[j] = array[j] - const*array[i]
                divisions += size - nonzero +1
                multiplications += size - nonzero +1
                additions += size - nonzero +1
    
    for i in reversed(range(size)):
        ind = find_first_nonzero(matrix[i])
        if ind != -1:
            sum =0 
            for j in range(ind+1,size):
                sum += matrix[i][j]*solution_array[j]
                additions += 1
                multiplications += 1
            solution_array[i] = (array[i] - sum)/matrix[i][ind]
            divisions += 1
            additions +=1

#With pivoting
def with_pivot(matrix,array):
    solution_array = [0]*len(array)
    matrix, array = pivoting(matrix,array)
    #solving using gauss elimination
    for i in range(len(matrix)):
        nonzero = find_first_nonzero(matrix[i])        
        for j in range(i+1,len(matrix)):
            if(matrix[j][nonzero] != 0):
                const = matrix[j][nonzero]/matrix[i][nonzero]
                temp_row = scalar_multiplication(const,matrix[i])
                matrix[j] = subtract_vectors(matrix[j],temp_row)
                array[j] = array[j] - const*array[i]
                pivot_divisions += size - nonzero +1
                pivot_multiplications += size - nonzero +1
                pivot_additions += size - nonzero +1
    size = len(array)
    for i in reversed(range(size)):
        ind = find_first_nonzero(matrix[i])
        if ind != -1:
            sum =0 
            for j in range(ind+1,size):
                sum += matrix[i][j]*solution_array[j]
                pivot_additions += 1
                pivot_multiplications += 1
            solution_array[i] = (array[i] - sum)/matrix[i][ind]
            pivot_divisions += 1
            pivot_additions +=1

print("Size \t Additions \t Multiplications \t Divisions")
#Input Array
for i in range(10):
    additions ,multiplications, divisions  = 0,0,0
    pivot_additions ,pivot_multiplications, pivot_divisions = 0,0,0
    size = 100*i
    equation_matrix = take_array(size,size)
    value_array = [0]*size
    for i in range(size):
        value_array[i] = float(input())

    from copy import deepcopy
    cloned_matrix = deepcopy(equation_matrix)
    cloned_array = deepcopy(value_array)
    print("============Without Pivoting===================")
    without_pivot(equation_matrix,value_array)
    print(size,"\t",additions,"\t",multiplications,"\t",divisions)
    print("============With Pivoting===================")
    with_pivot(cloned_matrix,cloned_array)
    print(size,"\t",pivot_additions,"\t",pivot_multiplications,"\t",pivot_divisions)
