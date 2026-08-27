# Coin Change Problem using Dynamic Programming

# Accept coin denominations
coins = list(map(int, input("Enter coin denominations separated by spaces: ").split()))

# Accept target amount
amount = int(input("Enter the target amount: "))

# DP array
dp = [float('inf')] * (amount + 1)
dp[0] = 0

# Calculate minimum coins
for i in range(1, amount + 1):
    for coin in coins:
        if coin <= i:
            dp[i] = min(dp[i], dp[i - coin] + 1)

# Display result
if dp[amount] == float('inf'):
    print("It is not possible to make the target amount with the given coins.")
else:
    print("Minimum number of coins required:", dp[amount])