# link   : https://codeforces.com/problemset/problem/1728/C
# author : Mohamed Ibrahim




from collections import Counter
for _ in range(int(input())):
    use=input()
    axe=Counter(input().split())
    axe.subtract(Counter(input().split()))
    ans=0
    for key in list(axe.keys()):
        if len(key) > 1:
            ans += abs(axe[key])
            axe[str(len(key))] += axe[key]
            axe[key] = 0
    print(ans+(sum(axe[key] for key in axe.keys() if axe[key] > 0) * 2) - abs((axe["1"])))
    
    
    
