s=input()
a=input()
if "#*#" in a:
    z=len(s)
    arr=[]
    encripted=[]
    x="0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    y="~!@#$%^&*:qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
    for i in range(z):
        arr.append(s[i])
    for i in range(len(arr)):
        for j in range(len(x)):
            if(arr[i]==y[j]):
                arr[i]=x[j] 
                break
    for  i in range(len(arr)):
        print(arr[i],end="")