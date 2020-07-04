def swap_case(s):
    tmp = []
    for char in s:
        if char.islower():
            tmp.append(char.upper())
        elif char.isupper():
            tmp.append(char.lower())
        else:
            pass
    return (''.join(tmp))

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
