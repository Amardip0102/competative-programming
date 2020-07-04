def riverSizes(matrix):
    # Write your code here.
	riverLength = []
    visited = [None] * len(matrix) * len(matrix[0])
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if not visited[row][col]:
                visited[row][col] = True
                count = 0
                rw = row
                cl = col
                # forward
                while matrix[rw][cl] == 1:
                    if not visited[row][col]:
                        visited[row][col] = True
                        count +=1
                        if rw !=len(matrix[row]):
                            rw = rw + 1
                # Backward
				while matrix[rw][cl] == 1:
                    if not visited[row][col]:
                        visited[row][col] = True
                        count +=1
                        if rw != 0:
                            rw = rw - 1
                # Upward
				while matrix[rw][cl] == 1:
                    if not visited[row][col]:
                        visited[row][col] = True
                        count +=1
                        if cl !=0:
                            cl = cl - 1
                # Downword
				while matrix[rw][cl] == 1:
                    if not visited[row][col]:
                        visited[row][col] = True
                        count +=1
                    if cl !=len(matrix[row]):
                        cl = cl + 1
            riverLength.append(count)
    return riverSizes


a = riverSizes([[1,0,0,1,0],[1,0,1,0,0],[0,0,1,0,1],[1,0,1,0,1],[1,0,1,1,0]])
print(a)