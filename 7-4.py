
#Sets the function find_sum to have the definitions num1 and num2
def find_sum(num1, num2):
   #sets the variable num_sum to equal num2 + num1
   num_sum = num2 + num1
   #find_sum will return the variable num_sum
   return num_sum
#the variable my_sum calls the function find_sum and sets the values to be 111 and 222
my_sum = find_sum(111, 222)
print(my_sum)
#When I run the program, it returns num_sum, which is 333 because that is 111 + 222
#Tests to make sure its 333, it is true
print(find_sum(111, 222) == 333)

#Tests to make sure its 555, it is true
print(find_sum(222, 333) == 555)
#tests to make sure it is not 444, it is false
print(find_sum(111, 222) == 444)
#tests to make sure it is 777, it is true
print(find_sum(222, 555) == 777)