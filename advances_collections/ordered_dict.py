from collections import OrderedDict


def main():
    # OrderedDict is a dictionary that remembers the order by what items were inserted
    # list of sport teams with wins and losses
    sportTeams = [("Royals", (18, 12)),
                  ("Rockets", (24, 5)),
                  ("Cardinals", (20, 10)),
                  ("Dragons", (22, 8)),
                  ("Kings", (15, 15)),
                  ("Chargers", (20, 10)),
                  ("Jets", (16, 14)),
                  ("Warriors", (25, 5))]

    sortedTeams = sorted(sportTeams, key=lambda t: t[1][0], reverse=True)
    print(sortedTeams)

    # create an ordered dictionary of the teams
    teams = OrderedDict(sortedTeams)
    print(teams)  # ordered is maintained
    while teams:  # do while teams is not empty
        team, winLoss = teams.popitem()  # default parameter is True => last item popped
        print(team, winLoss)

    teams = OrderedDict(sortedTeams)
    print("Top teams:")
    for i, team in enumerate(teams, start=0):
        print(i + 1, team)
        if i == 2:
            break

    a = OrderedDict({"a": 1, "b": 2, "c": 3})
    b = OrderedDict({"a": 1, "b": 2, "c": 3})
    print("Equality test 1:", a == b)  # True, order and values are the same
    # Change order
    b = OrderedDict({"a": 1, "c": 3, "b": 2})
    print("Equality test 2:", a == b)  # False, order is not the same

    print("Equality test 3",
          {"a": 1, "c": 3, "b": 2} == {"a": 1, "b": 2, "c": 3})  # True, for simple dict order doesn't matter


if __name__ == "__main__":
    main()
