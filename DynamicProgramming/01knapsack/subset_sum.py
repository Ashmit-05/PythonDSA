def subset_sum(arr,sum):
    dp = [[None for _ in range(sum+1)] for _ in range(len(arr)+1)]
    for i in range(sum+1):
        dp[0][i] = False
    for i in range(len(arr)+1):
        dp[i][0] = True
    dp[0][0] = True
    for i in range(1,len(arr)+1):
        for j in range(sum+1):
            if arr[i-1] <= j:
                dp[i][j] = dp[i-1][j-arr[i-1]] or dp[i-1][j]
            else:
                dp[i][j] = dp[i-1][j]
    # for row in dp:
    #     print(row)
    return dp[len(arr)][sum]

arr = [2,3,7,10]
sum = 5
answer = subset_sum(arr,sum) 
print(answer)
