import json
from tkinter import *
import tkinter.messagebox as msg
from configparser import ConfigParser
import requests

url='http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'
config_file='config.ini'
config=ConfigParser()
config.read(config_file)
api_key=config['api_key']['key']
def get_weather(city):
    result = requests.get(url.format(city,api_key))
    if result:
        json=result.json()
        city= json['name']
        country=json['sys']
        temp_kelvin=json['main']['temp']
        temp_celsius=temp_kelvin -273.15
        temp_fahrenhite=(temp_kelvin -273.15)*1.8+32
        weather=json['weather'][0]['main']
        final=[city,country,temp_celsius,temp_fahrenhite,weather]
        return final
    else:
        return None

def search():
    city = city_name.get()
    weather = get_weather(city)
    if weather:
        location_lbl['text'] = '{} ,{}'.format(weather[0], weather[1])
        temperature_label['text']='{:.2f}c,{:.2f}F'.format(weather[2],weather[3])
        weather_l['text'] = weather[4]
    else:
        msg.showerror('Error', "Cannot find {}".format(city))


root=Tk()
root.title("Weather App")
root.geometry("400x200")

city_name=StringVar()
city_entry =Entry(root,textvariable=city_name).pack(padx=20,pady=20)
Search_btn = Button(root, text="Search Weather",
                    width=12, command=search)
Search_btn.pack()


location_lbl = Label(root, text="Location", font={'bold', 20})
location_lbl.pack()
temperature_label = Label(root, text="")
temperature_label.pack()
weather_l = Label(root, text="")
weather_l.pack()
root.mainloop()
