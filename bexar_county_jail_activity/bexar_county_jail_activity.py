# Program that takes in Bexar County Arrest Reports and converts data into a readable CSV file

import csv

with open('./reports/01Jan2023.txt', 'r') as input_file:
    lines = input_file.readlines()
    with open('./reports/01Jan2023.csv', 'w') as output_file:
        writer = csv.writer(output_file)
        writer.writerow(('Booking Number', 'Month', 'Day', 'Year', 'Time', 'Last Name', 'First Name', 'Middle I', 'Race', 'Gender', 'DOB', 'Address'))
        for line in lines:
            if line.startswith('0B20'):
                writer.writerow(line.split())
        




