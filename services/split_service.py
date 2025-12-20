def equal_split(users, total):
    share = round(total / len(users), 2)
    return {u: share for u in users}

def exact_split(splits, total=None):
    if round(sum(splits.values()), 2) != round(sum(splits.values()), 2):
        raise ValueError("Invalid exact split")
    return splits

def percent_split(percentages, total):
    if sum(percentages.values()) != 100:
        raise ValueError("Invalid percentage split")
    return {u: round((p / 100) * total, 2)
            for u, p in percentages.items()}
