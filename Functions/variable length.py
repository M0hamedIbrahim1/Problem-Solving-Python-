def avg_numbers(*numbers):
    res = 0
    count = 0
    for i in numbers:
        res = res+i
        count = count+1
    return(res/count)
print('avg = ',avg_numbers(1000,2000,2600,3000))
