#Practice: python DFS of an NxN matrix

least_sum = []

visited = []


def DFS(arr, total, i, j):

    flag = 0

    total += arr[i][j]

    visited.append((i,j))

    if(i == len(arr) - 1):
        least_sum.append(total)
        return

    if(i+1 >= 0 and j >= 0): #down
        for k in visited:
            if ((i+1,j) == visited):
                flag = 1
        if (flag == 0):
            DFS(arr, total, i+1, j)

    if(i+1 >= 0 and len(arr) > j+1 >= 0): #down and right
        for k in visited:
            if ((i+1,j+1) == visited):
                flag = 1
        if (flag == 0):
            DFS(arr, total, i+1, j+1)

    if (i+1 >= 0 and j-1 >= 0):
        for k in visited:
            if ((i+1,j-1) == visited):
                flag = 1
        if (flag == 0):
            DFS(arr, total, i+1, j-1) #down and left



arr = [[9,9,9],[9,9,9],[9,9,1]]
DFS(arr,0,0,0)
DFS(arr,0,0,1)
DFS(arr,0,0,2)
print min(least_sum)



