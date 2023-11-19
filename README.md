# How to use


## Import the decorator
Import the time_complexity() decorator.

```py
from plot_complexity import time_complexity
```
## use the decorator 
**Important:** The function will not return any value when this decorator is used.
Use the decorator with the function you want to plot the time complexity for. 

The first argument of the function should be the variable that determines the complexity of the function.

Example:

```py
@time_complexity()
def linear_complexity(iterations, *args, **kwargs):
    for i in range(iterations):
        continue

# call the function
linear_complexity()
```

In the above code execution time of the function will be computed for different **iterations** value.


**Important:** don't forgot to add (*args, kwargs) in the function arguments


## Adjust number of input values
You can specify the the range of input values in which the execution time of the function will be computed using decorator argument. 

Specify the range as 

    time_complexity(lower_bound, upper_bound)

    By default lower_bound = 1, upper_bound = 1000

Example:
```py
@time_complexity(100)
def quadratic_complexity(iterations, *args, **kwargs):
    for i in range(iterations):
        for j in range(iterations):
            continue
```


## Demonstration
simply run the demo.py file. It will show time complexities O(n) and O(n^2) using loops.

```bash
python3 demo.py
```

