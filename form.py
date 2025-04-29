


import tkinter as tk
from tkinter import messagebox

# Function to display the summary line
def submit():
    name = name_entry.get()
    age = age_entry.get()
    weather = weather_var.get()
    summary = f"Hello {name}, you are {age} years old and you like {weather}."
    messagebox.showinfo("Summary", summary)

# Create the main window line
root = tk.Tk()
root.title("User Info Form")

# Name input line
tk.Label(root, text="Enter your name:").pack()
name_entry = tk.Entry(root)
name_entry.pack()

# Age input line
tk.Label(root, text="Enter your age:").pack()
age_entry = tk.Entry(root)
age_entry.pack()

# Weather dropdown line
tk.Label(root, text="Select your favorite weather:").pack()
weather_var = tk.StringVar(root)
weather_var.set("Sunny")  # default value
weather_options = ["Sunny", "Rainy", "Snowy"]
weather_menu = tk.OptionMenu(root, weather_var, *weather_options)
weather_menu.pack()

# Submit button line
submit_button = tk.Button(root, text="Submit", command=submit)
submit_button.pack()

# Run the application line
root.mainloop()
