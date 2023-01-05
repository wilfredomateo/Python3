# Program that takes in Bexar County Arrest Reports and converts data into a readable CSV file

import csv

with open('./reports/01Jan2023.txt', 'r') as input_file:
    input_file.seek(673) # move to location of first data entry
    line = input_file.readline()
    list = line.split()
    with open('./reports/01Jan2023.csv', 'w') as output_file:
        writer = csv.writer(output_file)
        writer.writerow(('Booking Number', 'Day', 'Month', 'Year', 'Time', 'Last Name', 'First Name', 'Middle I', 'Race', 'Gender', 'DOB', 'Address1', 'Address2', 'Address3', 'Address4', 'Address5', 'Address6'))
        writer.writerow(list)
        #print(list)




