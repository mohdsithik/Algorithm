amount=int(input("Enter The Amount : "))
coins=[1,2,5]
arr=[]
while(amount>0):
    temp=[]
    for x in coins:
        a=amount-x
        if a>=0:
            temp.append(a)
    mini=temp.index(min(temp))
    arr.append(coins[mini])
    amount=temp[mini]

print(arr)
