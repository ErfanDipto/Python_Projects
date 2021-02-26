import tkinter as tk


# window
window = tk.Tk()
# window.minsize(height=50, width=300)
window.title("Mile to KM converter")
window.config(padx=20, pady=20)

# entry
entry = tk.Entry(width=7)
entry.grid(row=0, column=1)
# try:
#     miles = float(entry.get())
# except ValueError:
#     miles = 0
#
# # miles calculation
# km = round(miles/0.62137, 2)


# function for button
def convert_to_km():
    miles = float(entry.get())
    km = round(miles / 0.62137, 2)
    label_km.config(text=f"{km:2}")


# label
label_miles = tk.Label(text="Miles")
label_miles.grid(row=0, column=2)

label_equal = tk.Label(text="is equal to ")
label_equal.grid(row=1, column=0)

label_km = tk.Label(text="0.0")
label_km.grid(row=1, column=1)

label_km_2 = tk.Label(text="KM")
label_km_2.grid(row=1, column=2)

# button
convert = tk.Button(text="Convert", command=convert_to_km)
convert.grid(row=2, column=1)

window.mainloop()
