# Install packages
import csv
import matplotlib.pyplot as plt
import numpy as np
import statistics
from scipy.stats import pearsonr
from scipy.stats import spearmanr
import plotly.express as px
import plotly.graph_objects as go

# Open and read the data
def list_data():
    data = []

    with open('test data.csv', 'r') as test_csv:
        spreadsheet = csv.DictReader(test_csv)
        for row in spreadsheet:
            data.append(row)

    return data

data = list_data()

# Getting a data list for each variable
def list_var(var):
    x = []
    for row in data:
        if row[var] != "":
            y = int(row[var])
            x.append(y)
    return x

fer_cap = list_var("Ferritin capillary")
fer_men = list_var("Ferritin menstrual")
hb_cap = list_var("Hb capillary")
hb_men = list_var("Hb menstrual")

# def list_participants(var):
#     x = []
#     y = 0
#     for row in data:
#         if row[var] != "":
#             y += 1
#             x.append(y)
#     return x
#
# num_participants = list_participants("Ferritin capillary")
# # print(num_participants)
#
# Mean and standard deviation calculations
def mean(var):
    z = statistics.mean(var)
    return z

def stand_dev(var):
    z = statistics.stdev(var, mean(var))
    return z
#
# print(f"Capillary ferritin:\n\tMean {mean(fer_cap)}\n"
#       f"\tStandard Deviation {stand_dev(fer_cap)}\n")
# print(f"Menstrual ferritin:\n\tMean {mean(fer_men)}\n"
#       f"\tStandard Deviation {stand_dev(fer_men)}\n")
# print(f"Capillary hemoglobin:\n\tMean {mean(hb_cap)}\n"
#       f"\tStandard Deviation {stand_dev(hb_cap)}\n")
# print(f"Menstrual hemoglobin:\n\tMean {mean(hb_men)}\n"
#       f"\tStandard Deviation {stand_dev(hb_men)}\n")
#
#
# # Graph time!
# def side_by_side_scat(cap,men):
#     x = np.array(cap)
#     y = np.array(men)
#
#     m, b = np.polyfit(x, y, 1)
#
#     plt.plot(x, y, 'o')
#     plt.plot(x, m*x+b, color='red')
#     plt.show()
#
# side_by_side_scat(fer_cap, fer_men)
# side_by_side_scat(hb_cap,hb_men)
#
#
# # It would be good to have separate graphs showing the mean and standard deviation
# def graph_mean_stand(var):
#     x = np.array(num_participants)
#     y = np.array(var)
#
#     fig, ax = plt.subplots()
#     ax.plot(x, y, 'o')
#     ax.plot(x, x*0+mean(var), color='green')
#     ax.fill_between(x, mean(var)+stand_dev(var), mean(var) - stand_dev(var), facecolor='grey')
#     plt.show()
#
# graph_mean_stand(fer_men)
# graph_mean_stand(hb_men)
#
# # Pearson take the floor
# class pearson:
#     def __init__(self,cap,men):
#         self.cap = cap
#         self.men = men
#
#     def calc_pearson(self):
#         x = np.array(self.cap)
#         y = np.array(self.men)
#
#         coef, pvalue = pearsonr(x, y)
#         return print(f"\tPearson Correlation Coefficient {coef}\n\tP-value {pvalue}\n")
#
# # Spearman time
# class spearman:
#     def __init__(self,cap,men):
#         self.cap = cap
#         self.men = men
#
#     def calc_spearman(self):
#         x = np.array(self.cap)
#         y = np.array(self.men)
#
#         coef, pvalue = spearmanr(x, y)
#         return print(f"\tSpearman Correlation Coefficient {coef}\n\tP-value {pvalue}\n")
#
# def fer_pearson_spearman():
#     x = pearson(fer_cap, fer_men)
#     y = spearman(fer_cap,fer_men)
#     print("Ferritin Correlation:")
#     x.calc_pearson()
#     y.calc_spearman()
#
# def hb_pearson_spearman():
#     x = pearson(hb_cap, hb_men)
#     y = spearman(hb_cap,hb_men)
#     print("Hemoglobin Correlation:")
#     x.calc_pearson()
#     y.calc_spearman()
#
# fer_pearson_spearman()
# hb_pearson_spearman()


# Attempting a Spearman graph


# I need to calculate mean and standard deviation and plot a graph showing that for the men data points
# This is so I can find the "calibration" numbers for the test

x_test = np.array(fer_men)
y_test = np.array(fer_cap)
fig = go.Figure(data=[go.Scatter(
    x=x_test,
    y=y_test,

    mode='markers')])


fig.show()

# fig = px.scatter(x)
# fig.show()

