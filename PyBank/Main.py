# This will allow us to create file paths across operating systems
import os
# Module for reading CSV files
import csv
#csvpath = os.path.join("c:/Users/jmced/Desktop/python-challenge/PyBank/Resources/budget_data.csv")
csvpath = os.path.join('..','Resources', 'budget_data.csv')
totalmonths = 0
total = 0
myavg = 0
change = 0
Datelist = []
prf_loss =[]
changes = []
avgchanges = []
avgloss = []


with open(csvpath) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    myskip = next(csvreader)
#loops through for total/total months and populates lists
    for row in csvreader:
        totalmonths += 1
        total += int(row[1])         
        prf_loss.append(int(row[1]))   
        avgloss.append(int(row[1]))       
        Datelist.append(row[0])
#Greatest Increase/decrease--------------------------------
for i in range(0,len(prf_loss)):
    changes.append(prf_loss[i] - prf_loss[i-1])    
    greatinc = max(changes)
    greatdec = min(changes)
    maxdate = str(Datelist[changes.index(max(changes))])
    mindate = str(Datelist[changes.index(min(changes))]) 

#average changes---------------------------------------------
for i in range(1,len(prf_loss)):
    avgchanges.append(avgloss[i] - avgloss[i-1])     
    myavg = round(sum(avgchanges)/len(avgchanges),2)

#print to terminal--------------------------------------------
print(f"Financial Analysis")
print(f"----------------------------")
print(f"Total Months: {totalmonths}")
print(f"Total: ${total}")
print(f"Average Change: ${myavg}")
print(f"Greatest Increase in Profits: {maxdate}  (${greatinc})")
print(f"Greatest Decrease in Profits: {mindate}  (${greatdec})")
#--------------------------------------------------------------



#printing to txt File----------------------------------------
myresults = f'''
Financial Analysis

-------------------------

 Total Months: {totalmonths}
 Total: ${total}
 Average Change: ${myavg}
 Greatest Increase in Profits:  {maxdate}  (${greatinc})
 Greatest Decrease in Profits:  {mindate}  (${greatdec})
 
  '''
#print (myresults)
#output_path= os.path.join("c:/Users/jmced/Desktop/python-challenge/PyBank/Analysis/PyBankAnalysis.txt")
output_path= os.path.join('..', 'Analysis', 'PyBankAnalysis.txt')
with open(output_path, 'w') as textfile:
    textfile.write(myresults)
#-------------------------------------------------------------  


