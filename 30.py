M=int(input("小明身上有幾元:"))
N=int(input("販賣機有幾種飲料:"))
k=0
for i in range(1,N+1):
    p=int(input("價錢%d:"%(i)))
    if (M%p==0):
        k+=1
print(k)