import random
def take_array(m,n):
    arr = []
    for i in range(0,m):
        row = []
        for j in range(0,n):
            row.append(int(input()))
        arr.append(row)
    return arr

def print_array(arr):
    for i in range(len(arr)):
        print(arr[i])

def random_array(m,n):
    arr = []
    for i in range(0,m):
        row = []
        for j in range(0,n):
            row.append(random.randint(100,10000)/1000)
        arr.append(row)
    return arr


def swap( Matrix, row1, row2, col):
        for i in range(col):
            temp = Matrix[row1][i]
            Matrix[row1][i] = Matrix[row2][i]
            Matrix[row2][i] = temp

def rankOfMatrix(Matrix,R,C):
        rank = C
        for row in range(0, rank, 1):
            if Matrix[row][row] != 0:
                for col in range(0, R, 1):
                    if col != row:
                        multiplier = (Matrix[col][row] /
                                      Matrix[row][row])
                        for i in range(rank):
                            Matrix[col][i] -= (multiplier *
                                               Matrix[row][i])
            else:
                reduce = True
                 
                # Find the non-zero element
                # in current column
                for i in range(row + 1, R, 1):
                    if Matrix[i][row] != 0:
                        swap(Matrix, row, i, rank)
                        reduce = False
                        break
                if reduce:
                     
                    rank -= 1
                     
                    # copy the last column here
                    for i in range(0, R, 1):
                        Matrix[i][row] = Matrix[i][rank]
                         
                # process this row again
                row -= 1
        return (rank)

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

#transpose
def transpose(mat,row,col):
    transpose_arr = []
    for i in range(col):
        temp = []
        for j in range(row):
            temp.append(mat[j][i])
        transpose_arr.append(temp)
    return transpose_arr

#Q Matrix clculation
def calculateQ(mat,row,col):
    mat = transpose(mat,row,col)
    q_mat = []
    q_mat.append(mat[0])
    for i in range(1,col):
        temp_arr = [0]*row
        for j in range(i):
            k = vector_multplication(mat[i],q_mat[j])/vector_multplication(q_mat[j],q_mat[j])
            k_vector = scalar_multiplication(k, q_mat[j])
            temp_arr = add_vectors(temp_arr,k_vector)
        mod_mat = vector_multplication(subtract_vectors(mat[i],temp_arr),subtract_vectors(mat[i],temp_arr))
        q_mat.append(scalar_multiplication(subtract_vectors(mat[i],temp_arr),1/mod_mat))
    return transpose(q_mat,col,row)

#Matrix Multiplication
def matrix_multiplication(A,B):
    # iterating by row of A
    result = []
    for i in range(len(A)):
        temp_arr = []
        for j in range(len(B[0])):
            temp = 0
            for k in range(len(B)):
                temp += A[i][k] * B[k][j]
            temp_arr.append(temp)
        result.append(temp_arr)
    return result

#Matrix Subtraction
def matrix_subtraction(A,B):
    result = []
    for i in range(len(A)):
        temp_arr = []
        for j in range(len(B[0])):
            temp_arr.append(A[i][j] - B[i][j])
        result.append(temp_arr)
    return result