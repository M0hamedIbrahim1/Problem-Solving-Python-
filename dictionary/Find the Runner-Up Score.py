// link : https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    lis = list(set(arr))
    lis.sort()
    print (lis[len(lis)-2])
