import csv
import os

file_to_load = os.path.join("Resources", "election_data.csv")
file_to_output = os.path.join("Analysis", "election_analysis.txt")

# initialize
total_votes = 0
candidate_votes = {}

# open and read csv
try:
    with open(file_to_load) as election_data:
        reader = csv.reader(election_data)
        header = next(reader)  # Skip the header row

        for row in reader:
            # increment total votes
            total_votes += 1 

            # candidate name from each row
            candidate_name = row[2]

            # add candidates to the directory
            if candidate_name not in candidate_votes:
                candidate_votes[candidate_name] = 0

            # increment vote count for the candidates
            candidate_votes[candidate_name] += 1

    # calculation: percentage of votes each candidate won and and winner
    winner = ""
    winning_count = 0
    winning_percentage = 0.0

    # generate results
    election_results = (
        f"Election Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-------------------------\n"
    )

    # loop through dictionary
    for candidate in candidate_votes:
        votes = candidate_votes[candidate]
        vote_percentage = (votes / total_votes) * 100

        # candidate with most votea
        if votes > winning_count:
            winning_count = votes
            winner = candidate
            winning_percentage = vote_percentage

        # add results to election results string
        election_results += f"{candidate}: {vote_percentage:.3f}% ({votes})\n"

    # add winner
    election_results += (
        f"-------------------------\n"
        f"Winner: {winner}\n"
        f"-------------------------\n"
    )

    print(election_results)

    with open(file_to_output, "w") as txt_file:
        txt_file.write(election_results)

except FileNotFoundError as e:
    print(f"Error: {e}. Please check the file path and try again.")