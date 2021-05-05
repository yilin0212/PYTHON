ans=input("請輸入第一組數字:")
g=input("請輸入第二組數字:")
ans=list(ans)
g=list(g)
a=0
b=0
length=len(ans)
for i in range(length):
    for j in range(length):
        if (ans[i]==g[j]):
            if(i==j):
                a+=1
            else:
                b+=1
            
if (a==4 and b==0):
    print("%dA%dB 全對"%(a,b))         
else:
    print("%dA%dB 加油"%(a,b))    
        
