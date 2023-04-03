import googlemaps
import urllib.parse
import tkinter as tk

# зберігаємо API ключ у змінну
API_key = "AIzaSyAo1UBVWS3BbsBwn-XjpkHgUm5uL6mi4sk"

# створюємо об'єкт клієнта Google Maps
gmaps = googlemaps.Client(key=API_key)

def generate_url():
    origin = origin_entry.get()
    destination = destination_entry.get()

    # отримуємо координати для заданих адрес
    origin_coords = gmaps.geocode(origin)[0]['geometry']['location']
    destination_coords = gmaps.geocode(destination)[0]['geometry']['location']

    # отримуємо маршрут між двома адресами
    routes = gmaps.directions(origin=origin, destination=destination, mode="driving")

    # формуємо URL-посилання з адресами, координатами та маршрутом
    url = "https://www.google.com/maps/dir/" + urllib.parse.quote(origin) + "/" + urllib.parse.quote(destination) + "/@" + str(origin_coords['lat']) + "," + str(origin_coords['lng']) + "," + str(destination_coords['lat']) + "," + str(destination_coords['lng']) + "/data=!3m1!4b1!4m2!4m1!3e0"

    new_url.set(url)

# створюємо графічний інтерфейс
root = tk.Tk()

# задаємо заголовок вікна
root.title("Google Maps URL Generator")

# створюємо елементи графічного інтерфейсу
tk.Label(root, text="Origin:").grid(row=0, column=0, padx=5, pady=5)
origin_entry = tk.Entry(root)
origin_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Destination:").grid(row=1, column=0, padx=5, pady=5)
destination_entry = tk.Entry(root)
destination_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Button(root, text="Generate URL", command=generate_url).grid(row=2, column=0, columnspan=2, padx=5, pady=5)

new_url = tk.StringVar()
new_url.set("")
tk.Label(root, textvariable=new_url).grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# запускаємо головний цикл графічного інтерфейсу
root.mainloop()
