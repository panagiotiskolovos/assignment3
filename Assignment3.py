import csv
import matplotlib.pyplot as plt
import numpy as np

# Function 1: File I/O - Writing and Reading from a Text File
# Writes a list of numbers to a file and then reads them back as a list of integers.
def write_and_read_txt(filename, numbers):
    opfile = open(filename, "w")
    for n in numbers:
        opfile.write(str(n) + "\n")
    opfile.close()

    infile = open(filename, "r")
    result = []
    for line in infile.readlines():
        result.append(int(line.strip()))
    infile.close()

    return result

# test function 1
numbers = [1,2,3,4]
result = write_and_read_txt("output.txt", numbers)
print("Function 1:")
print(result)


# Function 2: File I/O - Writing and Reading from a CSV File
# Writes a list of lists to a CSV file and reads it back.
def write_and_read_csv(filename, data):
    opfile = open(filename, "w")
    for row in data:
        opfile.write(",".join(str(x) for x in row) + "\n")
    opfile.close()

    infile = open(filename, "r")
    result = []
    for line in infile.readlines():
        parts = line.strip().split(",")
        result.append([int(x) for x in parts])
    infile.close()

    return result

# test function 2
data = [[1,2,3], [4,5,6], [7,8,9]]
result = write_and_read_csv("output.csv", data)
print("Function 2:")
print(result) 


# Function 3: Reading an Array from a File
# Reads a space-separated array from a text file and converts it to a NumPy array.
def read_array_from_file(filename):
    infile = open(filename, "r")
    line = infile.read().strip()
    infile.close()

    parts = line.split()

    numbers = []
    for p in parts:
        numbers.append(float(p))

    return np.array(numbers)

file = open("test_array.txt", "w")
file.write("1.5 2.5 3.5 4.5 5.5")
file.close()

print("Function 3:")
result = read_array_from_file("test_array.txt")
print(result)

# Function 4: Plotting Data with plot() and show()
# This function plots a given list of numbers as a line graph.
def plot_data(numbers):
    plt.plot(numbers, marker='o', linestyle='-')
    plt.title("Line graph")
    plt.grid(True)
    plt.show()

numbers = [1,2,3,4,5]
plt.figure()
plot_data(numbers)

# Function 5: Density Plot
# This function takes a list of numbers and plots a density plot.
def density_plot(data):
    plt.hist(data, bins = 10, density = True)
    plt.title("Density Plot")
    plt.show()

data = np.random.normal(0, 1, 1000)
plt.figure()
density_plot(data)