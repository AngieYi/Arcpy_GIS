# GEO 578:  yih_lab3_functions.py
# Purpose:  define functions used to learn concepts
# Author: Hongyan Yi


import os
import math
import re


# function: name_math
# Purpose: Calculate the product of the length of first and last name 
# Inputs: one string with one "_" in it, before _ is first name while after is last name
# Outputs: product of the length of first and last name

def is_numeric(value): # write if in two lines, keep before red line(python style)
    if(type(value) == float or type(value) == int
       or type(value) == long or type(value) == complex):
        return True
    else:
        return False
    
    

# function: assign_shape_params
# Purpose: judge whether input parameters are qualified, if yes,return a
#          dictionary of these parameters, if not print specific reasons.
# Inputs: shapename(string), dimension1(numeric), dimension2(numeric)
# Outputs: the dictionary type of these three parameters

def assign_shape_params(shapename,dim1,dim2):
    if is_numeric(dim1) and is_numeric(dim2):
        if dim1>0 and dim2>0:
            if shapename == 'rectangle':
                return {"shapename": shapename, "length": dim1, "width": dim2}  
            
            elif shapename == 'triangle': 
                d={"shapename":shapename, "length": dim1, "width": dim2}
                return d    # return dictionary
               
            elif shapename == 'circle': 
                return {"shapename": shapename, "radius": dim1}  
               
            elif shapename == 'square': 
                return {"shapename": shapename, "length": dim1} 
             
            else:   # return empty dictionary
                print(shapename + " is not a recognized shape.")
                return  {"shapename": 'NA', "length": -1, "width": -1}  
        if dim1 <= 0:
            print "Error: " + str(dim1) + " <= 0."
        if dim2 <= 0:           # no elif, otherwise dim1<=0&&dim2<=0, only print dim1
            print "Error: " + str(dim2) + " <= 0." 
    if not is_numeric(dim1):
        print "Error: " + str(dim1) + " is not numeric."
    if not is_numeric(dim2):    # no elif, otherwise,dim1&&dim2 not numeric,only print dim1
        print "Error: " + str(dim2) + " is not numeric."


# function: calc_shape_area
# Purpose: calculate the area of the shape, check whether input is a dictionary,
#          whether there is shapename key, and when the shape is not recognized  
# Inputs: a dictionary including shapename(string), dimension1(numeric), dimension2(numeric)
# Outputs: area of the shape, or None(smoonthly end)

def calc_shape_area(shape_dic): 
    if type(shape_dic) != dict: #check to see if shape is actually a dictionary type!
        print("The parameter type is not a dictionary")
        return None  # return a signal that function finished correctly
    
    try:
        shape_dic['shapename']
    except:
        print("This object does not have a 'shapename' key")
        return None     # return a signal that function finished correctly
    
    if shape_dic['shapename'] == 'triangle':
        try:
            area = 0.5 * shape_dic['length'] * shape_dic['width']
            return area
        except:
            print("The triangle does not have appropriate length or width")
            return None     # return a signal that function finished correctly
        
    elif shape_dic['shapename'] == 'rectangle':
        try:
            area = shape_dic['length'] * shape_dic['width']
            return area
        except:
            print("The rectangle does not have appropriate length or width")
            return None 
        
    elif shape_dic['shapename'] == 'circle':
        try:
            area = math.pi * math.pow(shape_dic['radius'],2)
            return area
        except:
            print("The circle does not have appropriate radius")
            return None 
        
    elif shape_dic['shapename'] == 'square':
        try:
            area = math.pow(shape_dic['length'],2)
            return area
        except:
            print("The square does not have appropriate length")
            return None 
        
    else:
        print(shape_dic['shapename'] + ' is not a recognized shape')
            


# Function: find the Euclidean distance between two points
# Purpose: use math.sqrt
# Inputs: two lists, each list is a 2D point coordinates
# Outputs: the euclidean distance of the two points

def euclidean_distance(arg1,arg2):
    x1 = arg1[0]
    x2 = arg2[0]
    y1 = arg1[1]
    y2 = arg2[1]
    distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)   # math.sqrt(x): Return the square root of x.
    return distance



# Function: check whether the file is in the path
# Purpose: use os.path.join to handle delimiter and os.path.isfile to check file existing
# Inputs: path and filename
# Outputs: tuple: False,None or True,full_filename

def check_filename(path, filename):
    try:
        full_filename = os.path.join(path, filename) # if we pass nonsense to the os., it will still crash,so try-except
    except IOError as e: #???
        print("Error in check filename:  Problem with either the path or the filename")        
        print("I/O error {0}: {1}".format(e.errno, e.strerror)) #???
        return False, None
    except:     # set up multiple except to handle different exceptions
        print("Error in check filename:  Undetermined.")
        return False, None

    if os.path.isfile(full_filename): # check whether the file exist
        return True, full_filename
    else: 
        print("Error in check filename: The file does not exist")
        return False, None    # here use None after False to keep consistant
    


# Function: find the closest point in a file to a target point
# Purpose: use open(file)
# Inputs: file path, filename,target_point
# Outputs: the closest point to the target point

def find_closest(path,filename,target_point):
    print("Directory = %s" %(path))
    print("filename = %s" %(filename))
    print("target_point = " + str(target_point))
    test = check_filename(path,filename)
    if test[0]:
        full_filename = test[1]
        try:
            file_read_object = open(full_filename)
            str_list = []
            points_list = []
            for line in file_read_object:
                line = line[:-1]            # to ignore the '\n' at the end of each line
                str_list = line.split(',')
                x = float(str_list[0])
                y = float(str_list[1])
                points_list.append([x,y])   # append each point to the list
        except:
            print("Error: put file content to list error.")
            file_read_object.close()        # ensure file closed after using in any situation
            return False,None
        file_read_object.close()        # ensure file closed after using in any situation

        try:
            min_distance = euclidean_distance(points_list[0],target_point)    # initilize value
            for point in points_list:
                temp_distance = euclidean_distance(point,target_point)
                if(temp_distance < min_distance):
                    min_distance = temp_distance
                    min_point = point
            return True,min_point
        except:
            print("Error: calculate minimum distance error.")
            return False,None




# Function: find files meets regular expression within the path
# Purpose: use os.listdir and re.match
# Inputs: full path and regular expression
# Outputs: tuple: False,None or True,filename list

def find_files(path, reg_exp):
    # step1: get all files in the directory
    try:
        files = os.listdir(path)
    except:
        print("Error in find_files: Path did not appear to work")
        print("The path used was:")
        print path
        return False, None

    # step2: loop to check if each file meet the regular expression
    matchlist = []
    for file in files:
        if (re.match(reg_exp, file)):
            matchlist.append(file)

    if len(matchlist) != 0:  return True, matchlist
    else: return False, None
        


   
# Function: sort files according to size,and save filename to a file whose size less than the maxsize
# Purpose: learn to use os.path.getsize, list.sort,and file.write
# Inputs: directory,reg_exp,maxsize,output_file
# Outputs: False,True
    
def sort_save(directory,reg_exp,maxsize,output_file):
    # 1: find files of a certain type(.py) in a giving directory
    print("Directory = %s" %(directory))
    print("Regular expression = %s" %(reg_exp))
    match_list = find_files(directory,reg_exp) # find files that match regular expression

    if not (match_list[0]):
        print("There is no file match regular expression")
        return

    # 2: sorts them by size
    sort_result_list = []
    specific_result_list = []
    try:
        for filename in match_list[1]:
            full_filename = os.path.join(directory,filename) # get the full filename(including path) of the file
            size = os.path.getsize(full_filename)   # get the size of each file
            sort_result_list.append((filename,size))   # append a tuple, save only filename and size to list of tuples.

        print "\nFilename and size before sorting are:"
        for file_list in sort_result_list:
            print file_list

        sort_result_list.sort(key = lambda s:s[1])  # sort the list according to file size

        print "\nFilename and size after sorting by size are:"
        for file_list in sort_result_list:
            print file_list
    except:
        print("\nError: getting file size or sorting errors.")
        return False

    # 3: find specific files that meet some requirement
    for sort_result in sort_result_list:
        if sort_result[1] < maxsize:    # requirement
            specific_result_list.append(sort_result[0]) # only append filename
    if specific_result_list.count < 1:
        print("\nThere is no file that size < " + str(maxsize))
        return  # directly return to call function when there's no file meet requirement
    print("\nFilename and size that size < " +str(maxsize))
    print specific_result_list

    # 4: write specific file names to another file
    print("\nOutput file that size < " + str(maxsize) + " to " + output_file)
    try:
        out_full_path = os.path.join(directory,output_file)
        try:
            file_write_object = open(out_full_path,'w')
            for line in specific_result_list:
                file_write_object.writelines(line + '\n')
            file_write_object.close()
        except:
            print("Error: write file error.")
            file_write_object.close()
            return False
    except IOError as e:
        print("Problem with either the path or the filename")
        print("I/O error {0}: {1}".format(e.errno, e.strerror))
        return False
    
    
            
            
    
    
    