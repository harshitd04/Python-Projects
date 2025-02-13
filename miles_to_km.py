from tkinter import *
window = Tk()
# window.minsize(200,100)
window.config(padx=10,pady=10)

def print_output_label():
    miles = float(user_input.get())
    km = round(miles * 1.609)
    output_label.config(text=f"{km}")
    output_label.grid(column = 1, row =1)

# for_grid = Label()
# for_grid.grid(column=0, row=0)

is_eq_label = Label(text="is equal to")
is_eq_label.grid(column=0, row=1)

miles_label = Label(text="Miles")
miles_label.grid(column = 2, row =0 )

user_input = Entry(width=10)
user_input.grid(column = 1, row =0)
user_input.focus()

output_label = Label(text="0")
output_label.grid(column = 1, row =1)

calculate_button = Button(text="Calculate", command=print_output_label)
calculate_button.grid(column = 1, row =2)









window.mainloop()