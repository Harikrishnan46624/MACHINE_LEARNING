
import random

def roll_die():
    return random.randint(1 ,6)

def calculate_sample_mean(sample):
    return sum(sample) / len(sample)

def cenrral_limit_theorm():
    population = [roll_die()for _ in range(1000)]
    sample_means = []
    sample_size = 30
    num_samples = 1000

    for _ in range(num_samples):
        sample = random.sample(population, sample_size)
        sample_mean = calculate_sample_mean(sample)
        sample_means.append(sample_mean)

    population_mean = calculate_sample_mean(population)
    sample_means_mean = calculate_sample_mean(sample_means)

    print("Population mean: ", population_mean)
    print("MEan of sample: ", sample_means_mean)

cenrral_limit_theorm()