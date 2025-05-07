import pandas as pd

# Load the CSV file to get the ballot data
df = pd.read_csv('ballot_data.csv', header=1)  # Adjust header as necessary

# Set your 5 choices manually for testing
my_choices = ['57A', '2B', '4C', '4D', '5E']  # First choice is '57A', others are random for now
#my_choices = ['56D', '56E', '56F', '56C', '56B'] # Actual choices currently on ballot

# Calculate total number of people in the ballot
# We sum the values in each column (from the 3rd column onwards) and divide by 5
# Since each person submits 5 choices, the total number of people is the sum of all choices divided by 5
total_people = df.iloc[:, 1:].apply(pd.to_numeric, errors='coerce').iloc[:, 1:].sum().sum() / 5

# Now, let's calculate the probabilities
probabilities = []
for choice in my_choices:
    # Check the number of people who have chosen this room as their first choice
    first_choice_count = df.loc[df['Room'] == choice, 'Chosen as first choice'].values[0]
    
    if first_choice_count == 0 :
        # If no one else has chosen it, you're guaranteed the room
        probabilities.append(1.0)
    else:
        # If there are other people who have chosen it, calculate the probability based on random prioritization
        prob = 1 / (first_choice_count + 1)  # Random chance of getting a higher priority
        probabilities.append(prob)

# Calculate thrown off probability
# For simplicity, let's say that if all of your 5 choices are filled by others, you'll be thrown off
# So, we calculate the probability of being thrown off as the complement of getting assigned any of your 5 choices
thrown_off_prob = 1 - sum(probabilities)

# Print the results
print(total_people)
print("Probabilities for each choice:")
for i, choice in enumerate(my_choices):
    print(f"{choice}: {probabilities[i]}")
print(f"Thrown off probability: {thrown_off_prob}")
