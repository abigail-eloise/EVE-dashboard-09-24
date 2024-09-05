# Install packages
import csv
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statistics
from scipy.stats import pearsonr


# Open and read the data
def list_data():
    data = []

    with open('test data.csv', 'r') as test_csv:
        spreadsheet = csv.DictReader(test_csv)
        for row in spreadsheet:
            data.append(row)

    return data

data = list_data()


# I want to know how many participants we have data for
def sum_particpants():
    x = 0
    for row in data:
        if row["Ferritin capillary"] != "":
            x += 1

    print(x)


# sum_particpants()

def mean_fer_cap():
    x = []
    for row in data:
        if row["Ferritin capillary"] != "":
            y = int(row["Ferritin capillary"])
            x.append(y)

    z = statistics.mean(x)
    return z

# print(f"Mean value ferritin in capillary blood: {mean_fer_cap()}")

def mean_fer_men():
    x = []
    for row in data:
        if row["Ferritin menstrual"] != "":
            y = int(row["Ferritin menstrual"])
            x.append(y)

    z = statistics.mean(x)
    return z

# print(f"Mean value ferritin in menstrual blood: {mean_fer_men()}")

def mean_hb_cap():
    x = []
    for row in data:
        if row["Hb capillary"] != "":
            y = int(row["Hb capillary"])
            x.append(y)

    z = statistics.mean(x)
    return z

# print(f"Mean value hemoglobin in capillary blood: {mean_hb_cap()}")

def mean_hb_men():
    x = []
    for row in data:
        if row["Hb menstrual"] != "":
            y = int(row["Hb menstrual"])
            x.append(y)

    z = statistics.mean(x)
    return z

# print(f"Mean value Hemoglobin in menstrual blood: {mean_hb_men()}")


# Let#s make some graphs!
# Starting with comparing ferritin cap and men blood

def side_by_side_graph_fer():
    x = []
    for row in data:
        if row["Ferritin capillary"] != "":
            d = int(row["Ferritin capillary"])
            x.append(d)

    y = []
    for row in data:
        if row["Ferritin menstrual"] != "":
            c = int(row["Ferritin menstrual"])
            y.append(c)

    plt.scatter(x,y)
    plt.show()

# side_by_side_graph_fer()

def side_by_side_graph_hb():
    x = []
    for row in data:
        if row["Hb capillary"] != "":
            d = int(row["Hb capillary"])
            x.append(d)

    y = []
    for row in data:
        if row["Hb menstrual"] != "":
            c = int(row["Hb menstrual"])
            y.append(c)

    plt.scatter(x,y)
    plt.show()

# side_by_side_graph_hb()


# Attempt at Pearson r
def pearson_fer():
    x = []
    for row in data:
        if row["Ferritin capillary"] != "":
            d = int(row["Ferritin capillary"])
            x.append(d)

    y = []
    for row in data:
        if row["Ferritin menstrual"] != "":
            c = int(row["Ferritin menstrual"])
            y.append(c)

    corr_coef, pvalue = pearsonr(x,y)
    print(f"Correlation coefficient for Ferritin: {corr_coef}\nP-value for ferritin: {pvalue}")

# pearson_fer()

# x = []
# for row in data:
#     if row["Ferritin capillary"] != "":
#         y = int(row["Wonderful Women"])
#         x.append(y)
# print(x)

# x = []
# for row in data:
#     if row["Wonderful Women"] != "":
#         y = row["Wonderful Women"]
#         x.append(y)
# print(x)