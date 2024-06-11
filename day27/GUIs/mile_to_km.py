from tkinter import *

def miles_to_km():
    print("Save for later")
    miles = input_entry.get()
    kilometers = int(miles) * 1.6
    output_label.config(text=str(kilometers))

window = Tk()
window.title("Mile to Km Converter")
#window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

input_entry = Entry(width=10)
input_entry.grid(column=1, row=0)

miles_label = Label(text="Miles", font=("Arial", 16))
miles_label.grid(column=2, row=0)

equal_label = Label(text="is equal to", font=("Arial", 16))
equal_label.grid(column=0, row=1)

output_label = Label(text="0", font=("Arial", 16))
output_label.grid(column=1, row=1)

km_label = Label(text="Km", font=("Arial", 16))
km_label.grid(column=2, row=1)

calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)


window.mainloop()