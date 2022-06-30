# The data we need to retrieve
# 1. The total number of votes cast. 
# 2. A complete list of candidates who recieved votes.
# 3. The percentage of votes each candidate won. 
# 4. The total number of vote each candidate won. 
# 5. The winner of the election based on popular vote.

import csv
import os 

#Assign a variable for the file to load and the path. 
file_to_load = os.path.join("Resources" , "election_results.csv")
#Assign a variable to save the file to a path
file_to_save = os.path.join("/Users/owner/Desktop/Analysis_Projects/Election-Analysis/Module-3-Assignment/election_analysis.txt")

# 1.Initalize the total vote counter 
total_votes = 0 

#Candidate Options
candidate_options = []

# Declare the empty dictionary. 
candidate_votes = {}

#Winning Candidate and Winning Count Tracker
winning_candidate = " " 
winning_count = 0 
winning_percentage = 0

#Open the election results and read the file
#election_data = open(file_to_load, 'r')
with open(file_to_load) as election_data: 


    #To do: read and analyze data here. 
    file_reader = csv.reader(election_data)

    #Read the header row. 
    headers = next(file_reader) 
    

    #Print each row in the CSV file
    for row in file_reader: 
        
        # Add to the total vote count
        total_votes = total_votes + 1

        #Print the candidate name from each row. 
        candidate_name = row[2]

        #If the candidate does not match any existing candidate. 
        if candidate_name not in candidate_options: 
            #Add it to the list of candidates 
            candidate_options.append(candidate_name)

            # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0 
       
        #Add a vote to that candidates count
        candidate_votes[candidate_name] += 1
    #Save the results to our text file.     
with open(file_to_save, "w") as txt_file: 
    election_results = (
            f"\nElection Results\n"
            f"---------------------\n"
            f"Total Votes: {total_votes: ,}\n"
            f"---------------------\n"

            )
        #Print each candidate, their voter count, and percentage to the terminal
    print(election_results, end = "")
        #Save the final vote count to the text file. 
    txt_file.write(election_results)

            

        #Add the candidate's name to the candidate list. 
        #candidate_options.append(candidate_name)

        #print(row)

#Print the candidate vote dictionary. 
#print(candidate_votes)



# Determine the percentage of votes for each candidate by looping
# through the counts. 
# 1. Iterate through the candidate list. 

for candidate_name in candidate_votes: 
    
   


    # 2. Retrieve the vote count of a candidate. 
    votes = candidate_votes[candidate_name]

    # 3. Calculate the percentage of votes. 
    vote_percentage = float(votes)/float(total_votes) * 100 

    # 4. Print the candidate name and percentage of votes. 
    with open(file_to_save, "w") as txt_file: 
        candidate_results = (f"{candidate_name}: recieved {vote_percentage: .1f}% of the vote. ")
        print(candidate_results)
        txt_file.write(candidate_results)
    
# To do: print out each candidates name, vote count, and 
# percentage of votes to the terminal.
#


# Determine winning vote count and candidate
#Determine if the winning vote is greater than the winning count. 
#Determine winning vote count and candidate
        # 1. Determine if the votes are greater than the winning count. 
   # print(f"{candidate_name}: {vote_percentage:.1f}% ({votes: ,})\n")            
    if (votes > winning_count) and (vote_percentage > winning_percentage): 
        # 2. If true then set winning_count = votes and winning_percent = vote percentage 
         winning_count = votes 
         winning_percentage = vote_percentage


    # 3. Set the winning candidate equal to the candidates name
         winning_candidate = candidate_name 
       

#To do: print out the winning candidate, vote count, and 
#percentage to terminal. 

    

winning_candidate_summary = ( 
    f"----------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage: .1f}% \n"
    f"-----------------------\n"
)

with open(file_to_save, "w") as txt_file:
    election_results = (
        f"\nElection Results\n"
        f"---------------------\n"
        f"Total Votes: {total_votes: ,}\n"
        f"---------------------\n"

        )
    candidate_results = (f"{candidate_name}: recieved {vote_percentage: .1f}% of the vote. ")
    print(candidate_results)
    txt_file.write(candidate_results)    

    print(winning_candidate_summary)
    #Save the winning candidates name to the text file. 
    txt_file.write(winning_candidate_summary)


    













#Print the candidate list.
#print(candidate_options)

# 3. Print the total votes. 
#print(total_votes)







#To do: perform analysis
















   # print(election_data)

#Close the file
#election_data.close()

# Create a filename variable to a direct or indirect path to the file. 


#file_to_save = os.path.join("analysis", "election_results.txt")

#Using the open() function with the "w" mode we will write data to the file. 
#outfile = open(file_to_save, "w")
#Using the with statement, open the file as a text file. 
#with open(file_to_save, "w") as txt_file: 

    #Write some data to the file. 
    #txt_file.write("Hello World \n")

    #Write three counties to the file. 
    #txt_file.write("Counties in the Election\n")
    #txt_file.write("------------------------\n")

    #txt_file.write("Arapahoe\nDenver\nJefferson")

#Write some data to the file
#outfile.write("Hello World")

#Close the file
#outfile.close()