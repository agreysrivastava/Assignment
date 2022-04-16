
from my_library import*

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
