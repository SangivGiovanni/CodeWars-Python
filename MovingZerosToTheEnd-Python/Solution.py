def move_zeros(arr):

    z = [val for val in arr if val == 0 and val is not False]
    a = [val for val in arr if val != 0 or val is False]

    return a + z
