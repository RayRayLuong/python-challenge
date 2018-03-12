#Raymond Luong
import os
import csv

csvpath = os.path.join("budget_data_1.csv")
f = open("BudgetResults.txt", "w+")
totalRevenue = 0
months = 0
monthList = []
revenueList = []
changeList = []
indexOfMax = 0
indexOfMin = 0

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    for row in csvreader:
        monthList.append(row[0])
        revenueList.append(int(row[1]))
        totalRevenue += int(row[1])
        months += 1

#Finds change in revenue
i=1
while i < len(revenueList):
    changeList.append(revenueList[i]-revenueList[i-1])
    i += 1

indexOfMax = changeList.index(max(changeList)) 
indexOfMin = changeList.index(min(changeList))
avgChange = sum(changeList)/len(changeList) #Not sure why this is different from solution
#Isn't average of changes equal to the slope between first and last points?

print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(months))
print("Total Revenue: " + str(totalRevenue))
print("Average Revenue Change: $" + str(avgChange))
print("Greatest Increase in Revenue: " + monthList[indexOfMax+1] + " ($" + str(changeList[indexOfMax]) + ")")
print("Greatest Decrease in Revenue: " + monthList[indexOfMin+1] + " ($" + str(changeList[indexOfMin]) + ")")

f.write("Financial Analysis\n")
f.write("----------------------------\n")
f.write("Total Months: " + str(months) + "\n")
f.write("Total Revenue: " + str(totalRevenue) + "\n")
f.write("Average Revenue Change: $" + str(avgChange) + "\n")
f.write("Greatest Increase in Revenue: " + monthList[indexOfMax+1] + " ($" + str(changeList[indexOfMax]) + ")\n")
f.write("Greatest Decrease in Revenue: " + monthList[indexOfMin+1] + " ($" + str(changeList[indexOfMin]) + ")\n")