# # Add our dependencies.
import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("pyPollResources", "election_results.csv")

# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#To count up all the votes, we need to initialize a variable "accumulator"
#increment by 1 as we read each row in the for loop. 
#For convenience, we will initialize a variable called total_votes to zero.

# 1. Initialize a total vote counter.
total_votes = 0

#The total_votes variable needs to be placed above the code where we open the file, using the with open() statement. 
# We do this because every time we run the file, the total_votes variable must be set equal to zero.

# Open the election results and read the file
with open(file_to_load) as election_data:

#Remember that we found the reader function within the csv module that will read the CSV file.
#The variable, file_reader, is referencing the file object, which is stored in memory.
    file_reader = csv.reader(election_data)
  
    #skip the header row of the CSV file, use the next() method.
    headers = next(file_reader)

      #Each row in the CSV file was printed out as a list.
    print(headers)

#programmatically count up all the votes cast in the election by amending the code below the for loop.
#iterate through the file_reader variable and print each row, including the headers, or column names.
    for row in file_reader:

      #After we read the headers, we can iterate through each row and increment the total_votes variable by 1.
      #The standard Python format to increment a variable is number = number + 1, which can be augmented to number += 1.
       # 2. Add to the total vote count.
        total_votes += 1

# 3. Print the total votes.
print(total_votes)

#The total votes should be equal to the total number of rows in election_results.csv without the header: 369,711.
#The last row number in the CSV file is 369,712, which includes the header. 

