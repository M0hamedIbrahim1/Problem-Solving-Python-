#link   : https://codeforces.com/group/jfviGllBoY/contest/389763/problem/H
#author : Mohamed Ibrahim

n, t, k, d = map(int, raw_input().split())
p = (d + t) / t 
print "YES" if k * p < n else "NO"
