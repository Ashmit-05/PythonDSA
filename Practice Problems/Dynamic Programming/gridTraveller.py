def gridTraveller(m,n,memo={}) :
    if str(m)+','+str(n) in memo :
        return memo[str(m)+','+str(n)]
    if m==1 or n==1 :
        return 1
    memo[str(m)+','+str(n)] = gridTraveller(m-1,n,memo) + gridTraveller(m,n-1,memo)
    return memo[str(m)+','+str(n)]

print(gridTraveller(2,3))
print(gridTraveller(3,3))
print(gridTraveller(4,3))
print(gridTraveller(4,4))
print(gridTraveller(18,18))


