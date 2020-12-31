def fibr(n):
    if n <= 0:
        return 1
    else:
        return fib(n-1) + fib(n - 2)
#print(fib(3))

T = dict()
def fib(n):
    if n not in T:
        if n <= 1:
            T[n] = n
        else:
            T[n] = fib(n-1) + fib(n - 2)
    return T[n]
print(fib(3))

T = dict()
def fib(n):
    T[0],T[1] = 0,0
    for i in range(2,len(n)-1):
        T[n] = fib(n-1) + fib(n-2)
        return T[n]