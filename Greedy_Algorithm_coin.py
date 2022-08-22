def FindMin(amount):
    coins = [1, 2, 5, 10, 20, 50, 100, 200, 500, 2000]
    n = len(coins)
    ans = []
    i = n - 1
    while i >= 0:
        while amount >= coins[i]:
            amount = amount - coins[i]
            ans.append(coins[i])
        i -= 1

    for i in range(len(ans)):
        print(ans[i], end=" ")


if __name__ == '__main__':

    print('Enter the Amount : ')
    n = int(input())
    FindMin(n)
