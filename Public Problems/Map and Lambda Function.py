#link   :  https://www.hackerrank.com/challenges/map-and-lambda-expression/problem
#author :  Mohamed Ibrahim

fib = lambda y: y if y < 2 else fib(y - 1) + fib(y - 2)
print map(lambda x: x**3, map(fib, range(input())))
