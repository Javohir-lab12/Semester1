def analyzer(team_dictionary):
    counter = 0
    temp = set()
    set_list = []
    for ids in team_dictionary.values():
        set_list.append(set(ids))
        counter += len(ids)
    #filtered = map(lambda ids: set(ids), teams.values()) deos same thing
    for i in range(len(set_list)):
        for j in range(i+1, len(set_list)):
            intersection = set_list[i].intersection(set_list[j])
            temp = temp.union(intersection)
    number_of_valids = counter - len(temp)
    valid_teams = None
    for team, ids in team_dictionary.items():
        for id in temp:
            if id not in ids:
                valid_teams = (team)
    return temp, number_of_valids, team

    
teams = {
    "Alpha": [101, 102, 103],
    "Beta":  [103, 104, 105], # 103 is a duplicate (Alpha & Beta)
    "Gamma": [106, 107],      # Clean
    "Delta": [102, 108]       # 102 is a duplicate (Alpha & Delta)
}
print(analyzer(teams))