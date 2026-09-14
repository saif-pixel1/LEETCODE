n= [0,1,1,0,0,1,0,1,1,0,0,1,1]

l = 0 
r = len(n) - 1
while l<r:
  if n[l] != 0:
    n[l],n[r] = n[r] , n[l]
    r-=1
  else:
    l+=1
print(n)