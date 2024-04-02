import csv 
import random


# Amount of records to generate
records = 1000

# Define the fieldnames for the csv file
fieldnames = ['id', 'name', 'age', 'city']

# Define some lists of possible values for each field
names = ['Alice', 'Bob', 'Grace', 'Charlie', 'Diana', 'Eva', 'Frank']
cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia', 'San Antonio', 'San Diego', 'Dallas', 'Austin', 'Jacksonville', 'San Jose', 'Fort Worth', 'Columbus', 'Charlotte', 'Indianapolis', 'San Francisco', 'Seattle', 'Denver', 'Oklahoma City']


# Open the CSV file for writing
with open('data.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    # Write the headers of the file
    writer.writeheader()

    # Generate and write random data for each record
    for i in range(records):
        writer.writerow({
                        'id':i,
                        'name': random.choice(names),
                        'age': random.randint(24,45),
                        'city': random.choice(cities)
        })

