import csv
import random

# Sample data generation (replace with your actual data generation logic)
data = []
for _ in range(3):
    person = {
        "Name": "John Doe",
        "Age": random.randint(18, 65),
        "City": "Example City",
    }
    data.append(person)

# Save data to a CSV file
with open("person.csv", mode="w", newline="") as csv_file:
    fieldnames = ["Name", "Age", "City"]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    for person in data:
        writer.writerow(person)
      
