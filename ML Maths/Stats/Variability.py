
def range(data):
    return max(data) - min(data)

def interquartile_range(data):
    sorted_data = sorted(data)
    n = len(sorted_data)
    lower_quartile = sorted_data[n // 4]
    upper_quartile = sorted_data[(3 * n) // 4]
    return upper_quartile - lower_quartile

i = interquartile_range([1,2,3,4,5,6])
print(i)