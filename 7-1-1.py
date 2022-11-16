#Sets the function "greeting"
def greeting():
   #The docstring is used to show what the function does and its limitations if asked for in the code
   '''Can only print "Hello World" on one line'''
   #The function greeting will return "Hellow World" when called
   return("Hello World")
   
G = greeting()
print(G)
#This statement would return the docstring from above
#help(greeting)