import re
def minion_game(string):
    # your code goes here
    score = {'Kevin':0, 'Stuart':0}
    substring = []
    # compute score for Kevin
    # Kevin Starts with Vovels A,E,I,O,U
    res = [string[i: j] for i in range(len(string))
           for j in range(i + 1, len(string) + 1)]

    for i in range(len(res)):
        if (bool(re.search(r'^(A|E|I|O|U)', res[i]))):
            score['Kevin'] += 1
        else:
            score['Stuart'] += 1

    if score['Kevin'] > score['Stuart']:
        print('Kevin ',score['Kevin'])
    elif score['Stuart'] > score['Kevin']:
        print('Stuart ',score['Stuart'])
    else:
        print("Draw")
if __name__ == '__main__':
    s = input()
    minion_game(s)