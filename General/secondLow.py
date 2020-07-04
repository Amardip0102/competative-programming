if __name__ == '__main__':
    myList = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        myList.append([name, score])

    myList = sorted(myList, key= lambda x:x[1])
    second_low = sorted(list(set([score for name,score in myList])))[1]

    print([n for n, s in myList if s == second_low])

'''marksheet=[]
scorelist=[]
if __name__ == '__main__':
    for _ in range(int(input())):
            name = input()
            score = float(input())
            marksheet+=[[name,score]]
            scorelist+=[score]
    print(scorelist)
    b=sorted(list(set(scorelist)))[1]
    print(b)

    for a,c in sorted(marksheet):
             if c==b:
                    print(a)'''