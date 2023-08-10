import random

def flip_coin():
    return random.choice(['Heads', 'Tails'])

def roll_die():
    return random.randint(1, 6)

def sample_population(population, sample_size):
    return random.sample(population, sample_size)

def sampling_and_random_variables():
    coin_flip_result = flip_coin()
    print("Coin flip result: ", coin_flip_result)

    die_roll_result = roll_die()
    print("Die roll result: ", die_roll_result)


    population = list(range(1, 101))
    sample_size = 10
    sample = sample_population(population, sample_size)
    print("Sample: ", sample)

sampling_and_random_variables()