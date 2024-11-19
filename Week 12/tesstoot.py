# List of given matchups
matchups = [
    ('1', '8', '11', '13'),
    ('1', '2', '5', '12'),
    ('1', '4', '6', '10'),
    ('2', '4', '14', '16'),
    ('2', '3', '13', '15'),
    ('2', '6', '7', '11'),
    ('3', '5', '9', '10'),
    ('3', '7', '12', '14'),
    ('4', '5', '11', '15'),
    ('4', '9', '12', '13'),
    ('5', '7', '13', '16'),
    ('6', '9', '15', '16'),
    ('8', '10', '14', '15'),
    ('10', '11', '12', '16')
]

# Dictionary to store teams and their matched opponents
team_matches = {}

# Populate the dictionary with existing matchups
for matchup in matchups:
    for i, team in enumerate(matchup):
        if team not in team_matches:
            team_matches[team] = set()
        # Add all other teams in the matchup to the current team's set
        team_matches[team].update(set(matchup) - {team})

# Find all teams involved in the matchups
all_teams = set(team_matches.keys())

# Dictionary to store the missing matchups
missing_matchups = {}

# Calculate missing matchups for each team
for team in sorted(all_teams):
    # Teams that have not been matched with the current team
    unmatched_teams = all_teams - team_matches[team] - {team}
    missing_matchups[team] = unmatched_teams

# Display the missing matchups in the required format
for team, unmatched in missing_matchups.items():
    matched_with = ", ".join(sorted(unmatched))
    print(f"{team} : {matched_with}")
