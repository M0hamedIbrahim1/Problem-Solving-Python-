# link : https://www.hackerrank.com/challenges/swap-case/problem
# author : @Mohamed Ibrahim

def swap_case(s):
    res = ""
    for i in s:
        if i == i.upper():
            i = i.lower()
            res+=i
        elif i == i.lower():
            i = i.upper()
            res+=i
    return res

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
