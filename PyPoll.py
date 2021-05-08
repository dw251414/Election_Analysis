# # Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("pyPollResources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:
#Don't forget the colon!
    # To do: read and analyze the data here.
#Remember that we found the reader function within the csv module that will read the CSV file.
 # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    #The variable, file_reader, is referencing the file object, which is stored in memory.
    #To "pull" the data out of the file object:
    #iterate through the file_reader variable and print each row, including the headers, or column names.
      # Print each row in the CSV file.
    # for row in file_reader:
    #     print(row)
    #Each row in the CSV file was printed out as a list.
#skip the header row of the CSV file, use the next() method.
    headers = next(file_reader)
    print(headers)