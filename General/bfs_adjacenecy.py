def bfs_adjacency(matrix):
    '''
      0 1 2 3
    0 0 1 1 0
    1 1 0 0 1
    2 1 0 0 0
    3 0 1 0 0
    :param matrix: Adjacency Matrix is the matrix which denotes the graph
    :return: Graph Nodes
    '''

    visited = [0] * len(matrix)

    queue = [0]

    node = queue.pop(0)
    isFirst = False
    print(node)
    visited[0] = True

    # Go on until nothing inside queue
    while  len(queue) != 0 or isFirst is False:
        isFirst = True
        for x in range(len(matrix)):
            if matrix[node][x] == 1 and visited[x] == 0:
                visited[x] = True

                queue.append(x)

        node = queue.pop(0)
        print(node)

bfs_adjacency([[0,1,1,0], [1,0,0,1],[1,0,0,0],[0,1,0,0]])