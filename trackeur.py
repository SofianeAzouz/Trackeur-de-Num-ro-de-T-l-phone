import tkinter
import tkintermapview
import phonenumbers
import requests

from key import key

from phonenumbers import geocoder
from phonenumbers import carrier

from tkinter import *
from tkinter import messagebox

root = tkinter.Tk()
root.geometry("500x500")

label1 = Label(text="Trackeur de Numero de telephone")
label1.pack()

def getResult():
    num = number.get("1.0", END)
    try:
        num1 = phonenumbers.parse(num)
    except phonenumbers.phonenumberutil.NumberParseException as e:
        result.insert(END, "Numéro de téléphone invalide")
        return
    
    location = geocoder.description_for_number(num1, "en")
    service_provider = carrier.name_for_number(num1, "en")
    
    url = "https://maps.googleapis.com/maps/api/geocode/json?components=phone:{}&key={}".format(num, key)
    
    response = requests.get(url)
    data = response.json()
    
    if data['status'] == 'OK':
        lat = data['results'][0]['geometry']['location']['lat']
        lng = data['results'][0]['geometry']['location']['lng']
        result.insert(END, "Le pays du numéro est :" + location)
        result.insert(END, "\nLa carte SIM du numéro est :" + service_provider)
        result.insert(END, "\La latitude est :" + str(lat))
        result.insert(END, "\La longitude est :" + str(lng))
    else:
        result.insert(END, "Le pays du numéro est :" + location)
        result.insert(END, "\nLa carte SIM du numéro est :" + service_provider)
        result.insert(END, "\nImpossible de récupérer la localisation du numéro de téléphone")


number =Text(height=1)
number.pack()

button = Button(text="Chercher", command=getResult)
button.pack()

result = Text(height=5)
result.pack()


root.mainloop()
