a=int(input())
if a<=2000:ans=100
else:
	ans=100+(a-2000)//500*5
	if(a-2000)%500>0: ans+=5
print(ans)