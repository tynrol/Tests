from itertools import combinations

n = int(input())
list = list(map(int, input().split()))

def listtoarr(list,n):
    array=[]
    for i in range(n):
        array.append(list[i])
    return array

arr=listtoarr(list,n)
mass=sum(arr)
min=mass
for i in range((n//2)+1):
    for comb in combinations(arr, i):
        if abs(mass - 2*sum(comb)) < min:
            min=abs(mass - 2*sum(comb))
print(int(min))



        
             
