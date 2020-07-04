def maxI(arr):
    max= 0
    for i in range(len(arr)):
        if arr[i] > max:
            max =arr[i]
    return max

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int,input().strip().split()))[:n]
    arr = sorted(arr)
    i = len(arr) - 1
    while(i>0):
        if(arr[i] > arr[i - 1]):
            print(arr[i-1])
            break
        else:
            i -=1


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int,input().strip().split()))[:n]
    mx = max(arr)
    while mx == max(arr):
        arr.remove(mx)
    print(max(arr))




