from plot_complexity import time_complexity

@time_complexity()
def linear_complexity(iterations, *args, **kwargs):
    for i in range(iterations):
        continue

@time_complexity(lower_bound=10, upper_bound=100)
def quadratic_complexity(iterations, *args, **kwargs):
    for i in range(iterations):
        for j in range(iterations):
            continue

linear_complexity()
quadratic_complexity()