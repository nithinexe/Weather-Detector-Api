
#creating a weather rest api to get the city weather report

#Using GUI to get the necessary data with a window

#we will be importing the necessary modules now

import json #importing json
import tkinter as tk #importing tkinter as tk (to be simple)
import requests
from tkinter import *
from tkinter import messagebox

#now we will be creating the necessary widgets with function create widgets

def CreateWidgets():
    cityLabel = Label(root, text = "ENTER THE CITY NAME : " , bg = "darkslategray4") #city label
    cityLabel.grid(row = 0 , column = 0 , padx = 10 , pady = 5)
    CityEntry = Entry(root ,  width = 36 , textvariable = cityName) #entering the city name
    CityEntry.grid(row = 0 , column = 1 , padx = 10 , pady = 5)

    findButton = Button(root , text = "FIND WEATHER " , command  = findWeather)#findingbutton
    findButton.grid(row = 1 , column = 0 , padx =5 , pady = 5 , columnspan =2)

    clearButton = Button(root , text = "CLEAR" , command = clearEntries) #clearingbutton
    clearButton.grid(row = 1 , column = 1 , padx = 5 , pady = 5 , columnspan = 2 )

    cityCoord = Label(root , text = "City Coordinates :" , bg ="darkslategray4")
    cityCoord.grid(row = 2 , column = 0 , padx = 10 , pady = 5)
    root.cityCoord = Entry(root , width=36)
    root.cityCoord.grid(row = 2 , column = 1 , padx = 10 , pady = 5)

    tempLabel = Label(root , text = "TEMPERATURE : " , bg = "darkslategray4")
    tempLabel.grid(row = 3 , column = 0 , padx = 10 , pady = 5)
    root.tempEntry = Entry(root ,  width = 36)
    root.tempEntry.grid(row = 3 , column = 1 , padx = 10 , pady = 5)

    humidityLabel = Label(root, text="HUMIDITY : " , bg ="darkslategray4")
    humidityLabel.grid(row = 4 , column = 0 , padx = 10 , pady = 5)
    root.humidityEntry = Entry(root , width = 36)
    root.humidityEntry.grid(row = 4 , column = 1 , padx = 10 , pady = 5)


    windLabel = Label(root , text="WIND : " , bg = "darkslategray4")
    windLabel.grid(row = 5 , column = 0 , padx = 10 , pady = 5)
    root.windEntry = Entry(root , width = 36)
    root.windEntry.grid(row = 5 , column = 1 , padx = 10 , pady = 5)

    pressureLabel = Label(root , text="ATMOSPHERIC PRESSURE : " , bg = "darkslategray4")
    pressureLabel.grid(row = 6 , column = 0 , padx = 10 , pady = 5)
    root.pressureEntry = Entry(root , width = 36)
    root.pressureEntry.grid(row = 6 , column = 1 , padx = 10 , pady = 5)

    descLabel = Label(root , text = "WEATHER DESCRIPTION : " , bg = "darkslategray4")
    descLabel.grid(row = 7 , column = 0 , padx = 10 , pady = 5)
    root.descEntry = Entry(root , width = 36)
    root.descEntry.grid(row = 7 , column = 1 , padx = 10 , pady = 5)



#defining findWeather() function to find weather of user input city

def findWeather():
    #storing the API KEY
    APIKey = "Your API Key"
    #storing the weather URL(base URL) to which request has to be sent
    weatherURL = "http://api.openweathermap.org/data/2.5/weather?"
    #fetchiing the user-input city name
    cityname = cityName.get()
    #concatenating APIKey and user input city name with weatherURL(base URL)
    #storing the complete url in requestURl
    #setting units = metric means TEMPERATURE will be shown in CELCIUS
    requestURl = weatherURL+"appid="+APIKey+"&q="+cityname+"&units=metric"
    #sending request to url and fetching and storing the response
    response = requests.get(requestURl)
    #converting response which is in json format data into python format
    weatherResponse = response.json()
    #printing the weatherResponse dictionary
    print(json.dumps(weatherResponse, indent=2))
    #print some values from the above weatherResponse dictionary will be fetched &displayed in tkinter window

    #checkinng if the value of is not equal to 404
    if weatherResponse["cod"] != "404":
        #fetching and storing the value of "main " key from weatherResponse
        weatherPARA = weatherResponse["main"]
        #fetching and storing the value of 'coord' key from weatherResponse
        coordinates = weatherResponse['coord']
        #storing the lattitude and longitude key value from weatherResponse
        lalitude = str(coordinates['lat'])
        longitude = str(coordinates['lon'])
        #fetching and storing wind key weatherResponse
        wind = weatherResponse['wind']
        #storing the speed key value from wind
        windSpeed = str(wind['speed'])
        #checkif 'deg' key is present in wind key weatherResponse dictionary
        if 'deg' in wind.keys():
            windDirect = str(wind['deg'])
        #If not present then set windDirect empty string
        else:
            windDirect = ''

        #fetching and storing the TEMPERATURE value from weatherPARA
        temperature = str(weatherPARA["temp"])
        ##fetching and storing the PRESSURE value from weatherPARA
        pressure = str(weatherPARA["pressure"])
        #fetching and storing the HUMIDITY value from weatherPARA
        humidity = str(weatherPARA["humidity"])
        #fetching and storing the weather value which is a list from weatherResponse
        weatherDesc = weatherResponse['weather']
        #storing the descriptionition value from 0 index item of weatherDesc list
        weatherDescription = weatherDesc[0]["description"]

        #clearing previous weather entries if there's any
        root.cityCoord.delete(0,END)
        root.tempEntry.delete(0,END)
        root.humidityEntry.delete(0,END)
        root.windEntry.delete(0,END)
        root.pressureEntry.delete(0,END)
        root.descEntry.delete(0,END)
        #showing the new results in tkinter window
        root.cityCoord.insert('0' , 'LATITUDE : '+lalitude+ "LONGITUDE : "+longitude)
        root.tempEntry.insert('0',temperature+" C")
        root.humidityEntry.insert('0' , str(humidity) +" %")
        root.windEntry.insert('0' , "SPEED: " +windSpeed+ "meter/sec" + "DIRECTION : "+windDirect+" ")
        root.pressureEntry.insert('0' , pressure+"hPa")
        root.descEntry.insert('0' , weatherDescription)
    #if cod key value is 404 then city is not found
    else:
        messagebox.showerror("ERROR" , "CITY NOT FOUND!")
#Defining clearEntries() to clear the valus from the text entries of tkinter window
def clearEntries():
    cityName.set('')
    root.cityCoord.delete(0,END)
    root.tempEntry.delete(0,END)
    root.humidityEntry.delete(0,END)
    root.windEntry.delete(0,END)
    root.pressureEntry.delete(0,END)
    root.descEntry.delete(0,END)


#creating object clas of tk class
root = tk.Tk()
#setting the title , bg color , window size & disabling the resizing property
root.title("PyWeatherDetector")
root.config(background="darkslategray4")
root.geometry("570x320")
root.resizable(False , False)
#creating tkinter variable
cityName = StringVar()
#calling the CreateWidgets() function
CreateWidgets()
#defining infinite loop to run application


root.mainloop()
