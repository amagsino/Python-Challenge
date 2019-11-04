import csv
import os

#creates a path for file (check this later)
my_path = os.path.abspath(os.path.dirname(__file__))
file = os.path.join(my_path, '..', 'Resources', 'budget_data.csv')

#list used to store data for months and revenue
months = []
revenue = []

#csv file is split into lists within reader
with open(file, 'r') as csvfile:
    csvread = csv.reader(csvfile)
    
    next(csvread, None) 

    #revenue list is converted to integers
    for row in csvread:
        months.append(row[0])
        revenue.append(int(row[1]))

#counts total months through len
total_months = len(months)

#sets up variables for greatest increase, greatest decrease and total
#sets greatest increase and greatest decrease starting at the first revenue entry
greatest_increase = revenue[0]
greatest_decrease = revenue[0]
total = 0

#for loop through revenue indices to find greatest increase and greatest decrease
#adds each revenue to total revenue
for r in range(len(revenue)):
    if revenue[r] >= greatest_increase:
        greatest_increase = revenue[r]
        great_increase_month = months[r]
    elif revenue[r] <= greatest_decrease:
        greatest_decrease = revenue[r]
        great_decrease_month = months[r]
    total += revenue[r]

#calculates average change and round to hundredths decimal place
average_change = round(total/total_months, 2)

#creates a path for output file called pybank_output
output_destination = os.path.join('Output','pybank_output.txt')

#opens the output in writefile mode and prints the summary
with open(output_destination, 'w') as writefile:
    writefile.writelines('Financial Analysis\n')
    writefile.writelines('----------------------------' + '\n')
    writefile.writelines('Total Months: ' + str(total_months) + '\n')
    writefile.writelines('Total: $' + str(total) + '\n')
    writefile.writelines('Average Change: $' + str(average_change) + '\n')
    writefile.writelines('Greatest Increase in Profits: ' + great_increase_month + ' ($' + str(greatest_increase) + ')'+ '\n')
    writefile.writelines('Greatest Decrease in Profits: ' + great_decrease_month + ' ($' + str(greatest_decrease) + ')')

#opens the output file in readfile mode and prints
with open(output_destination, 'r') as readfile:
    print(readfile.read())