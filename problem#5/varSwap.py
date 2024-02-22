""""
Name: Brian Oliver
lab time: 2/21/2024 3:30
""" 
def swap_values(user_val1, user_val2, user_val3, user_val4):   
   #write your code here
   non = user_val1
   none = user_val3
   user_val1 = user_val2
   user_val2 = non
   user_val3 = user_val4
   user_val4 = none
   lst = [str(user_val1), str(user_val2), str(user_val3), str(user_val4)]
   sep = " "
   lst = sep.join(lst)
   assert lst

if __name__ == '__main__':   
   user_input1 = int(input())
   user_input2 = int(input())
   user_input3 = int(input())
   user_input4 = int(input())
   #store output for every input here
   #print those output
   print(swap_values(user_input1,user_input2,user_input3,user_input4))

 