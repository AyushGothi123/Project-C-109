import random
import plotly.express as px
import plotly.figure_factory as ff
import statistics
import plotly.graph_objects as go
import pandas as pd
import csv

df = pd.read_csv("a.csv")
with open("a.csv") as f:
    data = csv.DictReader(f)
    marks = []

with open("a.csv") as f:
    data = csv.DictReader(f)

    for row in data:
       marks.append(float(row["reading score"]))

mean = sum(marks)/len(marks)
print(mean)
sd = statistics.stdev(marks)
print(statistics.mode(marks))
print(statistics.median(marks))

st_start1,st_end1 = mean-sd,mean+sd
st_start2,st_end2 = mean-(2*sd),mean+(2*sd)
st_start3,st_end3 = mean-(3*sd),mean+(3*sd)

sd1_ls = [result for result in marks if result > st_start1 and result < st_end1]
sd2_ls = [result for result in marks if result > st_start2 and result < st_end2]
sd3_ls = [result for result in marks if result > st_start3 and result < st_end3]


print("{}% is data within std1 ".format(len(sd1_ls)*100/len(marks)))
print("{}% is data within std2 ".format(len(sd2_ls)*100/len(marks)))
print("{}% is data within std3 ".format(len(sd3_ls)*100/len(marks)))

fig = ff.create_distplot([df["reading score"].tolist()],["marks"],show_hist = False)
fig.add_trace(go.Scatter(x = [mean,mean],y=  [0,0.17],mode = "lines",name ="mean"))
fig.add_trace(go.Scatter(x = [st_start1,st_start1],y = [0,0.17],mode = "lines",name = "stdv1"))
fig.add_trace(go.Scatter(x = [st_start2,st_start2],y = [0,0.17],mode = "lines",name = "stdv2"))
fig.add_trace(go.Scatter(x = [st_start3,st_start3],y = [0,0.17],mode = "lines",name = "stdv3"))

fig.add_trace(go.Scatter(x = [st_end1,st_end1],y = [0,0.17],mode = "lines",name = "stdv1end"))
fig.add_trace(go.Scatter(x = [st_end2,st_end2],y = [0,0.17],mode = "lines",name = "stdv2end"))
fig.add_trace(go.Scatter(x = [st_end3,st_end3],y = [0,0.17],mode = "lines",name = "stdv3end"))
fig.show()
