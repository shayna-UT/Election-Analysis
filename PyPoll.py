# 1. Add our dependencies: Import csv and os modules
#    os module allows us to interact with our operating system
import csv
import os 

# 2. Create a filename variable to load a file from a path
#    os.path allows us to access files on different operating systems
#    join() function joins our file components together
file_to_load = os.path.join("Resources", "election_results.csv")
# 3. Create a filename variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 4a. Initialize a vote couter 
total_votes = 0
# 4b. Declare an empty candidate list
candidate_options = []
# 4c. Declare an empty dictionary: key is each candidate's name and value is vote count for the candidate
candidate_votes = {}
# 4d. Declare a variable that holds an empty string value for the winning candidate 
winning_candidate = ""
# 4e. Declare a variable for the "winning count" equal to zero
winning_count = 0 
# 4f. Declare a variable for the "winning percentage" equal to zero
winning_percentage = 0

#    Open election results and read the file
#    Use with statement to open the file and ensure proper acquisition/ release of data w/out having to close file
with open(file_to_load) as election_data:
#   5a. Print the file object 
    #print(election_data)
#   5b. Read the file object with the reader function
    file_reader = csv.reader(election_data)
#   5c. Read and print the header row 
    headers = next(file_reader)
    #print(headers)
#   6. For each row in the csv file,
    for row in file_reader:
#       6a. Add to the total vote count 
        total_votes += 1
#       6b. Print candidate name from each row in column C (list index [2])
        candidate_name = row[2]
#           6c. If candidate does not match an existing candidate
        if candidate_name not in candidate_options:
#           Add name to candidate list 
            candidate_options.append(candidate_name)
#           And create each candidate as a key to begin tracking candidate's vote count
            candidate_votes[candidate_name] = 0
#       6d. Add total # of votes each candidate won
#       Move vote counter out of if statement but aligned with for loop
        candidate_votes[candidate_name] += 1

#    Save the results to our text file 
with open(file_to_save, "w") as txt_file:
    # 7a. Print the final vote count
    election_results = (
    f"\nElection Results\n"
    f"-------------------------\n"
    f"Total Votes: {total_votes:,}\n"
    f"-------------------------\n")
    print(election_results, end="")
    # 7b. Save the final vote count to the text file 
    txt_file.write(election_results)

    # 8-10. Determine the % of votes for each candidate and the winning candidate 
    #   Iterate through the candidate list
    for candidate in candidate_votes:
    #   8a. Retrieve vote count of candidate 
        votes = candidate_votes[candidate]
    #   8b. Calculate % of votes for candidate 
        vote_percentage = int(votes) / int(total_votes) * 100
    #   8c. Print candidate name and % of votes
        #print(f"{candidate}: received {vote_percentage: .1f}% of the vote.")

    #   9. Print each candidate's name, vote count, and % of votes
        candidate_results = (f"{candidate}: {vote_percentage: .1f}% ({votes: ,} )\n")
        print(candidate_results)
        txt_file.write(candidate_results)

    #   10. Determine winning vote count and candidate
    #   If the votes is greater than the winning count and vote percentage greater than winning percentage, 
        if(votes > winning_count) and (vote_percentage > winning_percentage):
    #       10a. Set winning count to votes
            winning_count = votes
    #       10b. Set winning percentage to vote_percentage
            winning_percentage = vote_percentage
    #       10c. Set winning candidate equal to candidate
            winning_candidate = candidate

    # 11. Print the winning candidate, vote count, and percentage then save to text file
    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count: ,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)

    # 12. Additional Print Options
    # 12a. Print the total votes: equal to total # of rows in csv file w/out header 
    #print(total_votes)
    # 12b. Print the candidate list
    #print(candidate_options)
    # 12c. Print the candidate vote dictionary 
    #print(candidate_votes)