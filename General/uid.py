import re

def validate(UID):
    for i in range(len(UID)):
        u = ''.join(sorted(UID[i][0]))
        try:
            assert re.search(r'[A-Z]{2}',u)
            assert re.search(r'\d{3}',u)
            assert not re.search(r'[^a-zA-Z0-9]',u)
            assert not re.search(r'(.)\1',u)
            print("Valid")
        except:
            print("Invalid")

N = int(input())
UID = []
for n in range(N):
    UID.append(input().split("\n"))
validate(UID)