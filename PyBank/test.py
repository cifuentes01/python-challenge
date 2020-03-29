import os
import csv

budgetdatapath = os.path.join('../..', 'gt-atl-data-pt-03-2020-u-c', '03-Python', 'Homework', 'PyBank', 'Resources', 'budget_data.csv')

#                          Documentos/GitHub/python-challenge/PyBank
# "C:\Users\Anita\OneDrive\Documentos\GitHub\gt-atl-data-pt-03-2020-u-c\03-Python\Homework\PyBank\Resources\budget_data.csv"
with open(budgetdatapath) as csvbudgetfile:
    csvreader = csv.reader(csvbudgetfile, delimiter=',')
    #print(csvreader)


# Read the header row first 
    csv_header = next(csvbudgetfile)

    profitloss = 0
        
    num_of_row = 0

    changelist = []

    sum_changes = 0

    increase = 0

    decrease = 0

    title = ["Total Months:", "Total:", "Average  Change:", "Greatest Increase in Profits:", "Greatest Decrease in Profits:"]

    analysis = []


     # Read through each row of data after the header
    for row in csvreader:
 
        #total number of months
        num_of_row += 1
       
        #net total amount of "Profit/Losses"
        profitloss += float(row[1])

        #Method 1: average of the changes in "Profit/Losses"
        #if num_of_row == 1:
            #first_num = float(row[1])
        #else:
          #change = float(row[1])- first_num
        
        if num_of_row == 1:
            previous_num = float(row[1])
        else:
          changelist.append(float(row[1]) - previous_num)
          previous_num = float(row[1])

          #Method 2: average of the changes in "Profit/Losses"
          sum_changes = sum(changelist)

    #greatest increase in profits
    for changeitem in changelist:
        if changeitem > 0 and changeitem > increase:
            increase = changeitem

    #greatest decrease in profits
    for changeitem in changelist:
        if changeitem < 0 and changeitem < decrease:
            decrease = changeitem

    analysis.append(num_of_row)      
    analysis.append('${:,.0f}'.format(profitloss))    
    analysis.append('${:,.2f}'.format((sum_changes / (num_of_row - 1))))
    analysis.append('${:,.0f}'.format(increase))
    analysis.append('${:,.0f}'.format(decrease))


    print(f"Total Months: {(num_of_row)}")
    print(f"Total: {'${:,.0f}'.format(profitloss)}")
    print(f"Average  Change: {'${:,.2f}'.format(sum_changes / (num_of_row -1 ))}")
    print(f"Greatest Increase in Profits: {(row[0])} {'${:,.0f}'.format(increase)}")
    print(f"Greatest Decrease in Profits: {(row[0])} {'${:,.0f}'.format(decrease)}")


# zip list together
cleaned_csv = zip(title, analysis)

# Set variable for output file
output_file = os.path.join("Output_PyBank.csv")

#  Open the output file
with open(output_file, "w") as datafile:
    writer = csv.writer(datafile)

    # Write in zipped rows
    writer.writerows(cleaned_csv)