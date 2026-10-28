def get_highscore(player_stats):
    total_points = {}
    for person in range(len(player_stats)):
        goals = player_stats[person]['goals']
        passes = player_stats[person]['passes']
        goal_attempts = player_stats[person]['goal_attempts']
        pass_attempts = player_stats[person]['pass_attempts']

        total_points[player_stats[person]['name']] = (goals * 20) + (passes * 2) + ((goal_attempts - goals) * 5) + (pass_attempts - passes)
        high_scorer = None
        high_score = 0
        high_scorer = None
    high_score = 0

    for name in total_points:
        if total_points[name] > high_score:
            high_score = total_points[name]
            high_scorer = name

    return high_scorer, high_score


player_stats = [
    {"name": "Bob", "goals": 2, "passes": 15, "goal_attempts": 3, "pass_attempts": 17},
    {"name": "Alex", "goals": 1, "passes": 17, "goal_attempts": 2, "pass_attempts": 20},
    {"name": "Molly", "goals": 1, "passes": 28, "goal_attempts": 2, "pass_attempts": 31},
    {"name": "Sophia", "goals": 2, "passes": 21, "goal_attempts": 3, "pass_attempts": 25}
]

print(get_highscore(player_stats))