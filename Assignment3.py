import csv
import matplotlib.pyplot as plt
import numpy as np

# Function 1: File I/O - Writing and Reading from a Text File
# Writes a list of numbers to a file and then reads them back as a list of integers.
def write_and_read_txt(filename, numbers):
    # open file in write mode
    opfile = open(filename, "w") 
    # write each number to the file, one number per line
    for n in numbers:
        opfile.write(str(n) + "\n")
    # close the file after writing
    opfile.close()

    # open file in read mode
    infile = open(filename, "r")
    # create empty list to store numbers 
    result = []
    # read all lines from file
    for line in infile.readlines():
        # remove newline character and convert string back to an integer
        result.append(int(line.strip()))
    # close file to save
    infile.close()
    # return list of integers we read from the file
    return result

# test function 1
numbers = [1,2,3,4]
result = write_and_read_txt("output.txt", numbers)

print("Function 1:")
print(result)

# Function 2: File I/O - Writing and Reading from a CSV File
# Writes a list of lists to a CSV file and reads it back.
def write_and_read_csv(filename, data):
    # open the file in write mode
    opfile = open(filename, "w")
    # write each row of data to the CSV file
    # join values with commas
    for row in data:
        opfile.write(",".join(str(x) for x in row) + "\n")
    # close file after writing
    opfile.close()

    # open CSV file in read mode
    infile = open(filename, "r")
    # create an empty list to store the rows read from a file
    result = []
    # read all lines from CSV file
    for line in infile.readlines():
        # remove newline and split the line by commas to get each value
        parts = line.strip().split(",")
        # convert eahc value in row from string back to integer
        result.append([int(x) for x in parts])
    # close the file after reading 
    infile.close()

    # return reconstructed list of lists
    return result

# test function 2
data = [[1,2,3], [4,5,6], [7,8,9]]
result = write_and_read_csv("output.csv", data)

print("Function 2:")
print(result) 


# Function 3: Reading an Array from a File
# Reads a space-separated array from a text file and converts it to a NumPy array.
def read_array_from_file(filename):
    # open file in read mode
    infile = open(filename, "r")
    # read entire file as one string and remove any extras spaces/ newlines
    line = infile.read().strip()
    # close the file after reading
    infile.close()
    # splti string by spaces to get each number separately
    parts = line.split()

    # convert each piece of text into a float and store in a list
    numbers = []
    for p in parts:
        numbers.append(float(p))

    # convert list of numbers into a Numpy array and return it
    return np.array(numbers)

# create a test file to check the function
file = open("test_array.txt", "w")
file.write("1.5 2.5 3.5 4.5 5.5")
file.close()

# test function
print("Function 3:")
result = read_array_from_file("test_array.txt")
print(result)

# Function 4: Plotting Data with plot() and show()
# This function plots a given list of numbers as a line graph.
def plot_data(numbers):
    # plot list of numbers as line graph
    # marker = 'o' creates 'o' at each data point
    # linestyle '-' connects points with a line
    plt.plot(numbers, marker='o', linestyle='-')
    # label x-axis
    plt.xlabel("X axis")
    # label y-axis
    plt.ylabel("Y axis")
    # name the graph
    plt.title("Line graph")
    # add grid in the background
    plt.grid(True)
    # display graph
    plt.show()

# test function
numbers = [1,2,3,4,5]
plt.figure()
plot_data(numbers)

# Function 5: Density Plot
# This function takes a list of numbers and plots a density plot.
def density_plot(data):
    # create histogram of data
    # bins=10 means the data is grouped into 10 intervals
    # density = true scales the histogram 
    plt.hist(data, bins = 10, density = True)
    # label x-axis
    plt.xlabel("Values")
    # label y-axis
    plt.ylabel("Density")
    # name the graph
    plt.title("Density Plot")
    # display the plot
    plt.show()

# test function using 1000 random values 
data = np.random.normal(0, 1, 1000)
# create new figure window before plotting
plt.figure()
density_plot(data)