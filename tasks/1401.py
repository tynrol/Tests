n=int(input())
x,y=map(int,input().split())
field=[][]
placed=0
#передаем расположение текущего квадрата со стороной 2^n
#в котором расположена точка
#относительно левого верхнего угла
def func(n,xCor,yCor,quater):
    #todo
    #вбивание остального квадрата
    #независимого от точки
    #определение относительного расположение точки
    #(следующей четверти и их координат)
    if n>1:
        return(func(n,xCor,yCor,quater))
    else:
        field[x,y]=0
        placed++
        #
        if quater==1:
            field[x-1,y]=placed
            field[x-1,y+1]=placed
            field[x,y+1]=placed
            placed++
        elif quater==2:
            field[x+1,y]=placed
            field[x+1,y+1]=placed
            field[x,y+1]=placed
            placed++
        elif quater==3:
            field[x+1,y]=placed
            field[x+1,y-1]=placed
            field[x,y-1]=placed
            placed++
        elif quater==4:
            field[x-1,y]=placed
            field[x-1,y-1]=placed
            field[x,y-1]=placed
            placed++
        
        
        
        
    
