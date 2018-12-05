import csv
import os
import collections 
import numpy as np

file_to_load = "election_data.csv"

# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as revenue_data:
    reader = csv.reader(revenue_data)

    # use of next to skip first title row in csv file
    next(reader)
    voters = []
    candidate = []
    for row in reader:
        voters.append(row[0])
        candidate.append(row[2])
    
    # Count occurence of candidates
    total = float(len(voters))
    khan = float(candidate.count('Khan'))
    Correy = float(candidate.count('Correy'))
    Li = float(candidate.count('Li'))
    OT = float(candidate.count("O'Tooley"))


    # Calculate % of winners 
    
    k = round((khan / total)*100, 2)
    c = round((Correy / total)*100, 2)
    l = round((Li / total)*100, 2)
    o = round((OT / total)*100, 2)

    # Put in list 
    percentage = [k, c, l, o]
    candidate_name = ["Khan", "Correy", "Li", "O'Toole"]

    # Get index number of maximum value  
    max_percentage = np.argmax(percentage) 
    winner = candidate_name[max_percentage]

    # print results    
    print("Election Results")
    print("-----------------------------------")
    print("Total Votes:", len(voters))
    print("-----------------------------------")
    print("Khan: ", k, "%", "(", khan, ")")
    print("Correy: ", c, "%","(", Correy, ")")
    print("Li: ", l, "%","(", Li, ")")
    print("O'Tooley: ", o, "%", "(", OT, ")")
    print("-----------------------------------")
    print("Winner: " , winner)

    
    # Specify the file to write to
output_path = os.path.join("Results_1.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row (column headers)
    csvwriter.writerow(['Election Results'])
    csvwriter.writerow(["-----------------------------------"])
    csvwriter.writerow(["Total Votes:", len(voters)])
    csvwriter.writerow(["-----------------------------------"])
    csvwriter.writerow(["Khan: ", k, "%", khan])
    csvwriter.writerow(["Correy: ", c, "%", Correy])
    csvwriter.writerow(["Li: ", l, "%", Li])
    csvwriter.writerow(["O'Tooley: ", o, "%", OT])
    csvwriter.writerow(["-----------------------------------"])
    csvwriter.writerow(["Winner: " , winner])
