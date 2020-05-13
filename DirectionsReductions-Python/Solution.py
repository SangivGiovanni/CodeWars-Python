def dirReduc(arr):
    dic = {"NORTH": "SOUTH", "SOUTH": "NORTH", "EAST": "WEST", "WEST": "EAST"}
    result = []
    for j in arr:
        if result and dic[j] == result[-1]:
            result.pop()
        else:
            result.append(j)

    return result
