rc1=input("請輸入矩陣1行列數:")
r1=input("第一個矩陣第一列的值:")
r2=input("第一個矩陣第二列的值:")
rc2=input("請輸入矩陣2行列數:")
r3=input("第二個矩陣第一列的值:")
r4=input("第二個矩陣第二列的值:")

r1=r1.split(" ")
r2=r2.split(" ")
r3=r3.split(" ")
r4=r4.split(" ")
if (rc1==rc2):
    rc31=int(r1[0])+int(r3[0])
    rc32=int(r1[1])+int(r3[1])
    rc33=int(r2[0])+int(r4[0])
    rc34=int(r2[1])+int(r4[1])
    print(("%d %d\n%d %d")%(rc31,rc32,rc33,rc34))
else:
    print("兩個矩陣無法相加")
