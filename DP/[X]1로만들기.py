x = int(input())
dp = [0] * (x + 1)

for i in range(2, x + 1):
    dp[i] = dp[i - 1] + 1
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i //3] + 1)
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i //2] + 1)

print(dp[x])

# 복습 풀이
# d[i]: i를 1로 만들기 위한 최소 연산 횟수
n=int(input())
dp=[0]*(n+1)

for i in range(2,n+1):
    dp[i]=dp[i-1]+1
    if i%3==0:
        dp[i]=min(dp[i],dp[i//3]+1)
    if i%2==0:
        dp[i]=min(dp[i],dp[i//2]+1)
        
print(dp[n])