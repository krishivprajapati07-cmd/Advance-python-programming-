# Longest Common Subsequence using Dynamic Programming

# Accept two strings
str1 = input("Enter the first string: ")
str2 = input("Enter the second string: ")

m = len(str1)
n = len(str2)

# Create DP table
dp = [[0] * (n + 1) for _ in range(m + 1)]

# Fill the DP table
for i in range(1, m + 1):
    for j in range(1, n + 1):
        if str1[i - 1] == str2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

# Display LCS length
print("Length of Longest Common Subsequence:", dp[m][n])