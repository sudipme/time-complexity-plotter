import time
import matplotlib.pyplot as plt

# Create an array to store values from 1 to 10000
values = list(range(1, 10000))
time_taken = []

for n in values:
    start_time = time.time()
    for i in range(n):
        continue
    end_time = time.time()
    
    time_taken.append((end_time - start_time)) 



x_axis = values
y_axis = time_taken

# Plotting the data
plt.plot(x_axis, y_axis)
plt.xlabel('n values')
plt.ylabel('time taken')

# Displaying the plot
plt.show()