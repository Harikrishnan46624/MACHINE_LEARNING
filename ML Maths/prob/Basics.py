import random

# Function to simulate flipping a fair coin
def flip_coin():
    return random.choice(['Heads', 'Tails'])

# Function to calculate the probability of an event
def calculate_probability(favorable_outcomes, total_outcomes):
    return favorable_outcomes / total_outcomes

# Function to demonstrate the addition rule of probability
def addition_rule():
    event_A = 0.4
    event_B = 0.3
    union_AB = event_A + event_B
    print("Probability of A or B:", union_AB)

# Function to demonstrate the multiplication rule of probability
def multiplication_rule():
    event_A = 0.6
    event_B_given_A = 0.4

    intersection_AB = event_A * event_B_given_A
    print("Probability of A and B:", intersection_AB)

# Function to demonstrate conditional probability
def conditional_probability():
    event_A = 0.6
    event_B = 0.3
    event_B_given_A = 0.2

    probability_A_given_B = (event_B_given_A * event_A) / event_B
    print("Probability of A given B:", probability_A_given_B)

# Function to demonstrate the concept of sampling
def sampling():
    population = list(range(1, 101))
    sample_size = 10
    sample = random.sample(population, sample_size)
    print("Sample:", sample)

# Function to calculate the range of a dataset
def calculate_range(dataset):
    return max(dataset) - min(dataset)

# Function to calculate the interquartile range (IQR) of a dataset
def calculate_iqr(dataset):
    dataset.sort()
    q1 = dataset[int(len(dataset) * 0.25)]
    q3 = dataset[int(len(dataset) * 0.75)]
    return q3 - q1

# Function to demonstrate calculating skewness
def calculate_skewness(dataset):
    mean = sum(dataset) / len(dataset)
    std_dev = (sum((x - mean) ** 2 for x in dataset) / len(dataset)) ** 0.5
    skewness = sum((x - mean) ** 3 for x in dataset) / (len(dataset) * std_dev ** 3)
    return skewness

# Example usage
if __name__ == "__main__":
    coin_flip_result = flip_coin()
    print("Coin flip result:", coin_flip_result)

    event_favorable_outcomes = 4
    event_total_outcomes = 10
    probability = calculate_probability(event_favorable_outcomes, event_total_outcomes)
    print("Probability:", probability)

    addition_rule()

    multiplication_rule()

    conditional_probability()

    sampling()

    dataset = [25, 32, 18, 42, 29, 37, 21, 44, 26, 31]
    range_value = calculate_range(dataset)
    print("Range:", range_value)

    iqr_value = calculate_iqr(dataset)
    print("Interquartile Range (IQR):", iqr_value)

    skewness = calculate_skewness(dataset)
    print("Skewness:", skewness)
