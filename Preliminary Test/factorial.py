def factorial(a):
    fact = 1
    for i in range(1, a+ 1):
        fact = fact * i
    print(fact)

factorial(6)