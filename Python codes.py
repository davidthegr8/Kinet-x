#for i in range(9):
#    print i
"""Prints all numbers in a range"""

#string = "Hello World"
#for x in string:
#    print x
"""Prints all letters and/or numbers in a string"""

#name = raw_input('What is your name?\n')
#print 'Hi, %s.' % name; print 'nice to meet you.'
"""Finds out one's name through question"""

#total=1
#for i in range (1, 51):
#    total *= i
#    print "%s" % i, total
"""Anything factorial"""

#a = firework
#b = show
#a[(any number)]
"""Lets you find a letter in a word by the number"""
#a[: (any nuber)]
"""Gives you the letters that are up to but not including it"""
#a[(any number) :]
"""Gives you the letters that come after a certain point"""
#len(a)
"""Gives you the length of a given list"""
#a+b
"""Adds the two lists together"""
#a*4
"""Puts a list 4 times"""

#for i in range(len('penguin')): 
#        print i, 'penguin'[i] 
"""Gives you the index value af each letter in a string"""

#for i in range(1, 6):
#    for x in range (1, 6):
#        print i, x
"""Gives you all the possible combinations of numbers"""

#a = ["bnc", "c", "vdwhj", "z", "atk"]
#sorted(a)
"""Alphabetizing the strings"""
#sorted(a, reverse=True)
"""Reverse alphabet order"""
#sorted(a, key=len)
"""Orders the strings in length order"""
#sorted(a, key=len, reverse=True)
"""Orders the strings in reverse length order"""

#a = [9, 4, 13, 1, 2]
#x = [firework]
#a.reverse()
"""Reverses the order of the list"""
#a.sort()
"""Sorts the list in numerical order"""
#sorted(x)
"""Sorts the letters of the word in aplhabetical order"""

#x, y = (1, 1)
#while x < 100
#    print format(x)
#    x, y = (y, x+y)
"""Fibonacci sequence up to but not including a number"""

#for x in range(20):
#    print x**0.5
"""Finds the square roots but not including a number"""

#for x in range(20):
#    print x**2
"""Finds the squares of all the numbers up to but not including a number"""

#a="ab"
#a[1]+a[0]
"""Reverses the order of the letters in the string aand still puts it as one string"""

#def addStr(string):
#    print "but"+(string)
"""Adds a word before or after a string and how to make a function"""

#def isPsqr(num):
#    for i in range (num):
#        if i**2==num:
#            return True
#    return False
"""Finds if a number is a perfect square"""            

#def isEven(num):
#    return (num%2)==0
"""Tells you if a number is even or can be modified for odd"""

def isVow(letter):
    return letter in ['a','e','i','o','u']
"""Tells you whether or not a letter is a vowel"""

def PigLatin(word):
    if isVow(word[0]):
        return word+"way" 
    if isCons(word[1]):
            return word[2:]+word[0]+word[1]+'ay'
    if isVow(word[1]):
        return word[1:]+word[0]+'ay'
"""Pig latin code"""                

#def isVowel(letter):
#    return letter in ['a','e','i','o','u']
"""Tells you if a letter is a vowel"""

def isVowel(letter):
    return letter in ['a','e','i','o','u']
def isCons(letter):
    return not isVowel(letter)
"""Defining a consanant"""

#chr()
"""Numbers to letters"""
#ord()
"""Letters to numbers"""

def CC(num):
    if num>=65<=97:
        return chr((((ord('A')+num)-65)%26)+65)
    return chr((((ord('a')+num)-97)%26)+97)
"""Caesar's cipher"""

def encrypt(word, shift):
    for i in word:
        if ord(i)>=65<=96:
            y=chr((((ord(i)+shift)-65)%26)+65)
            if ord(i)>=97<=122:
                y=chr((((ord(i)+shift)-97)%26)+97)
            print y
"""Encrypting a word"""

def decrypt(word, shift):
    for i in word:
        if ord(i)>=65<=96:
            y=chr((((ord(i)-shift)-65)%26)+65)
            if ord(i)>=97<=122:
                y=chr((((ord(i)-shift)-97)%26)+97)
            print y
"""Decrypting a word"""




        
        
        
        
    










    
