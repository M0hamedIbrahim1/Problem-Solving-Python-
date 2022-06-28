from scipy.optimize import fsolve
def f(b,a=36,d=39.4):
    return 1.30 * ((pow(a*b,0.625))/(pow(a+b,0.250))) - d

res = fsolve(f,1)
print(res)
