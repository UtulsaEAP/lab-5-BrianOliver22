def fibonacci(start_num):
    #write your code here
    x = 0
    n = 1
    finish = 1
    if (start_num < 0 ):
        return -1
    elif (start_num == 0):
        return 0
    elif (start_num == 1):
        return 1
    elif(start_num > 1):
        while (start_num > 0):
            start_num -= 1
            finish += x
            x += x
            start_num -= 1
        return finish

if __name__ == '__main__':
    start_num = int(input())
    print(f'fibonacci({start_num}) is {fibonacci(start_num)}')