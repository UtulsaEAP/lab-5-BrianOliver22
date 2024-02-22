def int_to_reverse_binary(num1):
    binary_val = []
#write your while loop here
    new = num1
    while (num1 > 0.99999):
     
        new = (num1 % 2)
        binary_val.append(str(new))
        num1 = int(num1/2)
    com = ""
    binary_val = com.join(binary_val)

    return binary_val


def string_reverse(input_string): 
    #reverse_input = input_string [::1]
    """"
    reverse_input = input_string.split()
    reverse_input = reverse_input [::1]
    sep = ""
    final= sep.join(reverse_input)
    
   #write your for loop here
    """
    final  = input_string [::-1] 
    return final

if __name__ == '__main__':
    user_input = int(input())
    
    binary_string = str(int_to_reverse_binary(user_input))
    binary_string = str(string_reverse(binary_string))
    
    print(binary_string)