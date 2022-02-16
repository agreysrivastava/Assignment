from array import array


def take_array(n):
    arr = []
    for i in range(0,n):
        row = []
        for j in range(0,n):
            row.append(int(input()))
        arr.append(row)
    return arr

#Input array
size = int(input("Enter Size: "))
dominant_diagonal_array = take_array(size)

#Find Dominant element of each row
dominant_columns = []
for i in range(size):
    drow = dominant_diagonal_array[i]
    max = drow[0]
    ind = 0
    for j in range(size):
        if drow[j] > max:
            max = drow[j]
            ind = j
    rowsum = 0
    for j in range(size):
        if j != ind:
            rowsum += drow[j]
    if rowsum <= max:
        dominant_columns.append(ind)
    else:
        print("Neither a Dominant diagonal matrix nor can be made through Row Transformations!!")
        break
if len(dominant_columns) == size:
    dominant_columns_set = set(dominant_columns)
    if dominant_columns == list(range(0,size)):
        print("The matrix is a diagonally dominant matrix")
    elif len(dominant_columns) == len(dominant_columns_set):
        print("The matrix can be made a Diagonally Dominant Matrix by row Transformations")
    else:
        print("Neither a Dominant diagonal matrix nor can be made through Row Transformations!!")

