             #(encription keys)
             #!-1     a-q    k-a    u-x
             #@-2     b-w    l-s    v-c
             #-3     c-e    m-d    w-v
             #$-4     d-r    n-f    x-b
             #%-5     e-t    o-g    y-n
             #^-6     f-y    p-h    z-m
             #&-7     g-u    q-j
             #*-8     h-i    r-k
             #:-9     i-o    s-l
             #;-10    j-p    t-z
s=input()
z=len(s)
arr=[]
encripted=[]
x="0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
y="~!@#$%^&*:qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
for i in range(z):
    arr.append(s[i])
for i in range(len(arr)):
    for j in range(len(x)):
        if(arr[i]==x[j]):
            arr[i]=y[j] 
            break
for  i in range(len(arr)):
    print(arr[i],end="")
print()
key=""
for j in range(len(s)):
    key=key+"#*#"
print("encription key",key)
