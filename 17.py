sum=0
s=input('輸入五張牌:')
list_s=s.split(" ")
for i in range(5):
    if (list_s[i]=="j" or list_s[i]=="J"):
        sum+=11
    elif(list_s[i]=="q" or list_s[i]=="Q"):
        sum+=12
    elif(list_s[i]=="k" or list_s[i]=="K"):
        sum+=13
    elif(list_s[i]=="a" or list_s[i]=="A"):
        sum+=1
    else:
        sum=sum+int(list_s[i])
print(sum)