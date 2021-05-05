m=int(input("請輸入階乘值M?"))
total=i=1
while (total<m):
    total=total*i
    if total>m:
        break
    i+=1
    
  
print("超過M為%d的最小階層N值為:%d"%(m,i))
    