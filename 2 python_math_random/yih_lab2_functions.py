# GEO 578:  yih_lab2_functions.py
# Purpose:  define functions used to learn concepts in week2
# Author: Hongyan Yi

# import modules
import math
from random import random

def name_math(arg1):
    # function:  name_math()
    # Purpose: Calculate the product of the length of first and last name 
    # Inputs: one string with one "_" in it, before _ is first name while after is last name
    # Outputs: product of the length of first and last name
    
    split_list = str.split(arg1,"_")        # split str with _, return a list
    len_first = len(split_list[0])          # 1st item of the list is first name
    len_last = len(split_list[1])           # 2nd item of the list is last name
    product_value = len_first * len_last    # product of the length of first and last name 
    return product_value


def Latitude_math(arg1):
    # function:  Latitude_math()
    # Purpose: accepts a three element list of [degrees, minutes, seconds] and converts it to a single decimal degree value.
    # Inputs: a three element list
    # Outputs: a single decimal degree value
    
    sec_to_min = arg1[2]/60.                    # convert the 3rd element to minute: 60 seconds = 1 minute
    min_to_deg = (arg1[1] + sec_to_min)/60.     # convert the 2nd and 3rd elements to degree: 60 minutes = 1 degree
    final_deg = arg1[0] + min_to_deg            # add 3 elements together
    return final_deg

    
    
def filename_iteration(arg1):
    # function: Filename iteration generator
    # Purpose: generate variants for file name by adding different numbers in the file name
    # Inputs: a string of filename with extension
    # Outputs: a list of filename variants    
    
    filename_list = str.split(arg1,".")     # split the filename and extension
    filename = filename_list[0]
    extension = filename_list[1]
    tail = "m" + "." + extension            # fix the tail string
    filename_variant_list = []              # inital a empty list so that could append others when doing loop
    
    num_list = range(100,1100,100)          # range(start, stop[, step])
    for i in num_list:
        filename_variant_list.append(filename + str(i) + tail)  # Add an item to the end of the list; Here the item is a string
        
    return filename_variant_list


def euclidean_distance(arg1,arg2):
    # Function: find the Euclidean distance between two points
    # Purpose: use math.sqrt
    # Inputs: two lists, each list is a 2D point coordinates 
    # Outputs: the euclidean distance of the two points
    
    x1 = arg1[0]
    x2 = arg2[0]
    y1 = arg1[1]
    y2 = arg2[1]
    distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)   # math.sqrt(x): Return the square root of x.
    return distance


def random_points(num_random_points,upleft_coords,lowright_coords):
    # Function: generates a list of random samples within a coordinate box defined by the user.
    # Inputs: number of samples desired; upper left corner point coordinates; lower right corner point coordinates;
    # Outputs: a list of [x,y] coordinate
    
    x1 = upleft_coords[0]
    y1 = upleft_coords[1]
    x2 = lowright_coords[0]
    y2 = lowright_coords[1]
    coordinate_list = []        
    for i in range(num_random_points):
        p = random()                        # a random number between 0 and 1.0
        x = p * x1 + (1-p) * x2
        y = p * y1 + (1-p) * y2
        point_list = [x,y]                  # point between p1 and p2
        coordinate_list.append(point_list)  # append the points to list
    return coordinate_list
    



        
        
    
    
            
    