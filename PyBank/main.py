import os
import csv

# Path to collect data from the Resources folder
budget_data_csv = os.path.join('Resources', 'budget_data.csv')

# print(budget_data_csv)
with open(budget_data_csv) as csvfileforfun:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfileforfun, delimiter=',')

    # print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(f"Financial Analysis: {csv_header}")

    surplus = []
    monthly_change = []
    mydate = []
    
    # Read each row of data after the header
   
    for row in csvreader:
        surplus.append(int(row[1]))
        mydate.append(str(row[0]))

    # print(f"Dates: {mydate}")
    # print(surplus)
    print(f"Number of Months: {len(surplus)}")

    print(f"Total Profits (USD): {sum(surplus)}")
    
    for surplus_index in range(len(surplus)-1):
        profit_change = surplus[surplus_index+ 1] - surplus[surplus_index]
        monthly_change.append(profit_change)

    # print(monthly_change)
   
    total_months = len(monthly_change) 

    sum_of_monthly_changes = sum(monthly_change)

    average_change = sum_of_monthly_changes/total_months

    print(f"Average Monthly Change (USD): {average_change}")


    monthly_change_index = monthly_change.index(max(monthly_change))

    print(f"Month of Greatest Profits: {mydate[monthly_change_index]} and Greatest Increase (USD): {max(monthly_change)}")    
    print(f"Month of Greatest Losses: {mydate[monthly_change_index]} and Greatest Decrease (USD): {min(monthly_change)}")    

    