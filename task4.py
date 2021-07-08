def fibo(n):
    if(n <= 1):
        return n
    else:
        return(fibo(n-1) + fibo(n-2))
n = int(input("Enter number of terms:"))
print("Fibonacci numbers:")
for i in range(n):
    print(fibo(i))
