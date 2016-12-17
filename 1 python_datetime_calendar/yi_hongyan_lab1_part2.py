# yi_hongyan_lab1_part2.py
# Purpose: Start learning to spot errors! 
# Author: Hongyan Yi
# Inputs: None
# Outputs: Prints to console
# Instructions:  
#   1. In a terminal window anchored in your directory, start python.exe (C:\Python27\ArcGIS10.2\python.exe)
#	2. At the Python prompt, type:  execfile("yi_hongyan_lab1_part2.py")
#   3. All the bugs are remarked


# Lab 1.part2
# from dateime import datetime    # bug: variable name didn't consistent
from datetime import datetime 


#Assign some strings to variables
animal1 = "alligators"

# animal2 = "birds'		# bug: string should use pair of single quote or double quote
animal2 = "birds"

n_animal1 = 2

#n_animal2 = five        # bug: five is not an integer number.
n_animal2 = 5        


#Get the date and time
# now = datatime.now()    # assign overall date time  # bug: typo mistake datetime not datatime
now = datetime.now() 

# thetime = now.hour+" "+now.minute     # pull the hour and minute and insert a space in between      # bug: could not concatenate 'str' and 'int' object use +
thetime = "%d:%d" %(now.hour,now.minute)


#Put them together to say something scary.
#print "At "+thetime+" in the morning, "+animal1 + "ate"+animal2        # bug: there is no effect to put space after a variable, should put space in the string
print "At "+thetime+" in the morning, "+animal1+ " ate "+animal2  

#print "There were "+n_animal1+animal1      # bug: could not concatenate 'str' and 'int' object
print "There were %d " %(n_animal1) + animal1

# print "At the beginning, there were "+n_animal2+animal2       # bug: could not concatenate 'str' and 'int' object
print "At the beginning, there were %d " %(n_animal2) + animal2
print "But at the end, there were none."





