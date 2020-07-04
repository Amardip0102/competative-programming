def reverSizes(matrix):
    riverLength = []
    visited = [[0] * len(matrix)] * len(matrix[0])
    print(visited)
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if not visited[row][col]:
                visited[row][col] = True
                count = 0
                rw = row
                cl = col
                # forward
                while matrix[rw][cl] == 1:
                    visited[rw][cl] = True
                    count +=1
                    if cl !=len(matrix[row]):
                        cl = cl + 1
                #backward
                while matrix[rw][cl] == 1:
                    visited[rw][cl] = True
                    count += 1
                    if cl != 0:
                        cl = cl - 1
                #upward
                while matrix[rw][cl] == 1:
                    visited[rw][cl] = True
                    count += 1
                    if rw != 0:
                        rw = rw - 1
                #downward
                while matrix[rw][cl] == 1:
                    visited[rw][cl] = True
                    count += 1
                    if rw != len(matrix):
                        rw = rw + 1
                riverLength.append(count)
                count = 0
                print(count)
    return riverLength


a = reverSizes([[1,0,0,1,0],[1,0,1,0,0],[0,0,1,0,1],[1,0,1,0,1],[1,0,1,1,0]])
print(a)

