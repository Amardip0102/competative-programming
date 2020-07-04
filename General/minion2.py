import re
def minion_game(string):
    # your code goes here
    score = {'Kevin':0, 'Stuart':0}
    print(len(string))
    for i in range(len(string)):
        if string[i] in "AEIOU":
            score['Kevin'] +=len(string) - i

        else:
            score['Stuart'] += len(string) - i

    if score['Kevin'] > score['Stuart']:
        print('Kevin ',score['Kevin'])
    elif score['Stuart'] > score['Kevin']:
        print('Stuart ',score['Stuart'])
    else:
        print("Draw")
if __name__ == '__main__':
    s = input()
    minion_game(s)