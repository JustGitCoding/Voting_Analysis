# Voting Analysis - Election Audit

## Overview of Election Audit
The purpose of this project is to audit the county election results in Colorado. To do this, we wrote a python program to systematically tally up the votes by county and by candidate, and simultaneously write this information into an output .txt file.

Steps performed include:
1. Calculating total number of votes cast
2. Compiling a list of candidates who received votes
3. Tallying the total votes for each candidiate
4. Calculating each candidate's percentage of total votes
5. Determining the election winner based on popular vote

## Resources
- Data Source: election_results.csv
- Software: Python 3.7.6, Visual Studio Code 1.64.1

## Results Summary
The analysis of the election showed showed that:
- There were 369,711 votes cast in the election.
- There votes were distributed into the following geographical regions:
    - Jefferson County: 10.5% (38,855)
    - Denver County: 82.8% (306,055)
    - Arapahoe County: 6.7% (24,801)
        - The county with the highest turnout was Denver County
- The Candidate results were:
    - Charles Casper Stockham: 23.0% (85,213)
    - Diana DeGette: 73.8% (272,892)
    - Raymon Anthony Doane: 3.1% (11,606)
        - The winner of the election is Diana DeGette with 73.8% (272,892) of the total votes that were cast.
            - Diana DeGette received the popular vote in Denver and Arapahoe counties, while Charles Casper Stockham won the popular vote in Jefferson County.

## Business proposal
The analysis above was generated through a python script which can be re-purposed for any future election audits with only a few minor modifications:
1. You'll need to update the script to let Python know where your raw data (.csv file) is saved on your hard drive. For example, in the snippet below, the blue text would need to be updated.
```python
    file_to_load = 'resources/election_results.csv'
```
2. Depending on how the data is formatted in the new .csv file, you may need to update the following section of code, so that you are pulling from the appropriate "columns" in the data. This is done by updating the index number between each square bracket.
```python
    candidate_name = row[2]
    county_name = row[1]
    county_candidate_choice = (row[1],row[2])
```
