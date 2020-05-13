def who_is_next(names, r):

    inner_bound = 0
    upper_bound = len(names)
    cycle = 0
    multiplyer = len(names)

    while not inner_bound < r <= upper_bound:
        cycle += 1
        inner_bound = upper_bound
        multiplyer *= 2
        upper_bound += multiplyer

    for i, j in enumerate(names):
        if i * 2 ** cycle < r - inner_bound <= (i + 1) * 2 ** cycle:
            return j
