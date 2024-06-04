from tkinter import *
window = Tk()
window.title("Miles to KM Converter")
window.config(padx = 20, pady = 20)


def convertDistance():
  miles_distance = float(miles_input.get())
  km_distance = round(miles_distance * 1.609)
  kilometer_result_label.config(text = f"{km_distance}")

#Input widget
miles_input = Entry(width = 7)
miles_input.grid(column = 1, row = 0)

#Miles unit label
miles_label = Label(text = "Miles")
miles_label.grid(column = 2, row = 0)

#Equals to label
is_equals_label = Label(text = "is equal to")
is_equals_label.grid(column = 0, row = 1)

#Km result label
kilometer_result_label = Label(text = "0")
kilometer_result_label.grid(column = 1, row = 1)

#Km unit label
km_label = Label(text="Km")
km_label.grid(column = 2, row = 1)


# Calculate button
button = Button(text = "calculate", command = convertDistance)
button.grid(column = 1, row = 2)

window.mainloop()