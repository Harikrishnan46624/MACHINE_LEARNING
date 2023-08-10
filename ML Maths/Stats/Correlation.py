
def mean(data):
    return sum(data) / len(data)

def correlation(x, y):
    mean_x = mean(x)
    mean_y = mean(y)
    dif_prod = [(xi - mean_x) * (yi - mean_y) for xi, yi in zip(x, y)]
    dif_prod_mean = sum(dif_prod) / len(x)

    x_diff_sq = [(xi - mean_x) ** 2 for xi in x]
    y_diff_sq = [(yi - mean_y) ** 2 for yi in y]
    x_diff_sq_mean = sum(x_diff_sq) / len(x)
    y_diff_sq_mean = sum(y_diff_sq) / len(y)

    correlation = dif_prod_mean / (x_diff_sq_mean ** 0.5 * y_diff_sq_mean ** 0.5)
    print(correlation)

x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
correlation(x,y)