import os
import csv

#list used to store data for months, profits, and change
months = []
profits = []
change_list=[]
greatest_increase = 0
greatest_decrease = 0
change=0

#creates a path for file (check this later)
file = os.path.join('Resources', 'budget_data.csv')

#csv file is split into lists within reader
with open(file) as csvfile:
    csvread = csv.reader(csvfile, delimiter=',')
    next(csvread) 

    #profits list is converted to integers
    #append month and profits to proper columns
    for row in csvread:
        months.append(row[0])
        profits.append(int(row[1]))

#goes through profits
profits = [int(row) for row in profits]

#for loop through profits indices to find greatest increase and greatest decrease

for i in range(len(profits)):
    if i < len(profits) - 1:
        change = change + (profits[i + 1] - profits[i])
        change_list.append(change)
        change = 0

#adds each profits to total profits
#calculates average change and round
average_change = round(sum(change_list) / len(change_list),2)
greatest_increase = max(change_list)
greatest_decrease = min(change_list)
greatest_decrease_month = change_list.index(greatest_decrease)
greatest_increase_month = change_list.index(greatest_increase)

#set variable for greatest and least month
greatest_month = months[greatest_increase_month+1]
least_month = months[greatest_decrease_month+1]

#creates a path for output file called pybank_output
output_file = os.path.join('..','Output','pybank_output.txt')

#opens the output in text mode and prints the summary
with open(output_file, 'w') as text:
    text.write('Financial Analysis\n')
    text.write('----------------------------' + '\n')
    text.write('Total Months: ' + str(len(months)) + '\n')
    text.write('Total: $' + str(sum(profits)) + '\n')
    text.write('Average Change: $' + str((average_change)) + '\n')
    text.write('Greatest Increase in Profits: ' + greatest_month + ' ($' + str(greatest_increase) + ')'+ '\n')
    text.write('Greatest Decrease in Profits: ' + least_month + ' ($' + str(greatest_decrease) + ')')

#opens the output file in readfile mode and prints
with open(output_file, 'r') as readfile:
    print(readfile.read())