import os
import csv

budgetdata_csv = os.path.join("budget_data.csv")

with open (budgetdata_csv, newline="") as budget_data:
    csvreader = csv.reader(budget_data, delimiter=",")
    csv_header = next(budget_data, None)  # skip the headers

    # define variables
    counter = 0
    profit = 0
    
    for row in csvreader:
        counter = counter + 1
        profit += int(row[1])

print("\n Financial Analysis\n---------------------------------- ")
print("Total Months:", counter)
print("Total Profit: $",profit)

