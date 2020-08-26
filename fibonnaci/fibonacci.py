
def find_fibonacci_by_recursion(n):
    if n <= 1 and n > 0:
        return 1
    elif n == 0:
        return 0
    else:
        return find_fibonacci_by_recursion(n-1) + find_fibonacci_by_recursion(n-2)

def find_fibonacci_by_loop(n):
    fib_list =[0,1]
    for i in range(0,n):
        if i > 0:
            fib_list.append(fib_list[i] + fib_list[i-1])
    return fib_list[n]