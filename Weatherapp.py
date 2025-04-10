from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz

root = Tk()
root.title("Weather App")
root.geometry("900x600+300+115")
root.resizable(False, False)
root.configure(bg='white')



#icon for the window
icon = Image.open("D:/WeaterApp/icon.png")
icon = icon.resize((40,40))
icon = ImageTk.PhotoImage(icon)
root.iconphoto(False, icon)



    
def getWeather():
    city = textfield.get()

    try:
        geolocator = Nominatim(user_agent='weatherapp_12345_sanjananandania@gmail.com')
        location = geolocator.geocode(city)
        if not location:
            messagebox.showerror("Error", "City not found!")
            return

        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude, lat=location.latitude)

        home = pytz.timezone(result)
        local_time = datetime.now(home)
        current_time = local_time.strftime("%I:%M:%p")
        clock.config(text=current_time)
        name.config(text='CURRENT TIME')

        # Build the API URL 
        api = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid=3c7067c55e418f1023c928a0d0ed99f7'

        response = requests.get(api)
        json_data = response.json()

        # Check if the API returned an error
        if response.status_code != 200 or 'weather' not in json_data:
            error_msg = json_data.get("message", "Unable to fetch weather data")
            messagebox.showerror("Error", f"API Error: {error_msg}")
            return

        # Now it's safe to access weather data
        condition = json_data['weather'][0]['main']
        description = json_data['weather'][0]['description']
        temp = int(json_data['main']['temp'] - 273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']

        # Update the display
        t.config(text=f"{temp}°")
        c.config(text=f"{condition} | FEELS LIKE {temp}°")
        w.config(text=f"{wind} m/s")
        h.config(text=f"{humidity}%")
        d.config(text=description.title())
        p.config(text=f"{pressure} hPa")

    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong:\n{e}")



#EXTRA_IMAGE_DECORATION
original_image2 = Image.open("D:/WeaterApp/decoration.png")
resized_image2 = original_image2.resize((90, 90))  # Change size as needed
decora_image = ImageTk.PhotoImage(resized_image2)
dimage = Label(image=decora_image, bg='white')
dimage.place(x=100, y=15)



#SEARCH BOX
Search_image = PhotoImage(file="D:/WeaterApp/search.png")
myimage = Label(image=Search_image, bg='white')
myimage.place(x=220, y=25)

textfield = tk.Entry(root, justify='center', width=14, font=('Times New Roman',20,'bold'), bg='#A1A1A1', border=0, fg='white')
textfield.place(x=312, y=45)
textfield.focus()


original_image = Image.open("D:/WeaterApp/searchtool.png")
resized_image = original_image.resize((36, 36))  # Change size as needed
Search_tool = ImageTk.PhotoImage(resized_image)

myimage_tool = Button(image=Search_tool, borderwidth=0, cursor='hand2', bg='#A1A1A1', command=getWeather)
myimage_tool.place(x=540,y=46)

#LOGO
Logo_image = PhotoImage(file="D:/WeaterApp/world.png")
logo = Label(image=Logo_image, bg='white')
logo.place(x=70, y=120)

#BOTTOM BOX
original_image1 = Image.open("D:/WeaterApp/box.png")
resized_image1 = original_image1.resize((800, 130))  # Change size as needed
Frame_image = ImageTk.PhotoImage(resized_image1)
frame = Label(image=Frame_image, bg='white')
frame.pack(padx=5, pady=(10,25), side=BOTTOM)

#TIME
name = Label(root, font=('arial',15,'bold'), bg='white')
name.place(x=620, y=40)
clock = Label(root, font=('Helvetica',20), bg='white')
clock.place(x=620, y=70)


#LABEL
label1 = Label(root, text='WIND', font=('Helvetica', 15,'bold'),fg='white', bg='#A5D1F5')
label1.place(x=100, y=460)

label2 = Label(root, text='HUMIDITY', font=('Helvetica', 15,'bold'),fg='white', bg='#A5D1F5')
label2.place(x=250, y=460)

label3 = Label(root, text='DESCRIPTION', font=('Helvetica', 15,'bold'),fg='white', bg='#A5D1F5')
label3.place(x=450, y=460)

label4 = Label(root, text='PRESSURE', font=('Helvetica', 15,'bold'),fg='white', bg='#A5D1F5')
label4.place(x=680, y=460)

t = Label(font=('arial', 70, 'bold'), fg='#ee666d', bg='white')
t.place(x= 400, y= 200)
c = Label(font=('arial', 15,'bold'), fg='#ee666d', bg='white')
c.place(x= 420, y= 300)

w =Label(text='...', font=('arial', 20, 'bold'), bg='#A5D1F5')
w.place(x=90, y=495)
h =Label(text='...', font=('arial', 20, 'bold'), bg='#A5D1F5')
h.place(x=260, y=495)
d =Label(text='...', font=('arial', 20, 'bold'), bg='#A5D1F5')
d.place(x=450, y=495)
p =Label(text='...', font=('arial', 20, 'bold'), bg='#A5D1F5')
p.place(x=695, y=495)




root.mainloop()
 
 
