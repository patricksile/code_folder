import matplotlib.pyplot as plt

# Output Directory
output_dir = "/home/choupi/D/codes/python_crash_course/"

# Input values

x_values = list(range(1,1001))
y_values = [x**3 for x in x_values]

plt.scatter(x_values, y_values, c=y_values, cmap='viridis', edgecolors='none', s=40)

# Set chat title and label axes.

plt.title("Cube Numbers", fontsize=26)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Cube of Values", fontsize=14)

# Set the range for each axis.
plt.axis([0, 1050, 0, 1050**3])

# Set size of tick labels.
plt.tick_params(axis='both', which='major', labelsize=14)
plt.savefig('{}cube_plot_to_1000.png'.format(output_dir), bbox_inches='tight')
