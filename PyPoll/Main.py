import os
# Module for reading CSV files
import csv
#csvpath = os.path.join("c:/Users/jmced/Desktop/python-challenge/PyPoll/Resources/election_data.csv")
csvpath = os.path.join('..','Resources', 'election_data.csv')

votecount = 0
clist = []
myvotedictionary = {}
winner = 0
percent = 0
myval= 0


with open(csvpath) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    skipheader = next(csvreader)

    for row in csvreader:        
        votecount += 1   
        cname = row[2]
      #create unique candidate name list
        if cname in clist:
            myvotedictionary[cname] = myvotedictionary[cname] + 1
       #new candidate     
        else:
            clist.append(cname)            
            myvotedictionary[cname] = 1



winner = max(myvotedictionary, key=myvotedictionary.get)

#printing to terminal---------------------------------------------
print(" ")
print(f"Election Results")
print(f"-------------------------")
print(f"Total Votes: {votecount}")
print(" ")
for names, votes in myvotedictionary.items():    
            
        myval = ("   % "'{val}'.format(val=(votes/votecount)*100))          
        
        print('{key} : {myval}  ({val})'.format(key=names,myval=myval, val=votes))


print(" ")
print(f"Winner: {winner}")
print(" ")



#printing to txt File---------------------------------------------

#output_path= os.path.join("c:/Users/jmced/Desktop/python-challenge/PyPoll/Analysis/PyPollAnalysis.txt")
output_path= os.path.join('..', 'Analysis', 'PyPollAnalysis.txt')
with open(output_path, 'w') as textfile:
    text = csv.writer(textfile)

    text.writerow([f"Election Results"])
    text.writerow([f"----------------------------------"])
    text.writerow([f'Total Votes :  {votecount}'])
    text.writerow([f"-----------------------------------"])
    for names, votes in myvotedictionary.items():  
        myval =("   % "'{val}'.format(val=(votes/votecount)*100))           
        text.writerow([f'{names} : {myval}  ({votes})'.format(key=names,myval=myval, val=votes)])

    text.writerow(["-----------------------------------"])

    text.writerow([f'Winner : {winner}'])

    text.writerow(["-----------------------------------"])

#---------------------------------------------------------------
    