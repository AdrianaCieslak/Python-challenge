import os
import csv

csvpath = os.path.join("..", "Resources", "budget_data.csv")

 
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    
    next(csvfile)
   
    #List to store data
    months = []
    total_months = []
    row = []
    date = []
    count = 0 
    net_total = 0
    average = 0
    greatest_increase = 0
    greatest_month = "0"
    previous_month = 867884
    greatest_decrease = 0
    worst_month = "0"
    current_changes = []
    current_change = 0
    for row in csvreader:
        current_month = int(row[1])
        current_change = current_month - previous_month
        previous_month = current_month
        count = count + 1
        date.append(row[0])
        
        current_changes.append(current_change)
        #Calculations
        net_total = net_total + int(row[1])
        months = len(date)

        if current_change > greatest_increase: 
            greatest_increase = current_change
            greatest_month =  row[0]
        
        if current_change < greatest_decrease:
            greatest_decrease = current_change
            worst_month = row[0]
    
    average = round(sum(current_changes)/months, 2)


    # Output
    print_string = "Financial Analysis\n" \
	"----------------------------\n" \
    f"Total Months: {count}\n" \
    f"Total: ${net_total:.0f}\n" \
    f"Average change: {average:.2f}\n" \
    f"Greatest Increase in Profits: {greatest_month} (${greatest_increase:.0f})\n" \
    f"Greatest Decrease in Profits: {worst_month} (${greatest_decrease:.0f})\n" \
    
    print(print_string)
    # Create txt file
    with open(os.path.join("..", "Analysis", "output.txt"), "w") as file:
	    file.write(print_string)