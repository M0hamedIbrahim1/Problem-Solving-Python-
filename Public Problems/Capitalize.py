#link : https://www.hackerrank.com/challenges/capitalize/problem
#@author : @Mohamed Ibrahim
#!/bin/python3

def solve(s):
   s = s.split(" ")
   return(" ".join(i.capitalize() for i in s))
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
