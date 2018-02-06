def evaluate_poly(poly, x):
    '''evaluate_poly(poly, x) -> f
    poly:   tuple of numbers, length > 0
    x:      float

    return the polynomial value'''
    f = 0
    df = 0
    for i, item in enumerate(poly):
        f += item*x**i
    return f

def compute_deriv(poly):
    df = ()
    for i, item in enumerate(poly):
        if i != 0:
            df += (i*item, )
    return df

def compute_root(poly, x_0, epsilon):
    x1 = x_0+2*epsilon
    count = 0
    while abs(evaluate_poly(poly, x_0)) > epsilon:
        x_0 = x1
        count += 1
        x1 = x_0-evaluate_poly(poly, x_0)/evaluate_poly(compute_deriv(poly), x_0)
    return x1, count

poly = (-13.39, 0.0, 17.5, 3.0, 1.0)
x_0 = 0.1
epsilon = .0001
print compute_root(poly, x_0, epsilon)
