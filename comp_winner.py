def tournamentWinner(competitions, results):
    scores = {}
    # this will hold the last winner for comparison in map
    best_team = ""
    scores[best_team] = 0

    for i, (home, away) in enumerate(competitions):

        winner = home if results[i] == 1 else away

        if winner not in scores:
            scores[winner] = 3
        else:
            scores[winner] += 3

        if scores[winner] > scores[best_team]:
            best_team = winner

    return best_team

    # this is solution 2 bit long but easy to understand time complexity is O(n) and SC is O(n)
    # for comp in competitions:
    #     # 0 means away team won
    #     if results[res_idx] == 0:
    #         if comp[1] not in map:
    #             map[comp[1]] = 3
    #         else:
    #             map[comp[1]] += 3
    #     else:
    #         if comp[0] not in map:
    #             map[comp[0]] = 3
    #         else:
    #             map[comp[0]] += 3
    #
    #     res_idx += 1
    #
    # winner = ""
    # max_score = 0
    #
    # for k, v in map.items():
    #     if v > max_score:
    #         winner = k
    #         max_score = v
    #
    # return winner



competitions = [
  ["HTML", "C#"],
  ["C#", "Python"],
  ["Python", "HTML"]
]
results = [0,0,1]

print(tournamentWinner(competitions, results))