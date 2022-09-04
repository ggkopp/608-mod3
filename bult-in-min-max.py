def maximum(value1, value2, value3):
    max_value = value1
    if  value2 > max_value:
        max_value = value2
    if value3 > max_value:
        max_value = value3
    return max_value

print(maximum(12, 27, 36))

def minimum(value1, value2, value3):
    min_value = value1
    if  value2 < min_value:
        min_value = value2
    if value3 < min_value:
        min_value = value3
    return min_value

print(minimum(12.3, 45.6, 9.7))

print('Garrett Kopp')


