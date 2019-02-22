import csv
import glob
import re
import os


#this is how to read in an csv file. You can make most excel file csv's if you simply
#go to save as, and save the file with the csv (comma seperated values extension)

# RevistionTest.csv is the name of the file. If you want to simply use the file name without having to use the absolute
# path simply place it in the same directory as your .py file 
with open('RevistionTest.csv', 'r') as f: #opens the file with read permissions. 
    reader = csv.reader(f)
    data = list(list(rec) for rec in csv.reader(f, delimiter=',')) #data is now a list of lists
    f.close() 
file  = open("testfileRevision.txt","w") #this opens a new or existing file with write permissions

file.write(str(data)) # This is how you would write the whole list of lists to a txt file

file1  = open("testfileRevision.txt","w") #this opens a new or existing file with write permissions

 # This is how you would iterate through the list of lists
 # Each row is a new list. So if you wanted to access the first row [0] and the second column [1] in the variable data[][] 
 # You would do so like data[0][1] as so on. 
 # The following code prints out only the second column of each row in the list of lists object "data"
for i, outer in enumerate(data):
    print(data[i][1]) 
    # This writes on the second column of each row to the file1 ("testfileRevision.txt")
	# notice you must cast to a string as .txt files will only accept strings. 
	file1.write(str(data[i][1])
file.close()
file1.close()
     