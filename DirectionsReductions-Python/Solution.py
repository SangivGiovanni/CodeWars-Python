def dirReduc(arr):
    dic = {"NORTH": "SOUTH", "SOUTH": "NORTH", "EAST": "WEST", "WEST": "EAST"}
    result = []
    for i in arr:
        if result and dic[i] == result[-1]:
            result.pop()
        else:
            result.append(i)

    return result
