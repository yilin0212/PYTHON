a=input("請輸入string_a:")
b=input("請輸入string_b:")
a=set(a)
b=set(b)

c=sorted(a&b)


if (c==[]):
    print("N")
else:
    print(c)