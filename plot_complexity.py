import time
import matplotlib.pyplot as plt

def time_complexity(lower_bound=1, upper_bound=1000):
    def decorator(func):
        def wrapper(*args, **kwargs):
            time_taken = []
            iterations = list(range(lower_bound, upper_bound))

            for i in iterations:
                start_time = time.time()
                result = func(i, *args, **kwargs)
                end_time = time.time()
                time_taken.append(end_time - start_time)
            
            # plot the graph
            x = iterations
            y = time_taken
            plt.plot(x, y)
            plt.xlabel('length of input')
            plt.ylabel('time taken')
            plt.show()
        return wrapper
    return decorator


if __name__ == '__main__':
    print("Running time_complexity.py file. This file is not meant to be run directly.")