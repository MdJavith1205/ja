ma0,ji1=map(str,input().split())

sa0=0

if len(ma0)>len(ji1):

  ma0,ji1=ji1,ma0

i=0

while i<len(ma0):

  sa0+=(ord(ji1[i])-ord(ma0[i]))

  i+=1

for i in range(i,len(ji1)):

  sa0+=ord(ji1[i])-ord('a')+1

print(sa0)
