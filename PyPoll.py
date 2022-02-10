import csv
import os


#assign data variable

#DIRECT PATH
# from pathlib import Path
# file_to_load = Path('Resources\\election_results.csv')
# file_to_load = Path('Resources\\election_results.csv')
# file_to_load = 'Resources\\election_results.csv'
# file_to_load = 'resources/election_results.csv'

#INDIRECT PATH
#assign a variable to LOAD a file FROM a path
file_to_load = os.path.join("Resources","election_results.csv")
#assign a variable to SAVE the file TO a path
file_to_save = os.path.join("analysis","voting_analysis.txt")


# election_data = open(file_to_load,'r')
# #perform analysis here - but you have to close file afterwards or risk losing data in "buffer"
# election_data.close()

# #open election results and read file
# with open(file_to_load) as election_data:
#     #perform analysis here (we wont' have to close file afterwards since we are using the 'with' statement)
#     print(election_data)

# outfile = open(file_to_save,"w")
# outfile.write("Hello World")
# outfile.close()

# with open(file_to_save,'w') as txt_file:
#     txt_file.write("Counties in the Election\n---------------------------\n")
#     txt_file.write("Arapahoe\nDenver\nJefferson")

#initialize vote counter (has to be before we open the file because we want the count to be 0 each time we run the program)
total_votes = 0

#initialize candidate options list + dictionary to hold each candidate's votes
candidate_options = []
candidate_votes = {}

#declare variables for winner
winner = ""
winning_count = 0
winning_percentage = 0

#read the file object with reader function
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    
    #'next' method will "read" the header row
    headers = next(file_reader)

    #print each row in the CSV file
    for row in file_reader:
        total_votes += 1

        #get candidate name from each row
        candidate_name = row[2]
        #append non-duplicating names to candidate options list & start vote count for that candidate at 0
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0
        #tally votes for each candidate
        candidate_votes[candidate_name] += 1

    # #total number of votes cast
    # print("Total vote count: ",total_votes)

    # #list of candidates + total votes per candidate
    # print(candidate_votes)

#save results into text file instead of printing
with open(file_to_save,"w") as txt_file:
    election_results = (
        f"\nElection results\n"
        f"---------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"---------------------------\n")
    print(election_results,end="")
    txt_file.write(election_results)

    #calc percentage of votes per candidate
    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes / total_votes) * 100
        # print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        #determine winner based on popular vote
        if votes > winning_count and vote_percentage > winning_percentage:
            winning_count = votes
            winning_percentage = vote_percentage
            winner = candidate_name

    #print winning candidate's results into terminal
    winner_summary = (
        f"------------------------------\n"
        f"Winner: {winner}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"------------------------------\n")
    # print(winner_summary)

