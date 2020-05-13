def max_sequence(arr):
    n = []

    for i in range(0, len(arr) + 1):
        for j in range(i, len(arr) + 1):
            no = sum(arr[i:j])
            n.append(no)

    return max(n)
