import os
import csv

electiondatapath = os.path.join('../..','gt-atl-data-pt-03-2020-u-c', '03-Python', 'Homework', 'PyPoll', 'Resources', 'election_data.csv')


with open (electiondatapath) as csvelectionfile:
    csvreader = csv.reader(csvelectionfile, delimiter=',')

# Read the header row first 
    csv_header = next(csvelectionfile)

    #hold number of rows which will be the total votes
    num_rows = 0

    #total votes per candidate
    totalvotesDic = {}
    
    candidates_info = ""

    #list to zip and write to csv
    results = []
    winnerlist = []


    for row in csvreader:

        #total number of votes cast
        num_rows += 1
        
        # Check if candidate in the dictionary keys, if is not then add the candidate to the dictionary and count it as one, else sum 1 to the votes
        if row[2] not in totalvotesDic.keys():
            totalvotesDic[row[2]] = 1
        else:
            totalvotesDic[row[2]] += 1

#get the percentage of votes and print result next to candidate and total votes
#for candidates in totalvotesDic.keys():
for candidates, votes in totalvotesDic.items():
    candidates_info =  '\n'.join([candidates_info, str(candidates) + ": " + "{:.2%}".format(votes / num_rows) + " " + "(" + str(votes)+ ")"])
    #print(candidates_info)
    #totalvotesDic[candidates].append("{:.2%}".format(totalvotesDic[candidates] / num_rows))
    #candidates_info = candidates, "{:.2%}".format(totalvotesDic[candidates] / num_rows), "(", totalvotesDic[candidates], ")"
    #print(candidates, "{:.2%}".format(totalvotesDic[candidates] / num_rows), "(", totalvotesDic[candidates], ")")

#get the winner out of the candidates
winner = max(totalvotesDic, key=totalvotesDic.get)
      
print("Election Results")
print("-----------------------")
print(f"Total Votes: {(num_rows)}")
print("-----------------------")
print(candidates_info)
print("-----------------------")
print(f"Winner: {(winner)}")
print("-----------------------")


#append to the list to zip
results.append("Election Results")
results.append(f"Total Votes: {(num_rows)}")
winnerlist.append(f"Winner: {(winner)}")

# zip list together
cleaned_csv = zip(results)

# Set variable for output file
output_file = os.path.join("output_Pypoll.csv")

#  Open the output file
with open(output_file, "w") as datafile:
    writer = csv.writer(datafile)

    # Write in zipped rows
    writer.writerows(cleaned_csv)

    csv.register_dialect("custom", delimiter=" ", skipinitialspace=True)
    writer = csv.writer(datafile, dialect="custom")
    #for candidates in totalvotesDic.keys():
    writer.writerow(candidates_info)

    writer.writerows(winnerlist)