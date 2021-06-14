def get_number(question="How many Fibonnaci numbers should I generate?"):
    num = int(input(question))
    return num

def make_next_Fibonacci(a,b):
    return a+b

def generate_Fibonacci():
    length = get_number()
    if length==0:
        return [1]
    elif length==1:
        return [1,1]
    else: 
        counter = 2
        fib = [1,1]
        while length > counter:           
            a = fib[len(fib)-2]
            b = fib[len(fib)-1]
            fib.append( make_next_Fibonacci(a,b) )
            counter = counter+1
        return fib

generate_Fibonacci()