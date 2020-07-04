import re

n = int(input())

for i in range(n):
    exp = input()
    try:
        re.compile(exp)
        print("True")
    except re.error:
        print("False")