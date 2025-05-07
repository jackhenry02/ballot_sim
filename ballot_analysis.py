import pandas as pd

# Load the ballot data from the CSV
df = pd.read_csv('ballot_data.csv')

# Example: Assuming the CSV has columns like 'room_1_choice_1', 'room_1_choice_2', ..., 'room_n_choice_5'
# We will sum these columns for each room.

# Create a new column that sums up the choices for each room
df['total_choices'] = df.iloc[:, 1:].sum(axis=1)  # Sum the columns that represent choices for each room

# Calculate the number of people (divide total choices by 5)
num_people = df['total_choices'].sum() / 5

print(f'Total number of people in the ballot: {num_people}')
