def snail(snail_map):

    n = len(snail_map)
    # m is the iteration count number.
    m = 1
    # r and q are used to control how many terms per iteration.
    r = n
    q = -1
    res = []
    # c and z are the indexing for snail_map.
    c = 1
    z = n - 1

    if m == 1:
        for item in snail_map[0]:
            res.append(item)
    m += 1

    while 1 < m < 2 * n:

        while c < r:
            res.append(snail_map[c][z])
            if c + 1 < r:
                c += 1
            else:
                break
        m += 1
        z -= 1
        while z > q:
            res.append(snail_map[c][z])
            if z - 1 > q:
                z -= 1
            else:
                break
        m += 1
        q += 1
        r -= 1
        c -= 1
        while c > q:
            res.append(snail_map[c][z])
            if c - 1 > q:
                c -= 1
            else:
                break
        m += 1
        z += 1
        while z < r:
            res.append(snail_map[c][z])
            if z + 1 < r:
                z += 1
            else:
                break
        m += 1
        c += 1

    return res
