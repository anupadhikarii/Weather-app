from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from datetime import datetime
from timezonefinder import TimezoneFinder
import requests
import pytz

import requests




def getWeather():
    
    try:
        
        city = textfield.get()
        geolocator = Nominatim(user_agent="geoapiExercise")
        location =  geolocator.geocode(city)
        
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude,lat=location.latitude)
        
        home = pytz.timezone(result)
        local_time = datetime.now(home)
        current_time = local_time.strftime("%I:%M%P")
        clock.config(text=current_time)
        name.config(text="CURRENT WEATHER")
        
        
        #weather 

        url = "https://community-open-weather-map.p.rapidapi.com/climate/month"

        querystring = {"q":city}

        headers = {
            # "X-RapidAPI-Host": "community-open-weather-map.p.rapidapi.com",
            "X-RapidAPI-Key": "6314d9879fmsh8c471d2719d716ap1d1081jsncabcfcd42ab0"
        }   

        response = requests.request("GET", url, headers=headers, params=querystring)
        json_data = response.json()
        # condition = json_data['weather'][0]['main']
        Country = json_data['city']['country']
        temp = (json_data['list'][0]['temp']['average']-273).__floor__()
        pressure = json_data['list'][0]['pressure']
        humidity = json_data['list'][0]['humidity']
        wind = json_data['list'][0]['wind_speed']
        
        t.config(text=(temp,"°"))
        
        if temp <= 0:
            c.config(text=" Feels very Cold ")
        elif temp >= 0 and temp <=15:
            c.config(text=" Feels cold")
        elif temp > 15 and temp < 25:
            c.config(text="  Feels Average Weather")
        else:
            c.config(text=" feels Hot Weather")        
            
                
        w.config(text=wind)
        h.config(text=humidity)
        d.config(text=Country)
        p.config(text=pressure)    
        
    except :
        
        messagebox.showerror("weather app","invalid Entry")    

root = Tk()
root.title = ('Weather Api')
root.geometry("900x500+300+200")
root.resizable(False,False)

#search box
Search_image  = PhotoImage(file="search.png")
myimage = Label(image=Search_image)
myimage.place(x=20,y=20)

textfield = tk.Entry(root,justify="center",width=17,font=("poppins",25,"bold"),bg="#404040",border=0,fg="white")
textfield.place(x=50,y=40)
textfield.focus()

search_icon = PhotoImage(file="search_icon.png")
myimage_icon = Button(image=search_icon , borderwidth=0,cursor="hand2",bg="#404040",command=getWeather)
myimage_icon.place(x=400,y=34)

#logo 
 
logo_image = PhotoImage(file="logo.png")
logo = Label(image=logo_image)
logo.place(x=150,y=100)

#button box
Frame_image = PhotoImage(file="box.png")
Frame_myimage = Label(image=Frame_image)
Frame_myimage.pack(padx=5,pady=5,side=BOTTOM)

#time
name = Label(root,font=("arial",15,"bold"))
name.place(x=30,y=100)
clock = Label(root,font=("helvetica",20))
clock.place(x=30,y=130)


#LABEL 

label1= Label(root,text='WIND', font=("Helvetica",15,'bold'),fg="white",bg='#1ab5ef')
label1.place(x=120,y=405)

label2= Label(root,text='HUMIDITY', font=("Helvetica",15,'bold'),fg="white",bg='#1ab5ef')
label2.place(x=250,y=405)

label3= Label(root,text='COUNTRY SYMBOL', font=("Helvetica",15,'bold'),fg="white",bg='#1ab5ef')
label3.place(x=430,y=405)

label4= Label(root,text='PRESSURE', font=("Helvetica",15,'bold'),fg="white",bg='#1ab5ef')
label4.place(x=650,y=405)

t = Label(font=("arial",70,"bold"), fg="#ea666d")
t.place(x=400,y=150)

c= Label(font=("arial",15,"bold"))
c.place(x=400,y=250)

w=Label(text=".....", font=("arial",20,"bold"),bg = "#1ab5ef")
w.place(x=120,y=430)
h=Label(text=".....", font=("arial",20,"bold"),bg = "#1ab5ef")
h.place(x=280,y=430)

d=Label(text=".....", font=("arial",20,"bold"),bg = "#1ab5ef")
d.place(x=450,y=430)

p=Label(text=".....", font=("arial",20,"bold"),bg = "#1ab5ef")
p.place(x=670,y=430)

root.mainloop()
