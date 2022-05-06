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
key_letter_drawer.pendown()
key_letter_drawer.write("Key:", font=("Arial", 15, "bold"))
key_letter_drawer.penup()
key_letter_drawer.goto(-150, 300)
key_letter_drawer.write("Liver Cancer -", font=("Arial", 15, "bold"))
key_letter_drawer.penup()
key_letter_drawer.goto(-150, 260)
key_letter_drawer.pendown()
key_letter_drawer.write("Colon and Rectum -", font=("Arial", 15, "bold"))
key_letter_drawer.penup()
key_letter_drawer.goto(-150, 220)
key_letter_drawer.pendown()
key_letter_drawer.write("Leukemia -", font=("Arial", 15, "bold"))
key_letter_drawer.penup()
key_letter_drawer.goto(-150, 180)
key_letter_drawer.pendown()
key_letter_drawer.write("Prostate -", font=("Arial", 15, "bold"))
key_letter_drawer.penup()
key_letter_drawer.goto(-150, 140)
key_letter_drawer.pendown()
key_letter_drawer.write("Bladder -", font=("Arial", 15, "bold"))
key_letter_drawer.penup()
key_letter_drawer.goto(-150, 100)
key_letter_drawer.pendown()
key_letter_drawer.write("Pancreatic -", font=("Arial", 15, "bold"))
key_letter_drawer.penup()
key_letter_drawer.goto(-150, 60)
key_letter_drawer.pendown()
key_letter_drawer.write("Breast -", font=("Arial", 15, "bold"))
key_letter_drawer.penup()
key_letter_drawer.goto(-150, 20)
key_letter_drawer.pendown()
key_letter_drawer.write("Non-Hodgkin -", font=("Arial", 15, "bold"))

#use turtles to add colored shapes for key
key_shape_drawer = t.Turtle()
key_shape_drawer.hideturtle()
key_shape_drawer.speed(0)
key_shape_drawer.penup()
key_shape_drawer.goto(0, 300)
key_shape_drawer.fillcolor("gray")
key_shape_drawer.begin_fill()
key_shape_drawer.circle(15)
key_shape_drawer.end_fill()
key_shape_drawer.goto(60, 260)
key_shape_drawer.fillcolor("blue")
key_shape_drawer.begin_fill()
key_shape_drawer.circle(15)
key_shape_drawer.end_fill()
key_shape_drawer.goto(-30, 220)
key_shape_drawer.fillcolor("red")
key_shape_drawer.begin_fill()
key_shape_drawer.circle(15)
key_shape_drawer.end_fill()
key_shape_drawer.goto(-35, 180)
key_shape_drawer.fillcolor("green")
key_shape_drawer.begin_fill()
key_shape_drawer.circle(15)
key_shape_drawer.end_fill()
key_shape_drawer.goto(-40, 140)
key_shape_drawer.fillcolor("cyan")
key_shape_drawer.begin_fill()
key_shape_drawer.circle(15)
key_shape_drawer.end_fill()
key_shape_drawer.goto(-20, 100)
key_shape_drawer.fillcolor("yellow")
key_shape_drawer.begin_fill()
key_shape_drawer.circle(15)
key_shape_drawer.end_fill()
key_shape_drawer.goto(-60, 60)
key_shape_drawer.fillcolor("pink")
key_shape_drawer.begin_fill()
key_shape_drawer.circle(15)
key_shape_drawer.end_fill()
key_shape_drawer.goto(0, 20)
key_shape_drawer.fillcolor("black")
key_shape_drawer.begin_fill()
key_shape_drawer.circle(15)
key_shape_drawer.end_fill()

statistic_writer = t.Turtle()
statistic_writer.hideturtle()
statistic_writer.speed(0)
statistic_writer.penup()
statistic_writer.goto(-15, -40)
statistic_writer.write("Statistics:", font=("Arial", 15, "bold"))

#LIVER MIN MAX AVR
min_anomaly = cancer_data['Liver'][0]
max_anomaly = cancer_data['Liver'][0]
min_year = cancer_data['Year'][0]
max_year = cancer_data['Year'][0]
sum_anomaly = 0
avg_anomaly = 0

for i in range(len(cancer_data['Liver'])):
    if (cancer_data['Liver'][i] > max_anomaly):
        max_anomaly = cancer_data['Liver'][i]
        max_year = cancer_data['Year'][i]
    if (cancer_data['Liver'][i] < min_anomaly):
        min_anomaly = cancer_data['Liver'][i]
        min_year = cancer_data['Year'][i]
    sum_anomaly += cancer_data['Liver'][i]

avg_anomaly = sum_anomaly/len(cancer_data['Liver'])

L = "The most fatalities per year were:", max_anomaly, "which occured in", max_year
statistic_writer.goto(-15, -100)
statistic_writer.write(L, font=("Arial", 10, "bold"))
print("The least fatalities per year were:", min_anomaly, "which occured in", min_year)
print("The average fatalities per year was:", avg_anomaly)

#plot kidney cancer deaths
plt.plot(cancer_data['Year'], cancer_data['Liver'], color='gray')
plt.plot(cancer_data['Year'], cancer_data['Colon and Rectum'], color='blue')
plt.plot(cancer_data['Year'], cancer_data['Leukemia'], color='red')
plt.plot(cancer_data['Year'], cancer_data['Prostate'], color='green')
plt.plot(cancer_data['Year'], cancer_data['Bladder'], color='cyan')
plt.plot(cancer_data['Year'], cancer_data['Pancreatic'], color='yellow')
plt.plot(cancer_data['Year'], cancer_data['Breast'], color='pink')
plt.plot(cancer_data['Year'], cancer_data['Non-Hodgkin'], color='black')
plt.show()
