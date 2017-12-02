import csv
import numpy as np
import statistics as s
total_months = []
total_months1 = []
total_months2 = []
total_revenue = []
total_revenue1 = []
total_revenue2 = []
total_monthr_change = []
total_monthr_change1 = []
total_monthr_change2 = []
new_total_revenue1 = []
new_total_revenue2 = []
new_total_revenue = []

with open('data/budget_data_1.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter = ",")
    for row in readCSV:
        month = row[0]
        revenue = row[1]
        total_months.append(month)
        total_months1.append(month)
        total_revenue.append(revenue)
        total_revenue1.append(revenue)
        new_total_revenue1.append(revenue)

with open('data/budget_data_2.csv') as csvfile2:
    readCSV2 = csv.reader(csvfile2, delimiter = ",")
    for row in readCSV2:
        month2 = row[0]
        revenue2 = row[1]
        total_months.append(month2)
        total_months2.append(month2)
        total_revenue.append(revenue2)
        total_revenue2.append(revenue2)
        new_total_revenue2.append(revenue2)

total_months.remove('Date')
total_months.remove('Date')
Number_total_months = len(total_months)
# print(total_months)
print("The total number of months included in the dataset is "
     + str(Number_total_months))

total_revenue.remove('Revenue')
total_revenue.remove('Revenue')
Sum_total_months = sum(int(r) for r in total_revenue)
#print(total_revenue)
print("The total amount of revenue gained over the entire period is "
     + "$" + str(Sum_total_months))

total_revenue1.remove('Revenue')
#print(total_revenue1)

new_total_revenue1.remove('Revenue')
new_total_revenue1.insert(0,"0")
del new_total_revenue1[-1]
#print(new_total_revenue1)

total_revenue2.remove('Revenue')
#print(total_revenue2)

new_total_revenue2.remove('Revenue')
new_total_revenue2.insert(0,"0")
del new_total_revenue2[-1]
#print(new_total_revenue2)

#print(len(total_revenue2))
#print(len(new_total_revenue2))

a = np.array([int(i) for i in total_revenue1])
b = np.array([int(i) for i in new_total_revenue1])
months_change1 = a-b
#print(months_change1)

c = np.array([int(i) for i in total_revenue2])
d = np.array([int(i) for i in new_total_revenue2])
months_change2 = c-d
#print(months_change2)

for revenue in months_change1:
    new_total_revenue.append(revenue)

for revenue in months_change2:
    new_total_revenue.append(revenue)

#print(new_total_revenue)

average_change_in_revenue = sum(new_total_revenue)/len(new_total_revenue)
#print(average_change_in_revenue)

print("The average change in revenue between months over the entire period is "
     + "$" + str(average_change_in_revenue))

greatest_increase = max(new_total_revenue)
#print(greatest_increase)
n = new_total_revenue.index(int(max(new_total_revenue)))
#print(n)
Date1 = total_months[n]
#print(Date1)

print("The greatest increase in revenue (date and amount) over the entire period"
     + Date1 + "($" + str(greatest_increase)+")")

greatest_decrease = min(new_total_revenue)
#print(greatest_decrease)
m = new_total_revenue.index(int(min(new_total_revenue)))
#print(m)
Date2 = total_months[m]
#print(Date2)

print("The greatest decrease in revenue (date and amount) over the entire period"
     + Date2 + "($" + str(greatest_decrease)+")")

