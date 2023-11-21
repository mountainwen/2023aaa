a=[9,8,7,6,5,4,3,2,1,0]
N=len(a)#取出陣列長度
print(a)
for i in range(N-1):#只做一輪的泡泡
  if a[i] > a[i+1]:
    a[i], a[i+1] =a[i+1], a[i]
print(a)