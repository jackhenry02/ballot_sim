import pandas as pd

# Load the CSV file
df = pd.read_csv('ballot_data.csv', header=1)

# Print the column names to check if 'Room' exists
print("Columns in the CSV:", df.columns)