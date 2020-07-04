import re
def validate(Nums):
    for i in range(len(Nums)):
        if bool(re.search(r'^(7|8|9)\d{9}$', Nums[i][0])):
            print("YES")
        else:
            print("NO")

N = int(input())
Nums = []
for n in range(N):
    Nums.append(input().split("\n"))
validate(Nums)