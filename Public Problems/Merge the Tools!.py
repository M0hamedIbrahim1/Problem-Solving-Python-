#link   : https://www.hackerrank.com/challenges/merge-the-tools/problem
#author : Mohamed Ibrahim

def merge_the_tools(string, k):
    my_list = []
    cnt = 0

    for i in range(len(string)):
        cnt+=1
        if string[i] not in my_list:
            my_list.append(string[i])
        if cnt == k:
            print("".join(my_list))
            my_list = []
            cnt = 0
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
    
