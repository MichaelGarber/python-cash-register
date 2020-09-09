def get_total(*cid):
    total = 0
    for row in cid:
        for column in row:
            total += column[1]
    return total


def check_cash_register(price, cash, *cid):
    total = get_total(*cid)
    status = ''
    if cash - price == total:
        status = "CLOSED"
    if cash - price > total:
        status = "INSUFFICIENT_FUNDS"
    if cash - price < total:
        status = "OPEN"

    give = cash - price

    money = [
        0.01,
        0.05,
        0.1,
        0.25,
        1,
        5,
        10,
        20,
        100
    ]

    for row in cid:
        pos = len(row) - 1
    change = [
        ["PENNY", 0],
        ["NICKEL", 0],
        ["DIME", 0],
        ["QUARTER", 0],
        ["ONE", 0],
        ["FIVE", 0],
        ["TEN", 0],
        ["TWENTY", 0],
        ["ONE HUNDRED", 0]
    ]

    while (give > 0 and pos > -1):
        money[pos] = round(money[pos], 2)
        give = round(give, 2)
        cid[0][pos][1] = round(cid[0][pos][1], 2)
        change[pos][1] = round(change[pos][1], 2)
        if money[pos] <= give and cid[0][pos][1] > 0:
            give = give - money[pos]
            cid[0][pos][1] = cid[0][pos][1] - money[pos]
            change[pos][1] = change[pos][1] + money[pos]

        else:
            cid[0][pos][1] = round(cid[0][pos][1], 2)
            give = round(give, 2)
            pos -= 1


    if status == 'OPEN':
        change = [c for c in change if c[1] != 0]
    change = sorted(change, key=lambda l: l[1], reverse=True)
    if (give > 0):
        change = []
        status = "INSUFFICIENT_FUNDS"
        return {'status': status, "change": change}

    return {'status': status, "change": change}
