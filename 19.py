n=int(input("組數為:"))

for i in range(1,n+1):
    num=input(("第%d組:")%(i))#輸入兩數字，用空格區分
    num=num.split(" ")
    p=int(num[0])*250+int(num[1])*175
    print("第%d組應收費用:%d"%(i,p))