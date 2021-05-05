af=input("請輸入A的好友:")
bf=input("請輸入B的好友:")
a=af.split(" ")
b=bf.split(" ")
a=set(a)
b=set(b)
if (a&b==[]):
    print("0")
else:
    print(len(a&b))
