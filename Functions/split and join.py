# link : https://www.hackerrank.com/challenges/python-string-split-and-join/problem 
# author : @Mohamed Ibrahim

def split_and_join(line):
    z = line.replace(' ','-')
    return z    
            
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
