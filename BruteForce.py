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
     