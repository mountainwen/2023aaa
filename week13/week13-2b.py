a = [0]*100 #有100格,每格都是0
a[0]=1
a[1]=1
for i in range(2,100):
  a[i]=a[i-1]+a[i-2]
print(a)