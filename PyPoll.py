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
file_to_load = os.path.join("Resources","election_results.csv")
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

with open(file_to_save,'w') as txt_file:
    txt_file.write("Counties in the Election\n----------------------------\n")
    txt_file.write("Arapahoe\nDenver\nJefferson")

#read the file object with reader function
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # for row in file_reader:
    #     print(row)
    headers = next(file_reader)
    print(headers)



#total number of votes cast

#complete list of candidates who received votes

#percentage of votes per candidate

#total number of votes each candidate won

#winner of election based on popular vote
