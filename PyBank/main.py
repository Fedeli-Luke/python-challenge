import os
import csv

budgetdata = os.path.join('budget_data.csv')

    


# Method 2: Improved Reading using CSV module

with open(budgetdata) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    # Read each row of data after the header

    
    month_count = 0
    total_profit = 0
    profit_end = []
    profit_beg = []
    #change = ending - beginning
    for row in csvreader:  
        if row == row[1]:
            profit_beg
            pass      
        month_count += 1
        total_profit += int(row[1])
        profit_end = row[1]
        #average = change / 2
        
    print(f"Total Months: {month_count}")
    print(f"Total: {total_profit}")
    print(f"Average Change: {profit_beg}")

