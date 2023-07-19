def fibonacci_sequence(n):
    fib_list = []
    if n <= 0:
        return fib_list
    fib_list.append(0)
    if n > 1:
        fib_list.append(1)
    while len(fib_list) < n:
        next_fib = fib_list[-1] + fib_list[-2]
        fib_list.append(next_fib)
    
    return fib_list
