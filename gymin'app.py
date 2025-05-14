import tkinter as tk
from tkinter import ttk, messagebox

# Organized workout library by type
workout_library = {}

# Add workout to library
def add_workout():
    name = workout_name_var.get().strip()
    wtype = workout_type_var.get().strip()
    
    if name and wtype:
        if wtype not in workout_library:
            workout_library[wtype] = []
        workout_library[wtype].append(name)
        update_library_display()
        workout_name_var.set("")
        workout_type_var.set("")  # Reset dropdown
    else:
        messagebox.showwarning("Missing Info", "Fill out all info")

# Update listbox
def update_library_display():
    library_listbox.delete(0, tk.END)
    for wtype in sorted(workout_library.keys()):
        library_listbox.insert(tk.END, f"[{wtype}]")
        for workout in workout_library[wtype]:
            library_listbox.insert(tk.END, f"  - {workout}")
        library_listbox.insert(tk.END, "")  # Space between sections

# GUI setup
main = tk.Tk()
main.title("Gymin'")
main.geometry("500x500")

# Workout name input
tk.Label(main, text="Workout Name").pack()
workout_name_var = tk.StringVar()
tk.Entry(main, textvariable=workout_name_var).pack()

# Dropdown for workout type
tk.Label(main, text="Workout Type").pack()
workout_type_var = tk.StringVar()
workout_type_dropdown = ttk.Combobox(main, textvariable=workout_type_var, state="readonly")
workout_type_dropdown['values'] = ["Push", "Pull", "Glutes", "Thighs", "Core", "Full Body"]
workout_type_dropdown.pack()

# Add button
tk.Button(main, text="Add Workout", command=add_workout).pack(pady=10)

# Listbox to show organized workouts
tk.Label(main, text="Workout Inventory (Grouped by Type)").pack()
library_listbox = tk.Listbox(main, width=60, height=20)
library_listbox.pack()

main.mainloop()
