import tkinter as tk
from tkinter import ttk
import math

class MiamiViceCalculator:
    def __init__(self, master):
        self.master = master
        master.title("Miami Vice Calculator")
        master.geometry("400x600")
        master.configure(bg='#FF1493')  # Deep pink background

        self.display_var = tk.StringVar()
        self.display_var.set('0')
        self.history = []

        self.create_widgets()

    def create_widgets(self):
        style = ttk.Style()
        style.theme_use('default')
        style.configure('TButton', background='#00CED1', foreground='white', font=('Arial', 14, 'bold'), borderwidth=0)
        style.map('TButton', background=[('active', '#008B8B')])

        # Display
        display = ttk.Entry(self.master, textvariable=self.display_var, font=('Arial', 24), justify='right')
        display.grid(row=0, column=0, columnspan=4, padx=5, pady=5, sticky='nsew')

        # Buttons
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        row_val = 1
        col_val = 0

        for button in buttons:
            ttk.Button(self.master, text=button, command=lambda x=button: self.on_button_click(x)).grid(row=row_val, column=col_val, padx=5, pady=5, sticky='nsew')
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        ttk.Button(self.master, text='C', command=self.clear).grid(row=row_val, column=col_val, padx=5, pady=5, sticky='nsew')
        ttk.Button(self.master, text='History', command=self.show_history).grid(row=row_val+1, column=0, columnspan=4, padx=5, pady=5, sticky='nsew')

        # Configure grid
        for i in range(5):
            self.master.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.master.grid_columnconfigure(i, weight=1)

        # History display
        self.history_display = tk.Text(self.master, height=10, width=40, bg='#1E90FF', fg='white', font=('Arial', 12))
        self.history_display.grid(row=row_val+2, column=0, columnspan=4, padx=5, pady=5, sticky='nsew')
        self.history_display.insert(tk.END, "Calculation History:\n")
        self.history_display.config(state='disabled')

    def on_button_click(self, key):
        if key == '=':
            try:
                result = eval(self.display_var.get())
                self.history.append(f"{self.display_var.get()} = {result}")
                self.display_var.set(result)
                self.update_history()
            except:
                self.display_var.set("Error")
        else:
            if self.display_var.get() == '0':
                self.display_var.set(key)
            else:
                self.display_var.set(self.display_var.get() + key)

    def clear(self):
        self.display_var.set('0')

    def show_history(self):
        history_window = tk.Toplevel(self.master)
        history_window.title("Calculation History")
        history_window.geometry("300x400")
        history_window.configure(bg='#1E90FF')

        history_text = tk.Text(history_window, height=20, width=40, bg='#1E90FF', fg='white', font=('Arial', 12))
        history_text.pack(padx=10, pady=10)

        for item in self.history:
            history_text.insert(tk.END, item + '\n')

        history_text.config(state='disabled')

    def update_history(self):
        self.history_display.config(state='normal')
        self.history_display.delete(1.0, tk.END)
        self.history_display.insert(tk.END, "Calculation History:\n")
        for item in self.history[-5:]:  # Show last 5 calculations
            self.history_display.insert(tk.END, item + '\n')
        self.history_display.config(state='disabled')

if __name__ == "__main__":
    root = tk.Tk()
    calculator = MiamiViceCalculator(root)
    root.mainloop()