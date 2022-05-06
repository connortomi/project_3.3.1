#program to visualize cancer fatalities
#from years 1990-2019

import matplotlib.pyplot as plt
import pandas as pd
import turtle as t

# Load in the data with read_csv()
cancer_data = pd.read_csv("Data on Fatalities Per Year (1990-2019) in the USA - Connor Tomita - Sheet1.csv", header=0)   # identify the header row

#plot liver cancer deaths
plt.ylabel('Number of Fatalities')
plt.xlabel('Years (1990-2019)')
plt.title('Fatality Rates of Different Cancers in the USA')

#create screen for key
width = 800
height = 800
wn = t.Screen()
wn.screensize(width, height)
wn.setup(width, height)

#use turtles to draw key 
key_letter_drawer = t.Turtle()
key_letter_drawer.hideturtle()
key_letter_drawer.penup()
key_letter_drawer.goto(0, 360)

#create user defined funct to 
#shorten letter repositioning
def key_change_position():
  key_letter_drawer.penup()
  key_drawer_ychange = key_letter_drawer.ycor()-40
  key_letter_drawer.goto(-150, key_drawer_ychange)
  key_letter_drawer.pendown()

#write cancers for color key 
key_letter_drawer.pendown()
key_letter_drawer.write("Key:", font=("Arial", 15, "bold"))
key_change_position()
key_letter_drawer.write("Liver Cancer -", font=("Arial", 15, "bold"))
key_change_position()
key_letter_drawer.write("Colon and Rectum -", font=("Arial", 15, "bold"))
key_change_position()
key_letter_drawer.write("Leukemia -", font=("Arial", 15, "bold"))
key_change_position()
key_letter_drawer.write("Prostate -", font=("Arial", 15, "bold"))
key_change_position()
key_letter_drawer.write("Bladder -", font=("Arial", 15, "bold"))
key_change_position()
key_letter_drawer.write("Pancreatic -", font=("Arial", 15, "bold"))
key_change_position()
key_letter_drawer.write("Breast -", font=("Arial", 15, "bold"))
key_change_position()
key_letter_drawer.write("Non-Hodgkin -", font=("Arial", 15, "bold"))

#use turtles to add colored shapes for key
key_shape_drawer = t.Turtle()
key_shape_drawer.hideturtle()
key_shape_drawer.speed(0)
key_shape_drawer.penup()
key_shape_drawer.goto(20, 320)
key_shape_drawer.fillcolor("gray")
key_shape_drawer.begin_fill()
key_shape_drawer.circle(15)
key_shape_drawer.end_fill()
key_shape_drawer.goto(80, 280)
key_shape_drawer.fillcolor("blue")
key_shape_drawer.begin_fill()
key_shape_drawer.circle(15)
key_shape_drawer.end_fill()
key_shape_drawer.goto(-10, 240)
key_shape_drawer.fillcolor("red")
key_shape_drawer.begin_fill()
key_shape_drawer.circle(15)
key_shape_drawer.end_fill()
key_shape_drawer.goto(-15, 200)
key_shape_drawer.fillcolor("green")
key_shape_drawer.begin_fill()
key_shape_drawer.circle(15)
key_shape_drawer.end_fill()
key_shape_drawer.goto(-20, 160)
key_shape_drawer.fillcolor("cyan")
key_shape_drawer.begin_fill()
key_shape_drawer.circle(15)
key_shape_drawer.end_fill()
key_shape_drawer.goto(0, 120)
key_shape_drawer.fillcolor("yellow")
key_shape_drawer.begin_fill()
key_shape_drawer.circle(15)
key_shape_drawer.end_fill()
key_shape_drawer.goto(-40, 80)
key_shape_drawer.fillcolor("pink")
key_shape_drawer.begin_fill()
key_shape_drawer.circle(15)
key_shape_drawer.end_fill()
key_shape_drawer.goto(20, 40)
key_shape_drawer.fillcolor("black")
key_shape_drawer.begin_fill()
key_shape_drawer.circle(15)
key_shape_drawer.end_fill()

#create and setup turtle for statistic writer
statistic_writer = t.Turtle()
statistic_writer.hideturtle()
statistic_writer.speed(0)
statistic_writer.penup()
statistic_writer.goto(-15, -40)
statistic_writer.write("Statistics:", font=("Arial", 15, "bold"))

#stat writer position change function
def stat_change_position():
  statistic_writer.penup()
  stat_writer_ychange = statistic_writer.ycor()-20
  statistic_writer.goto(-380, stat_writer_ychange)
  statistic_writer.pendown()

#LIVER MIN MAX AVR variables defined
lowest_fatalities = cancer_data['Liver'][0]
highest_fatalities = cancer_data['Liver'][0]
min_year = cancer_data['Year'][0]
max_year = cancer_data['Year'][0]
sum_fatalities = 0
avg_fatalities = 0

#calculate minimum, maximum and average fatalities
#for liver cancer
for i in range(len(cancer_data['Liver'])):
    if (cancer_data['Liver'][i] > highest_fatalities):
        highest_fatalities = cancer_data['Liver'][i]
        max_year = cancer_data['Year'][i]
    if (cancer_data['Liver'][i] < lowest_fatalities):
        lowest_fatalities = cancer_data['Liver'][i]
        min_year = cancer_data['Year'][i]
    sum_fatalities += cancer_data['Liver'][i]

avg_fatalities = sum_fatalities/len(cancer_data['Liver'])

#write statistics for colon/rectum cancer
liver_most = "Most fatalities per year:", highest_fatalities, "occured in", max_year
statistic_writer.goto(-380, -80)
statistic_writer.pencolor("gray")
statistic_writer.write(liver_most, font=("Arial", 9, "bold"))
stat_change_position()
liver_least = "Least fatalities per year:", lowest_fatalities, "occured in", min_year
statistic_writer.write(liver_least, font=("Arial", 9, "bold"))
stat_change_position()
liver_average = "The average fatalities per year was:", avg_fatalities
statistic_writer.write(liver_average, font=("Arial", 9, "bold"))

#COLON/RECTUM MIN MAX AVR variables defined
lowest_fatalities2 = cancer_data['Colon and Rectum'][0]
highest_fatalities2 = cancer_data['Colon and Rectum'][0]
min_year2 = cancer_data['Year'][0]
max_year2 = cancer_data['Year'][0]
sum_fatalities2 = 0
avg_fatalities2 = 0

#calculate minimum, maximum and average fatalities
#for colon/rectum cancer
for i in range(len(cancer_data['Colon and Rectum'])):
    if (cancer_data['Colon and Rectum'][i] > highest_fatalities2):
        highest_fatalities2 = cancer_data['Colon and Rectum'][i]
        max_year2 = cancer_data['Year'][i]
    if (cancer_data['Colon and Rectum'][i] < lowest_fatalities2):
        lowest_fatalities2 = cancer_data['Colon and Rectum'][i]
        min_year2 = cancer_data['Year'][i]
    sum_fatalities2 += cancer_data['Colon and Rectum'][i]

avg_fatalities2 = sum_fatalities2/len(cancer_data['Colon and Rectum'])

#write statistics for colon/rectum cancer
colon_most = "Most fatalities per year:", highest_fatalities2, "occured in", max_year2
statistic_writer.pencolor("blue")
stat_change_position()
statistic_writer.write(colon_most, font=("Arial", 9, "bold"))
stat_change_position()
colon_least = "Least fatalities per year:", lowest_fatalities2, "occured in", min_year2
statistic_writer.write(colon_least, font=("Arial", 9, "bold"))
stat_change_position()
colon_average = "The average fatalities per year was:", avg_fatalities2
statistic_writer.write(colon_average, font=("Arial", 9, "bold"))

#LEUKEMIA MIN MAX AVR variables defined
lowest_fatalities3 = cancer_data['Leukemia'][0]
highest_fatalities3 = cancer_data['Leukemia'][0]
min_year3 = cancer_data['Year'][0]
max_year3 = cancer_data['Year'][0]
sum_fatalities3 = 0
avg_fatalities3 = 0

#calculate minimum, maximum and average fatalities
#for Leukemia
for i in range(len(cancer_data['Leukemia'])):
    if (cancer_data['Leukemia'][i] > highest_fatalities3):
        highest_fatalities3 = cancer_data['Leukemia'][i]
        max_year3 = cancer_data['Year'][i]
    if (cancer_data['Leukemia'][i] < lowest_fatalities3):
        lowest_fatalities3 = cancer_data['Leukemia'][i]
        min_year3 = cancer_data['Year'][i]
    sum_fatalities3 += cancer_data['Leukemia'][i]

avg_fatalities3 = sum_fatalities3/len(cancer_data['Leukemia'])

#write statistics for colon/rectum cancer
leukemia_most = "Most fatalities per year:", highest_fatalities3, "occured in", max_year3
statistic_writer.pencolor("red")
stat_change_position()
statistic_writer.write(leukemia_most, font=("Arial", 9, "bold"))
stat_change_position()
leukemia_least = "Least fatalities per year:", lowest_fatalities3, "occured in", min_year3
statistic_writer.write(leukemia_least, font=("Arial", 9, "bold"))
stat_change_position()
leukemia_average = "The average fatalities per year was:", avg_fatalities3
statistic_writer.write(leukemia_average, font=("Arial", 9, "bold"))

#BREAST CANCER MIN MAX AVR variables defined
lowest_fatalities4 = cancer_data['Breast'][0]
highest_fatalities4 = cancer_data['Breast'][0]
min_year4 = cancer_data['Year'][0]
max_year4 = cancer_data['Year'][0]
sum_fatalities4 = 0
avg_fatalities4 = 0

#calculate minimum, maximum and average fatalities
#for Leukemia
for i in range(len(cancer_data['Breast'])):
    if (cancer_data['Breast'][i] > highest_fatalities4):
        highest_fatalities4 = cancer_data['Breast'][i]
        max_year4 = cancer_data['Year'][i]
    if (cancer_data['Breast'][i] < lowest_fatalities4):
        lowest_fatalities4 = cancer_data['Breast'][i]
        min_year4 = cancer_data['Year'][i]
    sum_fatalities4 += cancer_data['Breast'][i]

avg_fatalities4 = sum_fatalities4/len(cancer_data['Breast'])

#write statistics for colon/rectum cancer
breast_most = "Most fatalities per year:", highest_fatalities4, "occured in", max_year4
statistic_writer.pencolor("pink")
stat_change_position()
statistic_writer.write(breast_most, font=("Arial", 9, "bold"))
stat_change_position()
breast_least = "Least fatalities per year:", lowest_fatalities4, "occured in", min_year4
statistic_writer.write(breast_least, font=("Arial", 9, "bold"))
stat_change_position()
breast_average = "The average fatalities per year was:", avg_fatalities4
statistic_writer.write(breast_average, font=("Arial", 9, "bold"))

#PROSTATE CANCER MIN MAX AVR variables defined
lowest_fatalities5 = cancer_data['Prostate'][0]
highest_fatalities5 = cancer_data['Prostate'][0]
min_year5 = cancer_data['Year'][0]
max_year5 = cancer_data['Year'][0]
sum_fatalities5 = 0
avg_fatalities5 = 0

#calculate minimum, maximum and average fatalities
#for prostate cancer
for i in range(len(cancer_data['Prostate'])):
    if (cancer_data['Prostate'][i] > highest_fatalities5):
        highest_fatalities5 = cancer_data['Prostate'][i]
        max_year5 = cancer_data['Year'][i]
    if (cancer_data['Prostate'][i] < lowest_fatalities5):
        lowest_fatalities5 = cancer_data['Prostate'][i]
        min_year5 = cancer_data['Year'][i]
    sum_fatalities5 += cancer_data['Prostate'][i]

avg_fatalities5 = sum_fatalities5/len(cancer_data['Prostate'])

#write statistics for prostate cancer
prostate_most = "Most fatalities per year:", highest_fatalities5, "occured in", max_year5
statistic_writer.pencolor("green")
stat_change_position()
statistic_writer.write(prostate_most, font=("Arial", 9, "bold"))
stat_change_position()
prostate_least = "Least fatalities per year:", lowest_fatalities5, "occured in", min_year5
statistic_writer.write(prostate_least, font=("Arial", 9, "bold"))
stat_change_position()
prostate_average = "The average fatalities per year was:", avg_fatalities5
statistic_writer.write(prostate_average, font=("Arial", 9, "bold"))

#move to new line before adding more 
#statistics
statistic_writer.goto(10, -60)
statistic_writer.write("hi", font=("Arial", 9, "bold"))

#plot all cancer deaths on graph
plt.plot(cancer_data['Year'], cancer_data['Liver'], color='gray')
plt.plot(cancer_data['Year'], cancer_data['Colon and Rectum'], color='blue')
plt.plot(cancer_data['Year'], cancer_data['Leukemia'], color='red')
plt.plot(cancer_data['Year'], cancer_data['Prostate'], color='green')
plt.plot(cancer_data['Year'], cancer_data['Bladder'], color='cyan')
plt.plot(cancer_data['Year'], cancer_data['Pancreatic'], color='yellow')
plt.plot(cancer_data['Year'], cancer_data['Breast'], color='pink')
plt.plot(cancer_data['Year'], cancer_data['Non-Hodgkin'], color='black')
plt.show()
