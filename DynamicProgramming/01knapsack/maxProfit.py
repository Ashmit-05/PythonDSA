# https://www.youtube.com/watch?v=kvyShbFVaY8&list=PL_z_8CaSLPWekqhdCPmFohncHwz8TY2Go&index=3&ab_channel=AdityaVerma

# using recursion + memoization
dp = [[-1 for _ in range(102)] for _ in range(1002)]
def knapsack(wt,val,W,n) :
    if(n == 0 or W == 0) :
        return 0

    if dp[n][W] != -1 :
        return dp[n][W]

    if(wt[n-1] <= W) :
        dp[n][W] = max(val[n-1] + knapsack(wt,val,W-wt[n-1],n-1),knapsack(wt,val,W,n-1))
        return dp[n][W]
    elif(wt[n-1] > W) :
        dp[n][W] = knapsack(wt,val,W,n-1)
        return dp[n][W]

# using top down approach
def topdown(wt,val,W,n) :
    dp1 = [[0 if i == 0 or j == 0 else None for j in range(W+1)] for i in range(n+1)]
    for i in range(1,n+1) :
        for j in range(1,W+1) :
            if wt[i-1] <= j :
                dp1[i][j] = max(val[i-1] + dp[i-1][j-wt[i-1]], dp[i-1][j])
            else :
                dp[i][j] = dp[i-1][j]
    return dp1[n][W]

wt = [1,3,4,5]
val = [1,4,5,7]
W = 7
n = 4
maxProfit = knapsack(wt,val,W,n)
maxProfit1 = topdown(wt,val,W,n)
print(maxProfit)
print(maxProfit1)

