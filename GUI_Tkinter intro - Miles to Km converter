from tkinter import *

window = Tk()
window.title("Miles to Kilometers")
window.minsize(width=150, height=100)
window.config(padx=50, pady=50)
# Miles label
miles_label = Label(text="Miles", font=("Arial", 15, "bold"))
miles_label.grid(column=3, row=1)
# Km label
km_label = Label(text="Km", font=("Arial", 15, "bold"))
km_label.grid(column=3, row=2)
# is equal to label
equals_label = Label(text="is equal to", font=("Arial", 15, "bold"))
equals_label.grid(column=1, row=2)
# entry box creation
entry_box = Entry(width=10)
entry_box.grid(column=2, row=1)
# Result label
result = Label(text="", font=("Arial", 15, "bold"))
result.grid(column=2,row=2)
# Button to calc.


def calculate_result():
    km_result = round(int(entry_box.get()) * 1.6)
    result.config(text=km_result)


button = Button(text="Calculate", command=calculate_result)
button.grid(column=2, row=3)
window.mainloop()
