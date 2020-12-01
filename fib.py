n = 100
print("Fibonachi of", n," with python is ",end='')
fib = [0, 1]
[fib.append(fib[x - 1] + fib[x - 2]) for x in range(2, n)]
print(fib[n-1])