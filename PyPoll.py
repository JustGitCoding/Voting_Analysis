import csv

#path to input and output files
file_to_load = 'resources/election_results.csv'
file_to_save = 'Analysis/voting_analysis.txt'

#initialize vote counter (has to be before we open the file because we want the count to be 0 each time we run the program)
total_votes = 0

#initialize county and candidate options list + dictionary to hold each votes by county & by candidate
candidate_options = []
candidate_votes = {}
county_options = []
county_votes = {}
county_candidate_pairs = []
county_candidate_votes = {}

#declare variables for winner
winner = ""
winning_count = 0
winning_percentage = 0

#declare variables for county data
top_county = ""
winning_turnout = 0

#declare variable for pair data
county_winner = ""
county_winning_count = 0

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
        county_name = row[1]
        county_candidate_choice = (row[1],row[2])
        #append non-duplicating names to candidate options list & start vote count for that candidate at 0
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name] = 0

        #tally votes for each candidate
        candidate_votes[candidate_name] += 1

        #append non-duplicating names to county options list & start vote count for that county at 0
        if county_name not in county_options:
            county_options.append(county_name)
            county_votes[county_name] = 0

        #tally votes for each county
        county_votes[county_name] += 1

        #FURTHER INSIGHTS - append non-duplicating county/candidate pairs & start vote count for each pair at 0
        if county_candidate_choice not in county_candidate_pairs:
            county_candidate_pairs.append(county_candidate_choice)
            county_candidate_votes[county_candidate_choice] = 0
        
        #FURTHER INSIGHTS - tally votes per candidate per county
        county_candidate_votes[county_candidate_choice] += 1

#save results into text file instead of printing
with open(file_to_save,"w") as txt_file:
    election_results = (
        f"\nElection results\n"
        f"----------------------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"----------------------------------------\n"
        f"County Votes:\n")
    print(election_results,end="")
    txt_file.write(election_results)
    
    #summarize county stats
    for county_name in county_votes:
        covotes = county_votes[county_name]
        covote_percentage = float(covotes / total_votes) * 100
        county_result = (f"{county_name}: {covote_percentage:.1f}% ({covotes:,})\n")
        print(county_result,end="")
        txt_file.write(county_result)

        #determine county with largest turnout
        if covotes > winning_turnout:
            winning_turnout = covotes
            top_county = county_name

    #print county with largest turnout
    participation_summary = (
        f"----------------------------------------\n"
        f"Largest County Turnout: {top_county}\n"
        f"----------------------------------------\n")
    print(participation_summary,end="")
    txt_file.write(participation_summary)

    #summarize candidate stats
    for candidate_name in candidate_votes:
        canvotes = candidate_votes[candidate_name]
        canvote_percentage = float(canvotes / total_votes) * 100
        candidate_result = (f"{candidate_name}: {canvote_percentage:.1f}% ({canvotes:,})\n")
        print(candidate_result,end="")
        txt_file.write(candidate_result)


        #determine winner based on popular vote
        if canvotes > winning_count and canvote_percentage > winning_percentage:
            winning_count = canvotes
            winning_percentage = canvote_percentage
            winner = candidate_name

    #print winning candidate's results into terminal
    winner_summary = (
        f"----------------------------------------\n"
        f"Winner: {winner}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"----------------------------------------\n"
        f"Further Insights:\n"
        f"----------------------------------------\n")
    print(winner_summary, end="")
    txt_file.write(winner_summary)

    #FURTHER INSIGHTS - determine candidate preference by county
    for pair in county_candidate_votes:
        pvotes = county_candidate_votes[pair]
        pair_result = (f"{pair[0]} County votes for {pair[1]}: {pvotes:,}\n")
        # print(pair_result,end="")
        # txt_file.write(pair_result)
    
    for county in county_options:
        for candidate in candidate_options:
            ccvotes = county_candidate_votes[county,candidate]
            if ccvotes > county_winning_count:
                county_winning_count = county_candidate_votes[county,candidate]
                county_winner = candidate
            county_win_percentage = float(county_candidate_votes[county,county_winner] / county_votes[county]) * 100
        further_insights = (f"The popular vote in {county} County went to {county_winner} with {county_win_percentage:.1f}% ({county_candidate_votes[county,county_winner]:,}) of the votes cast in {county} county.\n")
        print(further_insights,end="")
        txt_file.write(further_insights)

