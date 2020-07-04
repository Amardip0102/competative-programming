if __name__ == '__main__':
    N = int(input())
    myList = []
    query = []
    for i in range(N):
        query.append(list(input().rstrip().split()))
        if query[i][0] == "insert":
            myList.insert(int(query[i][1]), int(query[i][2]))
        elif query[i][0] == "print":
            print(myList)
        elif query[i][0] == "remove":
            myList.remove(int(query[i][1]))
        elif query[i][0] == "append":
            myList.append(int(query[i][1]))
        elif query[i][0] == "sort":
            sorted(myList))
        elif query[i][0] == "pop":
            myList.pop()
        elif query[i][0] == "reverse":
            myList.reverse()
        else:
            pass