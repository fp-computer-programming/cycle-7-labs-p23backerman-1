#gives function circle with the variable option
def circle(option):
    #The docstring is used to show what the function does and its limitations if asked for in the code, doc string will say doubles the variable option
    '''doubles option'''
    #new is twice as much as option
    new = option * 2
    return new
#gives function triangle with variable option2
def triangle(option2):
    #docstring that states that it will triple option2 and what was put for option
    ''' triples option2 and adds to option'''
    old = option2 * 3
    now = circle(5) + option2
    return now
#gives function rect with variable option3
def rect(option3):
    '''multiplies option3 by 1.5, then divides the return fuction triangle with option2 as 2 by the variable option3 '''
    bro = option3 * 1.5
    sis = triangle(2) / option3 
    return sis
print(rect(2))
#checks to be make sure the function rect works. should return with True True False False
print(rect(2) == 6)
print(rect(3) == 4)
print(rect(4) == 2)
print(rect(1) == 8)
