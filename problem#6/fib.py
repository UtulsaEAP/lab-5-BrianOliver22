""""
Name: Brian Oliver
lab time: 2/22/2024 10:00
""" 
def fibonacci(start_num):
    #write your code here
    x = 0
    n = 1
    fib = [0,1]
    if (start_num < 0 ):
        return -1
    if (start_num >= 0 ):
        while (len(fib)<= start_num):
            next_value =fib[len(fib)-1]+fib[len(fib)-2]
            fib.append(next_value)
        final = fib[start_num]
        return int(final)
    
    
        

if __name__ == '__main__':
    start_num = int(input())
    #print(f'fibonacci({start_num}) is {fibonacci(start_num)}')
    print(fibonacci(start_num))