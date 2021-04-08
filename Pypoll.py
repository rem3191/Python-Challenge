import csv
import os

total_tally=[]
candidates=[]
end_result=[]
votes=0
vote_count=[]
data=['1','2']

dir_path=os.path.dirname(os.path.realpath(__file__))
print(dir_path)
os.chdir(dir_path)


with open ("C:\\Users\\rem31\\bootcamp\\ZZ-Homework\\Python-Challenge\\PyPoll\Resources\\election_data.csv",'r') as csvfile:
    csv_reader=csv.reader(csvfile, delimiter=",")
    columnname=next(csv_reader)
    
    for row in csv_reader:
        votes=votes+1
        candidate=row[2]

        if candidate in candidates:
            candidate_index=candidates.index(candidate)
            vote_count[candidate_index]=vote_count[candidate_index]+1

        else:
            candidates.append(candidate)
            vote_count.append(1)


    #print(candidates)

    percentage=[]
    max_vote=vote_count[0]
    max_index=0
    
    for count in range(len(candidates)):
        vote_percentage=vote_count[count]/votes*100
        percentage.append(vote_percentage)

        if vote_count[count]>max_vote:
            max_vote=vote_count[count]
            print(max_vote)
            max_index=count
        winner=candidates[max_index]

        percentage=[round(i,2) for i in percentage]
#print(vote_count)
     
    for count in range(len(candidates)):
        end_result=f"{candidates[count]}:{percentage[count]}% ({vote_count[count]})"
        total_tally.append(end_result)
        #print(end_result)
#print(total_tally)
#output data compiled above into 'table' format shown below.
analysisoutput=(
# print("Election Results")
# print("Total Votes:{votes}")
# print("---------------------------")
# print("{total_tally}")
# print("----------------------------")
# print("Winner: {winner}")
# )

f"Election Results\n"
f"---------------------------\n"
f"Total Votes:{votes}\n"
f"---------------------------\n"
f"{total_tally}\n"
f"----------------------------\n"
f"Winner:{winner}\n"
)
# #output data into txt file in Analysis folder
print(analysisoutput)
with open("C:\\Users\\rem31\\bootcamp\\ZZ-Homework\\Python-Challenge\\PyPoll\\Analysis\\poll_data.txt", "w") as polltxt:
    polltxt.write(analysisoutput)