#Write a python script which loads the dataset, parses the information, and 
#uses it to calculate the average interest rates for each of the listed purposes.
#Plot the results onto a graph.

#To run, python get_avg_int_rate.py

import csv
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# Load and parse CSV
print("Loading and parsing CSV")
int_rate_dict = {}

with open('data.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if row["purpose"] not in int_rate_dict:
            int_rate_dict[row["purpose"]] = list()
        int_rate_dict[row["purpose"]].append(float(row["int_rate"]))

# TODO: save this as a CSV or pandas dataframe
# Calculate average interest rate
print("Calculating average interest rate per purpose")
avg_int_rate = {}

for key in int_rate_dict.keys():
    sum = 0
    num_loans = len(int_rate_dict[key])
    for int_rate in int_rate_dict[key]:
        sum += int_rate
    avg = sum / num_loans
    avg_int_rate[key] = avg

#TODO: add x axis label and y axis label
# Plot graph
print("Plotting graph")
plt.bar(range(len(avg_int_rate)), avg_int_rate.values(), align='center')
plt.xticks(range(len(avg_int_rate)), avg_int_rate.keys(), rotation=60, fontsize='small', horizontalalignment='right')
plt.title("Average Interest Rate per Loan Purpose")
plt.tight_layout(pad=2)
plt.show()