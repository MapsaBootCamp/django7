### recursive ----> bazgashti ----> call a function inside of that. ----> baiad ye jai be payan beresim

######   1, 1, 2, 3, 5, 8, 13, ....  fib(10) = fib(9) + fib(8)

def fib(n: int, memoize={}) -> int:
    '''
    تابعی که ورودی آن در واقع اندیس هر عدد در دنباله فیبوناچی است و خروجی خود مقدار است.
    لکن حواسمان باشد که اندیس های این دنباله ای که ما میسازیم از صفر شروع میشود

    :params:index fibo
    :return:value of that index in fibo sequence
    '''
    
    if n==0 or n==1:
        return 1
    elif n in memoize:
        return memoize[n]
    else:
        memoize[n] = fib(n-1) + fib(n-2)
        return memoize[n]

