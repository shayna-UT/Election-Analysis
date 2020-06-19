# 1. Import csv and os modules
#    os module allows us to interact with our operating system
import csv
import os 

# 2. Create a filename variable to load a file from a path
#    os.path allows us to access files on different operating systems
#    join() function joins our file components together
file_to_load = os.path.join("Resources", "election_results.csv")
# 3. Create a filename variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 4. Open election results and read the file  
#    Use with statement to open the file and ensure proper acquisition/ release of data w/out having to close file
with open(file_to_load) as election_data:
#   Print the file object 
    print(election_data)
#   Read the file object with the reader function
    file_reader = csv.reader(election_data)
#   Read and print the header row 
    headers = next(file_reader)
    print(headers)

# 5. Use with statement to open file as a text file
with open(file_to_save, "w") as txt_file:
#   Write data to the file
    txt_file.write("Counties in the Election\n------------------------\nArapahoe\nDenver\nJefferson")


# The data we need to retrieve:
# 1. The total number of votes cast
# 2. A complete list of candidates who receieved votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote 