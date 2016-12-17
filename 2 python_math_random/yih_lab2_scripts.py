# GEO 578:  yih_lab2_scripts.py
# Purpose:  Illustrate scripts to call the functions in 
#           "yih_lab2_functions.py"
# Author: Hongyan Yi
#

# HOW TO USE THIS FILE:
# The purpose of this file is to show to call functions 
# that are defined in the yih_lab2_functions.py


# import the file with the functions defined
import yih_lab2_functions as yifunc



# user should first input your first and last name according to hint,then it will call function name_maththe
# which calculates the product of the length of first and last name, and return the value and show out 
print("\n----------------Name math----------------")

first_name = raw_input("Enter your firstname:")
last_name = raw_input("Enter your lastname:")
single_str = first_name + "_" + last_name

#single_str = "hongyan_yi"
num_len = yifunc.name_math(single_str)          # call name_math(arg1)
print("Product of the length of first and last name: "+ str(num_len))



# user should first input three variables according to hint,then it will call function Latitude_maththe
# which converts them to a single decimal degree value, and return the value and show out
print("\n----------------Latitude math----------------")
while True:
    num_degree = float(raw_input("Enter value of degree(0<=degree<=90):"))  # input three elements and use float() to change default string to float
    num_minutes = float(raw_input("Enter value of minutes:"))
    num_seconds = float(raw_input("Enter value of seconds:"))
    if(num_degree>=0 and num_degree<=90):                                   # only when num_degree match requirments, then call Latitude_math(arg1)
        list_nums = [num_degree,num_minutes,num_seconds]                    # directly put 3 variables to list.
        num_convert = yifunc.Latitude_math(list_nums)                       # call Latitude_math(arg1)       
        print("These elements convert to a single decimal degree is "+str(num_convert))
        break                                                               # only in this situation, stop loop
    else:
        print("Your degree is not 0<=degree<=90, Try again.")               # use while-True if-break-else to let user input correctly

        
# call and show function filename_iteration
print("\n----------------Filename iteration generator----------------")
filename = "filename.img"                   # Input is a string of filename with extension
print("The filename is: " + filename)
print("The filename iterations are: ")
print yifunc.filename_iteration(filename)   # call filename_iteration(arg1)


# call and show function euclidean_distance
print("\n----------------Euclidean distance between two points----------------")
p1_list = [0,0]                                                 # coordinate of point1[x1,y1]
p2_list = [1,1]                                                 # coordinate of point2[x2,y2]
print("The coordinate of point1 is: " + str(p1_list))           # print list   
print("The coordinate of point2 is: " + str(p2_list))
euc_distance_2p = yifunc.euclidean_distance(p1_list, p2_list)   # input two lists,each list is a 2D point coordinates
print("The Euclidean distance of point1 and point2 is: " + str(euc_distance_2p)) # return a number, use str(num) to print it


# call and show function random_points
print("\n----------------Random points----------------")
num_random_points = 3       # number of samples desired;
upleft_coords = [1,4]       # upper left corner point coordinates;
lowright_coords = [4,1]     # lower right corner point coordinates;
points_list = yifunc.random_points(num_random_points,upleft_coords,lowright_coords)

print("The upper left corner point is: " + str(upleft_coords))
print("The lower right corner point is: " + str(lowright_coords))
print("The %d random sample points: " %(num_random_points))
print points_list



