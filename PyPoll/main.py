import os
import csv

# Path to collect data from the Resources folder
election_data_csv = os.path.join('Resources', 'election_data.csv')

print(election_data_csv)

with open(election_data_csv, 'r') as f :
    csv_reader=csv.reader(f,delimiter=',')
    Header_csv=next(csv_reader)
    Total_Votes=0
    
    name={}
    for row in csv_reader:
        

        Total_Votes=Total_Votes+1
        if row[2] not in name: 
            name[row[2]] = 0
        name[row[2]] = name[row[2]] + 1 
    print(f'Election Results')
    print('---------------------------')
    print (f'Total votes : {Total_Votes}')
    print('---------------------------')
    old_value=0
    for key in name:
        value=name[key]
        if old_value <= value : 
            old_value=value
            Winner=key
        Vote_Per=(value/Total_Votes)*100 
        print(f'{key} : {"%.2f" % Vote_Per} % ({value})')
    print('---------------------------')
    print(f'Winner is {Winner}')
    print('---------------------------')
    

    import sys
    sys.stdout = open('Analysis/ElectionResults.txt', 'w') 
    print(f'Election Results')
    print('---------------------------')
    print (f'Total votes : {Total_Votes}')
    print('---------------------------')
    for key in name:
        value=name[key]
    Vote_Per=(value/Total_Votes)*100 
    print(f'{key} : {"%.2f" % Vote_Per} % ({value})')
    print('---------------------------')
    print(f'Winner is {Winner}')
    print('---------------------------')   