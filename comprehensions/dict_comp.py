def main():
    # Define a list of temperature values
    ctemps = [0, 12, 34, 100]

    # Use a comprehension to build a dictionary
    tempDict = {t: (t * 9 / 5) + 32 for t in ctemps}
    print(tempDict)
    tempDict = {t: (t * 9 / 5) + 32 for t in ctemps if t < 100}
    print(tempDict)

    # Merge two dicitonaries with a comprehensions
    team1 = {"Jones": 24, "Jameson": 18, "Smith": 58, "Burns": 7}
    team2 = {"White": 12, "Macke": 88, "Perce": 4}

    # team will take values from team1 and team2 - 'for team in (team1, team2)'
    # then we iterate over all these values in 'for k,v in team.items()'
    # and simply assign v to k 'k: v'
    newTeam = {k: v for team in (team1, team2) for k, v in team.items()}
    print(newTeam)


if __name__ == "__main__":
    main()
