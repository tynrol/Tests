#Есть произвольно задаваемый основной отрезок АВ и N произвольно задаваемых доп. отрезков. Необходимо вычислить длину основного отрезка, на который не происходит наложения дополнительных отрезков.
#Пример:
#А = 15, В = 165 (основной)
#N1 37 - 68
#N2 52 - 74
#N3 118 - 146
#N4 35 - 44
#N5 37 - 65
#N6 46 - 74
#Ответ: 83

a,b=map(int, input().split())
n = int(input())
arr = [[int(j) for j in input().split()] for i in range(n)]

for i in range(n):
    if arr[i][0] < a:
        arr[i][0] = a
    if arr[i][1] > b:
        arr[i][1] = b
    for j in range(n):
        if i == j:
            continue
        if arr[j][0] < arr[i][1] and arr[j][0] > arr[i][0]:
            arr[j][0] = arr[i][1]
        if arr[j][1] > arr[i][0] and arr[j][1] < arr[i][1]:
            arr[j][1] = arr[i][0]
        if arr[j][0] >= arr[i][0] and arr[j][1] <= arr[i][1]:
            arr[j][0] = arr[j][1]

sum = b-a
sub_sum = 0
for row in arr:
    sub_sum += row[1] - row[0]

print(sum-sub_sum)

