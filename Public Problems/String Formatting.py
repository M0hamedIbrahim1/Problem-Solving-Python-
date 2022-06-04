#link : https://www.hackerrank.com/challenges/python-string-formatting/problem
@Author : @Mohamed Ibrahim

def print_formatted(n):
    for i in range(1,n + 1):
        pad = n.bit_length()
        print(f'{i:{pad}d} {i:{pad}o} {i:{pad}X} {i:{pad}b}')
    

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
