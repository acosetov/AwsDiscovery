from faker import Faker
import csv

# Initialize Faker
fake = Faker()

# Number of rows to generate
num_rows = 10  # Adjust as needed

# Generate data and write to CSV
with open('test.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['First Name', 'Last Name', 'Age', 'Country'])  # Header row

    for _ in range(num_rows):
        first_name = fake.first_name()
        last_name = fake.last_name()
        age = fake.random_int(min=18, max=80)  # Generate random age between 18 and 80
        country = fake.country()

        writer.writerow([first_name, last_name, age, country])

print(f"Generated {num_rows} rows of fake data in 'test.csv'.")
