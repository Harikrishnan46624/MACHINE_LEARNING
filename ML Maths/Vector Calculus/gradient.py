

def f(x, y):
    return 3 * x ** 2 + 2 * y ** 3

x = 2
y = 3

delta = 1e-6 # A small value for numerical differentiation

df_dx = (f(x + delta, y)- f(x- delta, y)) / (2 * delta)
df_dy = (f(x, y + delta) - f(x,y - delta)) / (2 * delta)

print("Gradient with respect to x", df_dx)
print("Gradient with respect to y", df_dy)