import tkinter
import tkintermapview
import phonenumbers

from phonenumbers import geocoder
from phonenumbers import carrier

from tkinter import *
from tkinter import messagebox

root = tkinter.Tk()
root.geometry("1000x1000")

label1 = Label(text="Trackeur de Numero de telephone")
label1.pack()

result = Text(height=5)
result.pack()

def getResult():
    num = number.get("1.0", END)
    try:
        num1 = phonenumbers.parse(num)
    except phonenumbers.phonenumberutil.NumberParseException as e:
        result.insert(END, "Numéro de téléphone invalide")
        return
    
    location = geocoder.description_for_number(num1, "en")
    service_provider = carrier.name_for_number(num1, "en")
    
    result.insert(END, "Le pays du numéro est :" + location)
    result.insert(END, "\nLa carte SIM du numéro est :" + service_provider)

number =Text(height=1)
number.pack()

button = Button(text="Chercher", command=getResult)
button.pack()

root.mainloop()