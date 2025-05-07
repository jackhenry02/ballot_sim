import pandas as pd

# Load the CSV, skipping the first two rows (header and labels)
df = pd.read_csv('ballot_data.csv', header=1)

# Convert the data to numeric, forcing errors to NaN, then drop NaN values (in case of any invalid data)
df = df.iloc[:, 1:].apply(pd.to_numeric, errors='coerce')

# Calculate the total number of people by summing all choices and dividing by 5, then rounding the result
total_people = df.sum().sum() / 5

print(f'Total number of people in the ballot: {total_people}')

