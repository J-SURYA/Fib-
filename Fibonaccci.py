l_ip=[]
n=int(input("No. of inputs:"))
if n<1:
    print("Please give inputs.")
else:
    for i in range(n):
        a=int(input("Enter your sample value:"))
        l_ip.append(a)
    i=0
    j=1
    lfib=[0,1]
    large=max(l_ip)
    while lfib[-1]<=large:
        a=lfib[i]+lfib[j]
        lfib.append(a)
        i+=1
        j+=1
    for b in l_ip:
        fibsum=0
        for j in lfib:
            if j%2==0 and j<=b:
                fibsum+=j
        if b<0:
            print("Enter positive values from 0 to n.")
        else:
            print(fibsum)
    #test
            

    

    
    
    
