import random
import csv

# Generate random person data
data = []
for _ in range(3):
    name = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(5))
    age = random.randint(18, 65)
    height = round(random.uniform(150, 200), 2)
    data.append([name, age, height])

# Save data to a CSV file
with open('person.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Name', 'Age', 'Height'])
    writer.writerows(data)
