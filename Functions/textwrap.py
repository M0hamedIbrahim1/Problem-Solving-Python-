#link : https://www.hackerrank.com/challenges/text-wrap/problem
#author : Mohamed Ibrahim

import textwrap

def wrap(string, max_width):
    return "\n".join(textwrap.wrap(string,max_width))

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
