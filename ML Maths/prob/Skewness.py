
def calculate_skewness(dataset):
    n = len(dataset)
    mean = sum(dataset) / n
    sum_squared_deviations = sum((x - mean) ** 2 for x in dataset)
    sum_cubed_deviations = sum((x - mean) ** 3 for x in dataset)
    denominator = (n - 1) * (n - 2) * (sum_squared_deviations / n) ** (3/2)
    skewness = (n * sum_cubed_deviations) / denominator
    print("Skewness: ", skewness)    

dataset = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
calculate_skewness(dataset)
