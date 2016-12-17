# yi_hongyan_lab1_part1.py
# Purpose:  implement python basic sytax and grammers, string, math, date and time, function and dot notation
# Author:  Hongyan Yi
# Inputs: None
# Outputs:   Prints to console
# Instructions:  
#   1. In a terminal window anchored in your directory, start python.exe (C:\Python27\ArcGIS10.2\python.exe)
#	2. At the Python prompt, type:  execfile("yi_hongyan_lab1_part1.py")
#	3. This file finish ten subsections within some tasks,the content of them were commented at the beginning.


# Lab 1.part1
from __future__ import division
from datetime import datetime

# Subsection 1: Do some string examples.
print "\n\n---------------Subsection 1: Do some string examples---------------"
# task 1.1 copy of string
str_Happy = "Happy"			# strHappy = 'Happy' is also OK	
print "Print 5 copies of string 'Happy'"
print str_Happy * 5			# Print 5 copies of string "Happy"
print "\nPrint 5 copies of string 'Happy' with spaces between each"
print (str_Happy + " ") * 5	# Print 5 copies of string "Happy" with spaces between each, can use mutiply int but cannot mutiply float

# task 1.2: use backslash for special characters: apostrophe and backslash
# str_apostrophe =  'I can\'t believe I\'m falling apart,said Humpty' # this works because the apostrophes have been escaped using the backslash. 
str_apostrophe =  "I can't believe I'm falling apart,said Humpty"	# this works because the string is surrounded by double quotes,so Python doesnot interpret the apostrophes as marking the beginning or ending of a string
print "\nPrint string with postrophe"
print str_apostrophe 
path = "c:\\python27\\arcgis10.2\\" # path with backslash
print "\npath = %s" %(path)

# task 1.3: string concatenation
path = "R:\\Geo578\\Students\\yih\\Lab1\\"
print "updated path = %s" %(path)   # print updated path
myfile = "jujuhearts.py"
print "myfile = %s" %(myfile)       # print myfile
fullfilename = path + myfile        # concatenation of path and myfile
print "After concatenation, fullfilename = %s" %(fullfilename)

# Subsection 2: Accessing strings by index
print "\n\n---------------Subsection 2: Accessing strings by index---------------"
# task 2.1 Accessing strings by index
print "The fifth character of variable path is %s" %(path[4])	                    # print the fifth character of variable path
#print "The fifth character of variable path from the end is %s" %(path[-5:-4])     # print the fifth character from the end
print "The fifth character of variable path from the end is %s" %(path[-5])  		# a simpler way to do this is: path[-5]
# task 2.2 Dot notation
print "The length of variable path is %d" %(len(path))                              # print the length of the string
print "The uppercase version of variable path is %s" %(path.upper())                # print the uppercase version of the string


# Subsection 3: Accessing strings by index: More advanced use!
print "\n\n---------------Subsection 3: Accessing strings by index: More advanced use!---------------"
print "The last three characters in fullfilename variable is %s" %(fullfilename[-3:])   # print the last three characters in fullfilename variable
extension = "arecool"
longerfullfilename = "R:\\Geo578\\Students\\yih\\Lab1\\longer\\test.py"
index = longerfullfilename.find(".py")
str_after_insert = longerfullfilename[:index] + extension + longerfullfilename[index:]
print "extension = %s" %(extension)
print "longerfullfilename = %s" %(longerfullfilename)
print "After insertion, longerfullfilename = %s" %(str_after_insert)


# Subsection 4: Do some math examples
print "\n\n---------------Subsection 4: Do some math examples---------------"
x = 12 ** 2
y = 6
z = x / y               # x divided by y
print "x = %d, y = %d, z = x / y = %0.2f" %(x,y,z)

a = 3
b = 4
c = a ** 2 + b ** 2     # a squared plus b squared
print "\na = %d, b = %d, c = a^2 + b^2 = %0.2f" %(a,b,c)

a = 314
b = 7
d = a % b               # remainder of a divided by b
print "\na = %d, b = %d, d = %0.2f" %(a,b,d)


# Subsection 5: Decimals and more advanced calculations
# task5.1 Calculate the area of a circle 
print "\n\n---------------Subsection 5: Decimals and more advanced calculations---------------"
mypi = 22 / 7       # make sure calculation results in a decimal value (from __future__ import division)
#mypi = 22 / float(7) #simple way
#mypi = 22 / 7.0	#simple way
radius = 5
area = mypi * radius * radius
print "mypi = %f, radiu = %d, area = %f" %(mypi,radius,area)

# task5.2 Calculate OSU final budget
salary = 50000 / 2                          # salary for six months, 50,000 / year,
benefit = salary * 67 / 100                 # benefits are 67% of the salary
direct_charge = salary + benefit
osu_charge = direct_charge * 47 / 100       # OSU charges 47% on that total direct charge
final_budget = direct_charge + osu_charge    
print "\ndirect_charge = %.2f, osu_charge = %.2f, final_budget = %.2f" %(direct_charge,osu_charge,final_budget)


# Subsection 6: String formatting
print "\n\n---------------Subsection 6: String formatting---------------"
town = "Corvallis"
precip = "rains"
print "It %s a lot in %s." %(precip,town)   # normal method 


# Subsection 7: String formatting: The New Way
print "\n\n---------------Subsection 7: String formatting: The New Way---------------"
print "It {} a lot in {}." .format("rains","Corvallis") # string.format()


# Subsection 8: Converting formats
print "\n\n---------------Subsection 8: Converting formats---------------"
# task 8.1 covert number to string
number = 12
str_number = str(number)    
print "convert number to string: number = %d,str_number = %s" %(number,str_number)

# task 8.2 replace words in sentence
origin_sentence = 'There are twelve eggs in a dozen'
new_sentence = origin_sentence.replace('twelve','12')   # after calling replace, origin_sentence didn't change but return a new_sentence
print "\norigin_sentence = %s \nnew_sentence = %s" %(origin_sentence,new_sentence)


# Subsection 9: Working with Date and Time
print "\n\n---------------Subsection 9: Working with Date and Time---------------"
starttime = datetime.now()      # now is not a property but a function
str_starttime = str(starttime)
print "starttime = %s" %str_starttime		# how to show starttime
extension = str(starttime.day) + str(starttime.month)
str_after_insert = longerfullfilename[:index] + extension + longerfullfilename[index:]  # only need day and month 
print "After insertion, longerfullfilename = %s" %(str_after_insert)


# Subsection 10: New functions
print "\n\n---------------Subsection 10: New functions---------------"
# task 10.1 class list([iterable])
print"Eg1: class list([iterable])"
print list('123')                           # split character by character

# task 10.2 enumerate(sequence, start=0)
number = ['one', 'two', 'three', 'four','five','six','seven','eight','nine','ten']
print "\nEg2: enumerate(sequence, start=0)"
print list(enumerate(number,start = 1))     # could not directly print enumerate() but use list(enumerate())



