def fib(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        return fib(n-1) + fib(n-2)
    
def count_even_fib(n):
    array = list()
    i = 0
    while len(array) != n:
        value = fib(i)
        if value % 2 == 0:
            array.append(value)
        i += 1
    return array


num = int(input())
print(count_even_fib(num))


