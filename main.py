import tkinter as tk

root = tk.Tk()

# Entry ---------------------------------------------------------------
entry_var = tk.StringVar()

entry = tk.Entry(
    root,
    bg="white",
    textvariable=entry_var
)
entry.pack()

# Radiobutton  --------------------------------------------------------
radiobutton_var = tk.StringVar()

radiobutton_frame = tk.LabelFrame(
    root,
    text="Radiobutton",
    bd=1,
    relief="solid",
)
radiobutton_frame.pack()

radiobutton0 = tk.Radiobutton(
    radiobutton_frame,
    variable=radiobutton_var,
    value="Day",
    text="Day",
)
radiobutton0.pack()

radiobutton1 = tk.Radiobutton(
    radiobutton_frame,
    variable=radiobutton_var,
    value="Month",
    text="Month",
)
radiobutton1.pack()

radiobutton2 = tk.Radiobutton(
    radiobutton_frame,
    variable=radiobutton_var,
    value="Year",
    text="Year",
)
radiobutton2.pack()

# Checkbutton  --------------------------------------------------------
checkbutton_var0 = tk.BooleanVar()
checkbutton_var1 = tk.BooleanVar()
checkbutton_var2 = tk.BooleanVar()

checkbutton_frame = tk.LabelFrame(
    root,
    text="Checkbutton",
    bd=1,
    relief="solid",
)
checkbutton_frame.pack()

checkbutton0 = tk.Checkbutton(
    checkbutton_frame,
    variable=checkbutton_var0,
    onvalue=True,
    offvalue=False,
    text="Day",
)
checkbutton0.pack()

checkbutton1 = tk.Checkbutton(
    checkbutton_frame,
    variable=checkbutton_var1,
    onvalue=True,
    offvalue=False,
    text="Month",
)
checkbutton1.pack()

checkbutton2 = tk.Checkbutton(
    checkbutton_frame,
    variable=checkbutton_var2,
    onvalue=True,
    offvalue=False,
    text="Year",
)
checkbutton2.pack()

# Spinbox -------------------------------------------------------------
spinbox_var = tk.StringVar()

spinbox = tk.Spinbox(
    root,
    textvariable=spinbox_var,
    values=("Day", "Month", "Year"),
    state="readonly",
)
spinbox.pack()

# OptionMenu ----------------------------------------------------------
optionmenu_var = tk.StringVar()

optionmenu = tk.OptionMenu(
    root,
    optionmenu_var,
    "Day", "Month", "Year",
)
optionmenu.pack()

# Label -------------------------------------------------------------
label = tk.Label(root, bg="white")
label.pack()

def get_values():
    day_cntr, month_cntr, year_cntr = 0, 0, 0
    
    day_cntr += 1 if entry_var.get() == "Day" else 0
    month_cntr += 1 if entry_var.get() == "Month" else 0
    year_cntr += 1 if entry_var.get() == "Year" else 0
    
    day_cntr += 1 if radiobutton_var.get() == "Day" else 0
    month_cntr += 1 if radiobutton_var.get() == "Month" else 0
    year_cntr += 1 if radiobutton_var.get() == "Year" else 0
    
    day_cntr += 1 if checkbutton_var0.get() else 0
    month_cntr += 1 if checkbutton_var1.get() else 0
    year_cntr += 1 if checkbutton_var2.get() else 0
    
    day_cntr += 1 if spinbox_var.get() == "Day" else 0
    month_cntr += 1 if spinbox_var.get() == "Month" else 0
    year_cntr += 1 if spinbox_var.get() == "Year" else 0
    
    day_cntr += 1 if optionmenu_var.get() == "Day" else 0
    month_cntr += 1 if optionmenu_var.get() == "Month" else 0
    year_cntr += 1 if optionmenu_var.get() == "Year" else 0
    
    label.config(text=f"Day={day_cntr}, Month={month_cntr}, Year={year_cntr}")
    

button = tk.Button(
    root,
    text="Get Values",
    command=get_values,
)
button.pack()

root.mainloop()
