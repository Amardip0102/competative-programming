def merge_the_tools(string, k):
    # your code goes here
    tmp = []
    length = 0
    for char in string:
        length +=1
        if char not in tmp:
            tmp.append(char)
        if length == k:
            print(''.join(tmp))
            tmp = []
            length = 0


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)


'''
S, N = input(), int(input())
for part in zip(*[iter(S)] * N):
    d = dict()
    print(''.join([ d.setdefault(c, c) for c in part if c not in d ]))
    
'''
'''
s = 'abcdefghi'
itr = iter(s)
for part in zip(*[itr] *3):
    print(part)
'''