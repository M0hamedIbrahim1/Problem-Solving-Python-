#link   : https://www.hackerrank.com/challenges/the-minion-game/problem
#author : Mohamed Ibrahim

def minion_game(string):
    s = k = 0
    v = "AEIOU"
    for i in range(len(string)):
        if(string[i] in v):
            k += len(string)-i
        else:
            s+=len(string)-i
    if k > s:
        print ("Kevin", k)
    elif k < s:
        print ("Stuart", s)
    else:
        print ("Draw")
if __name__ == '__main__':
    s = input()
    minion_game(s)
