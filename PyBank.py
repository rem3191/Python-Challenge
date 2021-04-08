import csv
import os

dir_path=os.path.dirname(os.path.realpath(__file__))
print(dir_path)

os.chdir(dir_path)

with open("C:\\Users\\rem31\\bootcamp\\ZZ-Homework\\Python-Challenge\\PyBank\\Resources\\budget_data.csv", "r") as budgetcsv:
    
    csvreader = csv.reader(budgetcsv,delimiter=",")
    
    total=0
    months=0

    columnnames=next(csvreader)

    c1=[]
    for row in csvreader:
      c1.append(row[1])
      total=total+(int(row[1]))
      currency="${:,.2f}".format(total)
      months=months+1

c2=[]
for x,y in zip(c1,c1[1:]):
  c2.append(int(x)-int(y))
  total_change=sum(c2)
  average=total_change/months     
  currency2="${:,.2f}".format(average)

great_inc=max(c2)
currency3="${:,.2f}".format(great_inc)

great_dec=min(c2)
currency4="${:,.2f}".format(great_dec)



#output data compiled above into 'table' format shown below.
analysisoutput=(
  f"Financial Analysis\n"
  f"----------------------------\n"
  f"Total Months: {months}\n"
  f"Total: {currency}\n"
  f"Average  Change: {currency2}\n"
  f"Greatest Increase in Profits: {currency3} \n"
  f"Greatest Decrease in Profits: {currency4}\n"
)
#outputs data into txt file in Analysis folder
print(analysisoutput)
with open("C:\\Users\\rem31\\bootcamp\\ZZ-Homework\\Python-Challenge\\PyBank\\Analysis\\budget_data.txt", "w") as budgettxt:
    budgettxt.write(analysisoutput)