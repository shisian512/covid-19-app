from tkinter import *
import tkinter.font as TkFont
import requests
import time
import datetime

# Get requests from API
covidData = None
try:
    covidData = requests.get("https://corona-rest-api.herokuapp.com/Api/")
except:
    print("Please! Check your internet connection")

# Create Tkinter window
root = Tk()

# Set size to 300x200
root.geometry("350x250")

# Set background color to light cyan
root.configure(background="light cyan")

# Set title to My Covid-19 App
root.title("My Covid-19 App")

# Welcome label
label3 = Label(root, text="", bg='light cyan')
label3.pack()
label = Label(root, text="Welcome to My Covid 19 App!!!",font=("Helvetica", 14, 'bold'),bg='light cyan')
label.pack()
label2 = Label(root, text="", bg='light cyan')
label2.pack()
data = covidData.json()['Success']

# Get the needed data from API, into a variable
country = data[0]['country']
todaycases = data[0]['todayCases']
todaydeaths = data[0]['todayDeaths']
active = data[0]["active"]
critical = data[0]["critical"]
totalcases = data[0]['cases']
recovered = data[0]['recovered']

# Create a listbox to display those values
Lb = Listbox(root, height=7, width=30, font=("Helvetica", 11))
Lb.insert(1, f"  Country               :  {country}")
Lb.insert(2, f"  Today cases       :  {todaycases}")
Lb.insert(3, f"  Today deaths      :  {todaydeaths}")
Lb.insert(4, f"  Active cases       :  {active}")
Lb.insert(5, f"  Critical cases      :  {critical}")
Lb.insert(6, f"  Total cases         :  {totalcases}")
Lb.insert(7, f"  Total recovered   :  {recovered}")
Lb.pack()

# Maintain the window
root.mainloop()