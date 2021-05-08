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

#Declare a new list, candidate_options = [] by adding it before the with open() statement in our script.
candidate_options = []

# 1. Declare the empty dictionary.
candidate_votes = {}

# Open the election results and read the file
with open(file_to_load) as election_data:

#Remember that we found the reader function within the csv module that will read the CSV file.
#The variable, file_reader, is referencing the file object, which is stored in memory.
    file_reader = csv.reader(election_data)
  
    #skip the header row of the CSV file, use the next() method.
    headers = next(file_reader)

      #Each row in the CSV file was printed out as a list.
   # print(headers)

#programmatically count up all the votes cast in the election by amending the code below the for loop.
#iterate through the file_reader variable and print each row, including the headers, or column names.
    for row in file_reader:

      #After we read the headers, we can iterate through each row and increment the total_votes variable by 1.
      #The standard Python format to increment a variable is number = number + 1, which can be augmented to number += 1.
       # 2. Add to the total vote count.
        total_votes += 1

# 3. Print the total votes.
#print(total_votes)

#The total votes should be equal to the total number of rows in election_results.csv without the header: 369,711.
#The last row number in the CSV file is 369,712, which includes the header. 

#iterate through the rows in the CSV file
#get the candidates from the "Candidate" column, and then add their names to a list.

#Add the following code to get the candidate's name from the row within the for loop.
        candidate_name = row[2]

#Inside the for loop, we will need to check if the candidate has been added to the candidate_options list.
        if candidate_name not in candidate_options:

        # Add the candidate_name to the candidate_options list using the append() method.
          candidate_options.append(candidate_name)

          # 2. Begin tracking that candidate's vote count.
          #we're setting each candidate's vote count to zero. 
          #Once we set it to zero, then we can start tallying the votes for each candidate.
          candidate_votes[candidate_name] = 0

#To increment each candidate's vote count every time their name appears in a row, 
#we need to move the vote counter inside the for loop and have it align with the if statement
          # Add a vote to that candidate's count
          #out of the if statement but aligned with the for loop
        candidate_votes[candidate_name] += 1

# # Print the candidate vote dictionary.
# print(candidate_votes)

#Add a print statement that is flush with the left margin to print out the candidate_options list
# print(candidate_options)

#To get the unique names in the candidate_options list, we can use an if statement with the not in membership operator to check if the candidate has been added to the list. 
# If the candidate's name has been added to the list, then the next time the candidate's name is found in a row using the for loop,
# it will not be added to the list.

 #Next is tocreate a dictionary where the key is each candidate's name and the vote count for that candidate is the value for the key.
###after first run <<add votes to each candidate. Using the Python format for incrementing variables, 
# we'll increment each candidate_votes[candidate_name] 
# every time that name appears while we are iterating through each row.

##next task is to calculate the percentage of votes for each candidate. 
#This means we need to divide the candidate's vote count by the total vote count, and then multiply by 100. 
# Here's the equation: vote_percentage = (votes / total_votes) * 100

# Determine the percentage of votes for each candidate by looping through the counts.

#Use a for loop to iterate through the candidate_options = [] list. We will get the candidate's name.
# 1. Iterate through the candidate list.
for candidate_name in candidate_votes:

#Use the for loop variable to retrieve the votes of the candidate from the candidate_votes = {} dictionary.
    # 2. Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]

#Calculate the percentage of the vote count.
    # 3. Calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100

#Print each candidate and the percentage of votes using f-string formatting.
    # 4. Print the candidate name and percentage of votes.
    print(f"{candidate_name}: received {vote_percentage:.2f}% of the vote.")