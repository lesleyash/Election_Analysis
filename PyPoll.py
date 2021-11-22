import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Open the election results and read the file.
#Write down the names of all the candidates.
total_votes=0
candidate_options =[]
candidate_votes={}
winning_candidate=""
winning_count=0
winning_percentage=0
with open(file_to_load) as election_data:
    file_reader=csv.reader(election_data)
    headers = next(file_reader)
   #Add a vote count for each candidate.
    for row in file_reader:
        total_votes +=1
        candidate_name=row[2]
        #Get the total votes for each candidate.
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)
            candidate_votes[candidate_name]=0
        candidate_votes[candidate_name] +=1
    #Get the results of election
    for candidate_name in candidate_votes:
        votes=candidate_votes[candidate_name]
        vote_percentage=float(votes)/float(total_votes)*100
        if votes>winning_count and vote_percentage>winning_percentage:
            winning_count=votes
            winning_percentage=vote_percentage
            winning_candidate=candidate_name
        print(f'{candidate_name}: received {vote_percentage}% of the vote\n')
    print(f'The winning candidate is {winning_candidate} with {winning_count} votes / {winning_percentage}%\n')      
print('The total votes of the election is {total_votes}\n')


          
        

