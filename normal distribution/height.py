import csv
import plotly.figure_factory as ff
import pandas as px
import statistics

df=px.read_csv("height.csv")

height_list=df["Height(Inches)"].to_list()

weight_list=df["Weight(Pounds)"].to_list()

#mean for height and weight

height_mean=statistics.mean(height_list)
weight_mean=statistics.mean(weight_list)

#median for height and weight

height_median=statistics.median(height_list)
weight_median=statistics.median(weight_list)

#mode for height and weight

height_mode=statistics.mode(height_list)
weight_mode=statistics.mode(weight_list)

#sd for height and weight

height_sd=statistics.stdev(height_list)
weight_sd=statistics.stdev(weight_list)

print("mean,meadian and mode height is {},{},{}".format(height_mean,height_median,height_mode))
print("mean,meadian and mode weight is {},{},{}".format(weight_mean,weight_median,weight_mode))

height_1st_sd_start,height_1st_sd_end=height_mean-height_sd,height_mean+height_sd

height_list_of_data_within_1_sd=[result for result in height_list if result>height_1st_sd_start and result<height_1st_sd_end]
print("{}% percentage of data which lies between 1st sd is".format(len(height_list_of_data_within_1_sd)*100.0/len(height_list)))

