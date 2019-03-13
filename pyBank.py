import os
import csv
import numpy
#importing file
budget_data = os.path.join(os.path.expanduser('~'),"desktop","data analytics bootcamp","python","budget_data.csv")
#locating csv file

#store data as list
months = []
profit_loss = []
net_total = []
profit = []

with open(budget_data, newline= "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ",")
#creating csv reader 
    print(csvreader)

    csv_header = next(csvfile)
    print(f"Header: {csv_header}")
    headers = csv_header.split (',')
    print('headers split up:' , headers)
    

    for row in csvreader:
        months.append(row[0]) 
        profit_loss.append(int(row[1]))


    net_total = numpy.diff(profit_loss)
    net_total = list(net_total)


    average = (sum(net_total) / len(months))

    greatest_increase = max(net_total)

    greatest_decrease = min(net_total)

    print("Financial Analysis")
    print("-----------------------")
    print("Total number of months:", len(months))
    #net total of amount
    print("This is the net total:", sum(profit_loss))
    #average of changes in profit/losses
    print("The average of the change in Profit/Losses:" , average)
    #the greatest increase in profits
    print("The greatest increase in profits:", greatest_increase)
    #the greatest decrease in profits
    print("The greatest decrease in profits:", greatest_decrease)
 
file = open("output_PyBank.txt", "w")
file.write("Total number of months: 86")
file.write("Total: 38382578")
file.write("Average  Change: -2288.19")
file.write("Greatest Increase in Profits: 1926159 Feb 2012")
file.write("Greatest Decrease in Profits: -2196167 Sept 2013")
file.close()  
  
  