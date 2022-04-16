
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

#Input array
m = int(input("Enter Rows"))
n = int(input("Enter Columns"))

random_array = take_array(m,n)
print_array(random_array)

rank_of_mat = rankOfMatrix(random_array,m,n)
print("Rank of the Matrix is: ",rank_of_mat)

if rank_of_mat < n:
    print("Gram Schidt Process cannot be applied;")
else:
    print("Gram Schidt Process can be applied;")
