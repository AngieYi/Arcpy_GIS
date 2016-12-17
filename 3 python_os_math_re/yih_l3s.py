# GEO 578:  yih_l3s.py
# Purpose: script file to Test yih_lab3_functions.py
# is author: Hongyan Yi

# HOW TO USE THIS FILE:
# The purpose of this file is to show to Test functions 
#  that is are defined in the yih_lab3_functions.py


import yih_lab3_functions as yi3func
import os


print("\n--------------------Program 1: is_numeric----------------------------")
# 1: test unqualified values
value = 'craziness'
print("string " + str(value) + " is a number? "+ str(yi3func.is_numeric(value)))

# 2: test qualified values
value = -0x260           # hexadecimal int ?
print "\nInt -0x260 is a number? " + str(yi3func.is_numeric(value)) 
#print "Int 0x%x is a number? " %value + str(yi3func.is_numeric(value))
#print("Int "+str(value)+" is a number? " + str(yi3func.is_numeric(value)))

value = 0x69            # hexadecimal int ?
print "\nInt 0x%x is a number? " %value + str(yi3func.is_numeric(value)) 
#print("Int "+str(value)+" is a number? " + str(yi3func.is_numeric(value)))

value = 1.1e2           # test float
print("\nfloat 1.1e2 is a number? " + str(yi3func.is_numeric(value)))
#print("float "+str(value)+" is a number? " + str(yi3func.is_numeric(value)))

value = -1.1e2          # test float
print("\nfloat -1.1e2 is a number? " + str(yi3func.is_numeric(value)))
#print("float "+str(value)+" is a number? " + str(yi3func.is_numeric(value)))

value = -0x19323L       # test long: integers of unlimited size
print("\nLong -0x19323L is a number? " + str(yi3func.is_numeric(value)))
#print("Long " + str(value) + " is a number? " + str(yi3func.is_numeric(value)))

value = -4721885298529L     # test complex
print("\nLong -4721885298529L is a number? " + str(yi3func.is_numeric(value)))
#print("Long " + str(value) + " is a number? " + str(yi3func.is_numeric(value)))

value = 9.322e-36j     # test complex
print("\ncomplex 9.322e-36j is a number? " + str(yi3func.is_numeric(value)))
#print("complex " + str(value) + " is a number? " + str(yi3func.is_numeric(value)))

value = -.6545+0J     # test complex
print("\ncomplex -.6545+0J is a number? " + str(yi3func.is_numeric(value)))
#print("complex " + str(value) + " is a number? " + str(yi3func.is_numeric(value)))


print("\n\n--------------------Program 2: assign_shape_params-----------------")
# 1: test unqualified values
print("Test assign_shape_params(\"triangle\",\"str1\",\"str2\")")
triangle = yi3func.assign_shape_params("triangle","str1","str2")
print triangle

print("\nTest assign_shape_params(\"triangle\",\"str1\",\"9\")")
triangle = yi3func.assign_shape_params("triangle","str1",9)
print triangle

print("\nTest assign_shape_params(\"triangle\",\"5\",\"str2\")")
triangle = yi3func.assign_shape_params("triangle",5,"str2")
print triangle

print("\nTest assign_shape_params(\"triangle\",\"-5\",\"9\")")
triangle = yi3func.assign_shape_params("triangle",-5,9)
print triangle

print("\nTest assign_shape_params(\"triangle\",\"5\",\"0\")")
triangle = yi3func.assign_shape_params("triangle",5,0)
print triangle

print("\nTest assign_shape_params(\"triangle\",\"-5\",\"-9\")")
triangle = yi3func.assign_shape_params("triangle",-5,-9)
print triangle

# 2: test qualified but different shape
print("\nTest assign_shape_params(\"triangle\",\"5\",\"9\")")
triangle = yi3func.assign_shape_params("triangle",5,9)
print triangle

print("\nTest assign_shape_params(\"rectangle\",\"5\",\"9\")")
rectangle = yi3func.assign_shape_params("rectangle",5,9)
print rectangle

print("\nTest assign_shape_params(\"circle\",\"5\",\"9\")")
circle = yi3func.assign_shape_params("circle",5,9)
print circle

print("\nTest assign_shape_params(\"square\",\"5\",\"9\")")
square = yi3func.assign_shape_params("square",5,9)
print square

print("\nTest assign_shape_params(\"pentagon\",\"5\",\"9\")")
pentagon = yi3func.assign_shape_params("pentagon",5,9)
print pentagon


print("\n\n--------------------Program 3: calc_shape_area---------------------")
# 1: test unqualified parameter
print "Test parameter is not dictionary "
print (yi3func.calc_shape_area(value))

print "\nTest shape is not recognized"
print (yi3func.calc_shape_area(pentagon)) 

# 2: test qualified value
print "\nArea of triangle is "
print (yi3func.calc_shape_area(triangle))  

print "\nArea of rectangle is "
print (yi3func.calc_shape_area(rectangle))  

print "\nArea of circle is "
print (yi3func.calc_shape_area(circle))  

print "\nArea of square is "
print (yi3func.calc_shape_area(square))


print("\n\n--------------------Program 5: scan,sort,write file------------------")
print("Sort files by size,and save filename which size < maxsize to a file.")
path = "X:\\class\\GIS578\\Lab3"
#path = "R:\\Geo578\\Students\\yih\\Lab3"
reg_exp = ".*\.py"  #??
maxsize = 7000L
output_file = "output.txt"
yi3func.sort_save(path,reg_exp,maxsize,output_file)


print("\n\n--------------------Program 11: find closest point from file-------")
print("find the closest point in a .csv file to a target point.")
path = "X:\\class\\GIS578\\Lab3"
#path = "R:\\Geo578\\Students\\yih\\Lab3"
filename = "coordinates.csv"
given_point = [0,0]
closest_point = yi3func.find_closest(path,filename,given_point)
if closest_point[0]:
    print("Point {0} is closest to target point {1}".format(closest_point[1],given_point))














