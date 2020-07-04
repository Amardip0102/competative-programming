def riverSizes(matrix):
    riversizes = []
    visited = [[False for _ in row] for row in matrix]

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if visited[row][col]:
                continue
            traverseRiver(row,col,matrix,visited,riversizes)

    return riversizes

def traverseRiver(row,col,matrix,visited,sizes):
    stack = [[row,col]]
    count = 0
    while len(stack):
        i, j = stack.pop()
        if visited[i][j]:
            continue
        visited[i][j] = True
        if matrix[i][j] == 0:
            continue
        count += 1
        if i > 0 and not visited[i - 1][j]:
            stack.append([i - 1, j])
        if i < len(matrix) - 1 and not visited[i + 1][j]:
            stack.append([i + 1, j])
        if j > 0 and not visited[i][j - 1]:
            stack.append([i, j - 1])
        if j < len(matrix[0]) - 1 and not visited[i][j + 1]:
            stack.append([i, j + 1])

    if count > 0:
        sizes.append(count)


