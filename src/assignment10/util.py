#Word Order
def cnd(n):
  val=[]
  count={}
  for i in n:
      if i in count:
         count[i]+=1
      else:
         count[i]=1
  counts=[]
  for a,b in count.items():
        counts.append(b)

  return counts

# Code