import sys
input=sys.stdin.readline

n=int(input())
a=list(map(int,input().rstrip().split()))
d=[1]*n

for i in range(1,n):
    for j in range(0,i):
        if a[j]<a[i]:
            d[i]=max(d[i],d[j]+1)

print(max(d))