#6-5

import numbers


def six_five(numbers): 
   #puts numbers in a list
   numbers = [1, 2, 3, 4, 6, 9, 9,]

   #Sorts the numbers in the list in reverse order
   numbers.sort(reverse=True)
   #if the first index is the same as the last index, it will print that tbere was an error. if this is not the case, then it will print the first and last variable in the newly sorted list so it prints the highest and lowest variable
   if numbers[0] == numbers[-1]:
      return("error:list does not meet specifications") 
   else : 
      return(numbers[0]) 
      return(numbers[-1])
m = six_five(numbers)
print(m)
print(six_five(numbers) == None)
print(six_five(numbers) == True)
print(six_five(numbers) == False)
print(six_five([1,1]) == "error:list does not meet specifications")

#6-6

#gives the function six_six with variable ulist


def six_six(a, b, c, d, e,):
   #Gets the length of the words the user put in and stores it as a new variable
   La = len(a)
   Lb = len(b)
   Lc = len(c)
   Ld = len(d)
   Le = len(e)
   #Puts the corresponding variables in the same spots as the previous ones in a new list
   Llist = [La, Lb, Lc, Ld, Le]
   return(Llist)
#should return true, false, true, false when checked
print(six_six('bird', 'crazy', 'bonkers', 'smell', 'the'))
print(six_six('bird', 'crazy', 'bonkers', 'smell', 'the') == [4,5,7,5,3])
print(six_six('bird', 'crazy', 'bonkers', 'smell', 'the') == [4,5,7,5,2])
print(six_six('bird', 'crazy', 'bonkers', 'smell', 'te') == [4,5,7,5,3])
print(six_six('bird', 'crazy', 'bonkers', 'smell', 'cant') == [4,5,7,5,4])

#6-7
#Asks for three numerical values
def six_seven(option4, option5, option6):
   Nlist = [option4 * 2, option5 * 2, option6 * 2]
   return Nlist
print(six_seven(1, 2, 3))
print(six_seven(1, 2, 3) == [2, 4, 6])
print(six_seven(1, 2, 3) == [3, 4, 6])
print(six_seven(2, 4, 6) == [4, 8, 12])
print(six_seven(2, 4, 6) == [4, 8, 11])

#6-8
#gives the function six_eight with variables l m k
def six_eight(l, m, k):
   Nlist = [l, m, k]
   
   #Checks if the numbers are all even or odd, and if neither it will return mixed
   if l % 2 == 0 and m % 2 == 0 and k % 2 == 0:
    return("Even")
   elif l % 2 != 0 and m % 2 != 0 and k % 2 != 0:
    return("Odd")
   else: return("mixed")

#the first three should be true. last should be false
print(six_eight(10, 8, 4) == "Even")
print(six_eight(9, 8, 4) == "mixed")
print(six_eight(9, 7, 3) == "Odd")
print(six_eight(10, 8, 3) == "Even")