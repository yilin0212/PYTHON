num=list(input("輸入一組四位數字:"))
for i in range(0,4):
    num[i]=(int(num[i])+7)%10

print("輸出加密後的數字為:"+str(num[2])+str(num[3])+str(num[0])+str(num[1]))