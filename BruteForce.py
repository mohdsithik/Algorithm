<<<<<<< HEAD
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
=======
from itertools import combinations_with_replacement as rep
# amount = int(input("Enter The Amount : "))
amount = 13
coins = [1,2,5]
arr = []
for i in range(1,amount+1):
    arr.append(rep(coins,i))
temp=[]
for j in arr:
    for k in j:
        if sum(k)==amount:
            temp.append(k)
print(temp[0])  
     
>>>>>>> bd50ad387914dd34eab0664da5c5856926861b25
