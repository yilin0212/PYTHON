m=int(input("輸入月:"))
n=int(input("輸入日:"))
s=(m*2+n)%3
if (s==0):
    print("普通")
elif(s==1):
    print("吉")
elif(s==2):
    print("大吉")