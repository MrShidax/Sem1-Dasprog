from itertools import combinations
import random

# List of team names or identifiers
teams = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16"]

# Set to keep track of pairs that have already met
pairs_met = set()

# List to store the valid combinations
valid_combinations = []

# Generate all possible combinations of 4 teams
team_combinations = list(combinations(teams, 4))
random.shuffle(team_combinations)  # Shuffle to get a random distribution

# Iterate over each combination
for combo in team_combinations:
    # Generate all pairs within the current combination
    pairs_in_combo = list(combinations(combo, 2))
    
    # Check if any pair has already met
    if any(pair in pairs_met or (pair[1], pair[0]) in pairs_met for pair in pairs_in_combo):
        continue  # Skip this combination if any pair has met before
    else:
        # Add the combination to the list of valid combinations
        valid_combinations.append(combo)
        
        # Update the set of pairs that have now met
        for pair in pairs_in_combo:
            pairs_met.add(pair)
    
    # Optional: Break if all pairs have met (i.e., pairs_met contains all possible pairs)
    if len(pairs_met) == len(list(combinations(teams, 2))):
        break

# Output the valid combinations
print("Number of valid combinations:", len(valid_combinations))
for combo in valid_combinations:
    print(combo)
