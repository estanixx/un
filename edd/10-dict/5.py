person_votes = dict()
vote_count = {0: 0}
while (cmd:=input()) != '0 0':
    person, vote = map(int, cmd.split())
    # Ya votó.
    if person_votes.get(person) is not None:
        last_vote = person_votes[person]
        vote_count[last_vote] -= 1
        person_votes[person] = 0
    else:
        person_votes[person] = vote
        if vote_count.get(vote) is None:
            vote_count[vote] = 1
        else:
            vote_count[vote] += 1
sorted_votes = sorted(vote_count.items(), key=lambda a: (a[1], a[0]), reverse=True)
for doc, votes in sorted_votes:
    if votes > 0:
        print(doc, votes)