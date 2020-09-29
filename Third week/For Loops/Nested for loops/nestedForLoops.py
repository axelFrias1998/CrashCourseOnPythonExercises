for left in range(7):
    for right in range(left, 7):
        print(f"[{left}|{right}]", end=" ")
    print()

teams = ["Dragons", "Wolves", "Pandas", "Unicorns"]
for home_team in teams:
    print(f"| {home_team}", end=" |\n")
    for away_team in teams:
        if home_team != away_team:
            print(f"{home_team} vs {away_team}")
    print()
