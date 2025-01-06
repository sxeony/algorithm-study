
def func(n):
    if n <= 3:
        return 1  
    dp = [0] * (n + 1)
    dp[1], dp[2], dp[3] = 1, 1, 1
    for i in range(4, n + 1):
        dp[i] = dp[i - 2] + dp[i - 3]
    return dp[n]

T = int(input())  
for i in range(T):
    n = int(input())  
    print(func(n)) 
