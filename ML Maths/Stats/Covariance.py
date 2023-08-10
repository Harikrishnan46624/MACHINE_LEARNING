
def mean(data):
    return sum(data) / len(data)

def covarience(x, y):
    mean_x = mean(x)
    mean_y = mean(y)
    diff_prod = [(xi - mean_x) * (yi - mean_y) for xi, yi in zip(x, y)]
    covarience = sum(diff_prod) / len(x)
    print(covarience)

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
covarience(x , y)