import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry_task.get()
    if task:
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    try:
        selected_task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

# Create the main window
window = tk.Tk()
window.title("To-Do List")

# Task entry
entry_task = tk.Entry(window, width=40)
entry_task.pack(pady=10)

# Add task button
add_button = tk.Button(window, text="Add Task", command=add_task)
add_button.pack()

# To-Do list
listbox_tasks = tk.Listbox(window, selectmode=tk.SINGLE, width=40, height=10)
listbox_tasks.pack(pady=10)

# Delete task button
delete_button = tk.Button(window, text="Delete Task", command=delete_task)
delete_button.pack()

# Run the main loop
window.mainloop()
