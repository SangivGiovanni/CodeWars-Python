def v(k, n):
    return (1.0/k)*(n+1)**(-2*k)


def doubles(maxk, maxn):
    total = 0
    for k in range(1, maxk + 1):
        for n in range(1, maxn + 1):
            total += v(k, n)

    return total
