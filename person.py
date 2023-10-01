import csv

# Your code to generate CSV data here

data = [
    ["Name", "Age"],
    ["Alice", 25],
    ["Bob", 30],
    # Add more data here
]

csv_file = "data/output.csv"

with open(csv_file, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("CSV file generated.")
