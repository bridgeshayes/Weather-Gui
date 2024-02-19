import customtkinter
import requests

def get_weather():
    city = inputCity.get()
    state = inputState.get()
    if city and state:
        response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city},{state}&appid=")
        data = response.json()
        print(data)
        if data.get("cod") != "404":
            weather_data = data.get("weather")
            main = weather_data[0].get("main")
            description = weather_data[0].get("description")
            temp = round(9 / 5 * (data["main"]["temp"] - 273.15) + 32)
            tempLabel.configure(text = f"{temp}")
            
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

window = customtkinter.CTk()
window.title("Weather App")
window.geometry("480x600")

label1 = customtkinter.CTkLabel(window, text="CITY")
label1.configure(font= ("Roboto", 14))
label1.place(x=120, y=100)

label2 = customtkinter.CTkLabel(window, text="STATE")
label2.configure(font= ("Roboto", 14))
label2.place(x=120, y=130)

inputCity = customtkinter.CTkEntry(window, placeholder_text="New York")
inputCity.place(x=220, y=100)

inputState = customtkinter.CTkEntry(window, placeholder_text="New York")
inputState.place(x=220, y=130)

button = customtkinter.CTkButton(master=window, text="ENTER", command=get_weather)
button.place(x=240, y=230, anchor=customtkinter.CENTER)

temperature = customtkinter.CTkLabel(window, text="Temperature:")
temperature.configure(font=("Roboto", 20))
temperature.place(x=50, y=400)

tempLabel = customtkinter.CTkLabel(master=window, text="0.0")
tempLabel.configure(font=("Roboto", 20))
tempLabel.place(x=200, y=400)

window.mainloop()