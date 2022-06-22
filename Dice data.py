import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random

dice_result = []

for i in range(0,1000):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice_result.append(dice1 + dice2)

mean = sum(dice_result) / len(dice_result)
median = statistics.median(dice_result)
mode = statistics.mode(dice_result)
std_dev = statistics.stdev(dice_result)

first_std_dev_start, first_std_dev_end = mean - std_dev, mean + std_dev
second_std_dev_start, second_std_dev_end = mean - (2 *std_dev), mean + (2 *std_dev)
third_std_dev_start, third_std_dev_end = mean - (3 *std_dev), mean + (3 *std_dev)

fig = ff.create_distplot([dice_result],["Result"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines",name = "MEAN"))

fig.show()





