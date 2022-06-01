def fib(n):
    zero = 0
    one = 1
    if n == 1:
        return zero
    else:
        print(zero)
        print(one)
        for _ in range(2, n):
            multi = zero + one
            zero = one
            one = multi
            print(multi and zero and one) 
fib(int(input("Fibonacci sequence, please type a positive number higher then 5: ")))









#def fib(n):
#     a = 0
#     b = 1
#     if n == 1:
#         print(a)
#     else:
#         print(a)
#         print(b)
#         for i in range(2,n):
#             c = a + b
#             a = b
#             b = c
#             print(c)
# fib(10)