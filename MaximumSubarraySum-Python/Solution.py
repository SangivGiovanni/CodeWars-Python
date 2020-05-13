def max_sequence(arr):
    m = []

    for i in range(0, len(arr) + 1):
        for j in range(i, len(arr) + 1):
            no = sum(arr[i:j])
            m.append(no)

    return max(m)
