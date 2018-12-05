import csv
import os


file_to_load = "budget_data.csv"


# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as revenue_data:
    reader = csv.reader(revenue_data)

    # use of next to skip first title row in csv file
    next(reader) 
    revenue = []
    date = []
    rev_change = []

    # in this loop I did sum of column 1 which is revenue in csv file and counted total months which is column 0 
    for row in reader:

        revenue.append(float(row[1]))
        date.append(row[0])

    print("Financial Analysis")
    print("-----------------------------------")
    print("Total Months:", len(date))
    print("Total Revenue: $", sum(revenue))


    #in this loop I did total of difference between all row of column "Revenue" and found total revnue change. Also found out max revenue change and min revenue change. 
    for i in range(1,len(revenue)):
        rev_change.append(revenue[i] - revenue[i-1])   
        avg_rev_change = sum(rev_change)/len(rev_change)

        max_rev_change = max(rev_change)

        min_rev_change = min(rev_change)

        max_rev_change_date = str(date[rev_change.index(max(rev_change))+1])
        min_rev_change_date = str(date[rev_change.index(min(rev_change))+1])


    print("Avereage Revenue Change: $", round(avg_rev_change, 2))
    print("Greatest Increase in Revenue:", max_rev_change_date,"($", round(max_rev_change),")")
    print("Greatest Decrease in Revenue:", min_rev_change_date,"($", round(min_rev_change),")")

Total_Months = len(date)
Total_Sum = sum(revenue)


# Specify the file to write to
output_path = os.path.join("Results.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row (column headers)
    csvwriter.writerow(['Total Months', 'Total Revenue', 'Average Revenue Change', 'Date of Max Change' 'Greatest Increase in Revenue', 'Date of Min Change','Greatest Decrease in Revenue',  ])
    csvwriter.writerow([Total_Months, Total_Sum, avg_rev_change, max_rev_change_date, max_rev_change, min_rev_change_date, min_rev_change])




    