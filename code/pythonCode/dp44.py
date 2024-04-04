import time

start = time.perf_counter()
n, aim = [3, 20]
arr = [5, 3, 2]
arr = [0] + arr
# print([n, aim])
# print(arr)
dp = [float("inf") for _ in range(aim + 1)]
dp[0] = 0
for ii in range(1, n + 1):
    for jj in range(arr[ii], aim + 1):
        dp[jj] = min(dp[jj], dp[jj - arr[ii]] + 1)
        # print([ii, jj] + dp)
print(dp)
if dp[-1] == float("inf"):
    print(-1)
else:
    print(dp[-1])
end = time.perf_counter()
runTime = (end - start) * 1000
print("elapsed time(ms)：", runTime)
