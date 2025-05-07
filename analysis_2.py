import pandas as pd
import random
from collections import Counter

# --- Load data ---
df = pd.read_csv("ballot_data.csv", header=1)

# --- Your ballot ---
my_choices = ['57A', '2B', '4C', '4D', '5E']

# --- Build simulated participant list ---
participants = []

# Loop through each row (room) and extract how many people chose it in each rank
for _, row in df.iterrows():
    room = row['Room']
    for rank_col, rank_index in zip(df.columns[1:], range(5)):
        try:
            count = int(row[rank_col])
        except:
            continue
        # Add `count` people with this room in their rank_index position
        for _ in range(count):
            # Fill with placeholders for now
            if len(participants) <= _:
                participants.append([None]*5)
            # Fill the right position
            participants[_][rank_index] = room

# Fix any missing values by random assignment from available rooms
all_rooms = df['Room'].tolist()
for i, ballot in enumerate(participants):
    for j in range(5):
        if ballot[j] is None:
            ballot[j] = random.choice(all_rooms)

# Add your own ballot
participants.append(my_choices)

# --- Run Monte Carlo simulation ---
num_trials = 10000
outcome_counter = Counter()

for _ in range(num_trials):
    assigned = {}
    room_taken = set()
    
    # Shuffle participant order
    order = list(range(len(participants)))
    random.shuffle(order)
    
    for idx in order:
        ballot = participants[idx]
        for choice_rank, room in enumerate(ballot):
            if room not in room_taken:
                assigned[idx] = choice_rank  # Assign room
                room_taken.add(room)
                break
        if idx not in assigned:
            assigned[idx] = -1  # Thrown off

    # Record outcome for *you* (the last index)
    my_outcome = assigned[len(participants) - 1]
    outcome_counter[my_outcome] += 1

# --- Display results ---
print("\nEstimated Probabilities:")
for i in range(5):
    prob = outcome_counter[i] / num_trials
    print(f"{my_choices[i]} (choice {i+1}): {prob:.3f}")
thrown_prob = outcome_counter[-1] / num_trials
print(f"Thrown off: {thrown_prob:.3f}")


import matplotlib.pyplot as plt

# Prepare data for plotting
labels = [f"{my_choices[i]} (#{i+1})" for i in range(5)] + ["Thrown Off"]
probs = [outcome_counter[i] / num_trials for i in range(5)]
probs.append(outcome_counter[-1] / num_trials)

# Create bar plot
plt.figure(figsize=(10, 6))
bars = plt.bar(labels, probs, color=['#4caf50']*5 + ['#f44336'])

# Add probability values above bars
for bar, prob in zip(bars, probs):
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 0.01, f"{prob:.2%}", ha='center', fontsize=10)

plt.title("Probability of Receiving Each Room Choice (Ballot Simulation)")
plt.ylabel("Probability")
plt.ylim(0, 1)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
