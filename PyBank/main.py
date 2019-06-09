# declare dependencies
import os
import csv

budgetdata_csv = os.path.join("budget_data.csv")
newfile = os.path.join('Financial_Analysis_Results.txt')

# open and read csv file
with open (budgetdata_csv, newline="") as budget_data:
    csvreader = csv.reader(budget_data, delimiter=",")
    csv_header = next(budget_data, None)  # skip the headers

# declare variables
    profit = []
    date = []
    profit_change = []
    output = []


# loop to read csv file and append csv rows to open list variables
    for row in csvreader:
        profit.append(float(row[1]))
        date.append(row[0])

       

# loop to calculate revenue data points
    for i in range(1,len(profit)):
        profit_change.append(profit[i] - profit[i-1])   
        avg_prof_change = sum(profit_change)/len(profit_change)

        max_prof_change = max(profit_change)

        min_prof_change = min(profit_change)

        max_prof_change_date = str(date[profit_change.index(max(profit_change))])
        min_prof_change_date = str(date[profit_change.index(min(profit_change))])

# variables
    total_months = len(date)
    total_profit = sum(profit)
    avg_prof_chng = round(avg_prof_change)

# appened all data points
    output.append("\n Financial Analysis\n---------------------------------- ")
    output.append("Total Months:" + str(total_months))
    output.append("Total Profit: $" + str(total_profit))
    output.append("Avereage Revenue Change: $" + str(avg_prof_chng))
    output.append("Greatest Increase in Revenue: " + str(max_prof_change_date) + " ($" + str(max_prof_change) + ")")
    output.append("Greatest Decrease in Revenue: " + str(min_prof_change_date) + " ($" + str(min_prof_change) + ")")

# print appended results
    print("\n".join((output)))

# write ouput to txt file
with open(newfile, 'w') as txtfile:
    txtfile.write('\n'.join(output))