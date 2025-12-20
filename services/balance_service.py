from collections import defaultdict

balances = defaultdict(lambda: defaultdict(float))

def update_balance(paid_by, splits):
    for user, amount in splits.items():
        if user == paid_by:
            continue

        # user owes paid_by
        balances[user][paid_by] += amount

        # NETTING LOGIC (THIS IS THE FIX)
        if balances[paid_by][user] > 0:
            min_amt = min(balances[user][paid_by], balances[paid_by][user])
            balances[user][paid_by] -= min_amt
            balances[paid_by][user] -= min_amt

def simplify():
    net = defaultdict(float)

    for debtor in balances:
        for creditor, amount in balances[debtor].items():
            net[debtor] -= amount
            net[creditor] += amount

    debtors = [[u, -amt] for u, amt in net.items() if amt < 0]
    creditors = [[u, amt] for u, amt in net.items() if amt > 0]

    result = []
    i = j = 0

    while i < len(debtors) and j < len(creditors):
        pay = min(debtors[i][1], creditors[j][1])
        result.append({
            "from": debtors[i][0],
            "to": creditors[j][0],
            "amount": pay
        })

        debtors[i][1] -= pay
        creditors[j][1] -= pay

        if debtors[i][1] == 0: i += 1
        if creditors[j][1] == 0: j += 1

    return result
