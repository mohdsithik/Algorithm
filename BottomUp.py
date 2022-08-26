coins=[1,2,5]
amt=7
# total=amt+1
arr=[]
for x in range(0,amt+1):
    arr.append(amt+1)
arr[0]=0
# arr[1]=1
for y in range(1,amt+1):
    mini=arr[y]
    for z in range(len(coins)):
        # if amt==coins[z]:
        #    print(1)
        c=1
        t=y-coins[z]
        if t>0:
            c+=arr[t]

        if c<mini and t>=0:
            mini=c
        
    arr[y]=mini
print(arr[amt])

 
print(arr)
