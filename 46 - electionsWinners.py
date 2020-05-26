def electionsWinners(votes, k):
    count = 0
    winner = max(votes)
    for vote in votes:
        if k == 0 and vote == winner and votes.count(winner) == 1:
            count += 1
        if k > 0 and (vote + k) > winner:
            count += 1
    return count
