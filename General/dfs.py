def dfs_adjacency(matrix):
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

    stack = [0]
    visited[0] = True

    # Go on until nothing inside queue
    while len(stack):
        node = stack.pop(len(stack) - 1)
        print(node)
        for x in range(len(matrix)):
            if matrix[node][x] == 1 and visited[x] == 0:
                visited[x] = True
                stack.append(x)

dfs_adjacency([[0,1,1,0], [1,0,0,1],[1,0,0,0],[0,1,0,0]])