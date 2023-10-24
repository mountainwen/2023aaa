# week07-6 樓上改過來
s ="abcdabcd" #str字串
d = {} #dict字典
for c in s:
  if c in d:
    d[c]=d[c]+1
  else:
   d[c] = 1
  print ('現在讀到的字母',c,"字典變成", d)