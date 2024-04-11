import tkinter as tk
from tkinter import messagebox

class ToDoListApp:
    def __init__(self, window):
        self.window = window
        self.window.title("Unique Python To-Do List")
        
        self.task_list = []
        self.load_tasks()
        
        self.listbox = tk.Listbox(window, height=15, width=50)
        self.listbox.pack()
        
        self.entry = tk.Entry(window, width=50)
        self.entry.pack()
        
        self.add_button = tk.Button(window, text="Add Task", command=self.add_task)
        self.add_button.pack()
        
        self.mark_button = tk.Button(window, text="Mark as Completed", command=self.mark_task_as_completed)
        self.mark_button.pack()
        
        self.delete_button = tk.Button(window, text="Delete Task", command=self.delete_task)
        self.delete_button.pack()
        
        self.update_listbox()
    
    def load_tasks(self):
        try:
            with open("tasks.txt", "r") as file:
                self.task_list = file.readlines()
        except FileNotFoundError:
            self.task_list = []
    
    def save_tasks(self):
        with open("tasks.txt", "w") as file:
            for task in self.task_list:
                file.write(task + "\n")
    
    def add_task(self):
        task = self.entry.get()
        if task:
            self.task_list.append(task)
            self.entry.delete(0, tk.END)
            self.update_listbox()
            self.save_tasks()
        else:
            messagebox.showinfo("Info", "Please enter a task.")
    
    def mark_task_as_completed(self):
        selected_task = self.listbox.curselection()
        if selected_task:
            task = self.task_list[selected_task[0]]
            self.task_list[selected_task[0]] = f"✔ {task}"
            self.update_listbox()
            self.save_tasks()
        else:
            messagebox.showinfo("Info", "Please select a task.")
    
    def delete_task(self):
        selected_task = self.listbox.curselection()
        if selected_task:
            del self.task_list[selected_task[0]]
            self.update_listbox()
            self.save_tasks()
        else:
            messagebox.showinfo("Info", "Please select a task.")
    
    def update_listbox(self):
        self.listbox.delete(0, tk.END)
        for task in self.task_list:
            self.listbox.insert(tk.END, task)

if __name__ == "__main__":
    window = tk.Tk()
    app = ToDoListApp(window)
    window.mainloop()
