n=int(input())
p=[]
sum=0
sumLocal=0
for i in range(n):
    p.append(int(input()))
for i in range(n):
    sumLocal+=p[i]
    if sumLocal<0:
      sumLocal=0
    elif sum<sumLocal:
      sum=sumLocal
print(sum)

             
