

## MEAN
def calculate_mean(data):
    total = sum(data)
    mean = total / len(data)
    print("MEAN SCore", mean)

data = [85, 90, 92, 88, 95]
mean = calculate_mean(data)


##MEADIAN
def calculate_median(data):
    sorted_data = sorted(data)
    n = len(sorted_data)
    if n % 2 == 0:
        median = (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2
    else:
        median = sorted_data[n // 2]
    print("Median: ", median)

data = [12, 9, 7, 15, 13, 8]
calculate_median(data)


##MODE

def calculate_mode(data):
    count_dict = {}
    for value in data:
        count_dict[value] = count_dict.get(value, 0) + 1
    max_count = max(count_dict.values())
    modes = [value for value, count in count_dict.items() if count == max_count]
    print("Mode: ", modes)

data = [7, 9, 7, 12, 9, 15, 9]
calculate_mode(data)


##RANGE
def calculate_range(data):
    data_range = max(data) - min(data)
    print("RANGE",data_range)
data = [45, 68, 32, 90, 75]
calculate_range(data)

##Correlation
def mean(data):
    return sum(data) / len(data)

def correlation_coefficient(x, y):
    if len(x) != len(y):
        raise ValueError("Data sets must have the same length.")

    n = len(x)
    mean_x = mean(x)
    mean_y = mean(y)

    numerator = sum((x[i] - mean_x) * (y[i] - mean_y) for i in range(n))
    denominator_x = sum((x[i] - mean_x) ** 2 for i in range(n))
    denominator_y = sum((y[i] - mean_y) ** 2 for i in range(n))

    correlation = numerator / (denominator_x ** 0.5 * denominator_y ** 0.5)
    print("Correlation coefficient:", correlation)


data_x = [1, 2, 3, 4, 5]
data_y = [2, 4, 6, 8, 10]
correlation_coefficient(data_x, data_y)

    
    
