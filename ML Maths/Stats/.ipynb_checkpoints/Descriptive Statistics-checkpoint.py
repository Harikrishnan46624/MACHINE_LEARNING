
def mean(data):
    return sum(data) / len(data)

def median(data):
    sorted_data = sorted(data)
    n = len(data)
    if n%2 == 0:
        return(sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2
    else:
        return sorted_data[n // 2]
    
def mode(data):
    counts = {}
    for value in data:
        counts[value] = counts.get(value, 0) + 1
    max_count = max(counts.values())
    modes = [value for value, count in counts.items() if count == max_count]
    return modes

def range(data):
    return max(data) - min(data)

def varience(data):
    data_mean = mean(data)
    diff = [(x - data_mean) ** 2 for x in data]
    return sum(diff) / len(data)

def standerd_deviation(data):
    return varience(data) ** 0.5