import tkinter as tk
from tkinter import messagebox
import math

class EngineeringCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Инженерный калькулятор")
        self.root.configure(bg='black') 

        self.input_text = tk.StringVar()
        
        self.create_widgets()

    def create_widgets(self):
        entry = tk.Entry(self.root, textvariable=self.input_text, font=('Arial', 16), bd=14, insertwidth=2, width=14, borderwidth=14, bg='black', fg='white')
        entry.grid(row=0, column=0, columnspan=4)

        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            'sin', 'cos', 'tan', 'sqrt',
            'log', 'exp', '(', ')',
            'C', 'Del'  
        ]

        row_val = 1
        col_val = 0
        for button in buttons:
            tk.Button(self.root, text=button, padx=20, pady=20, font=('Arial', 16),
                      command=lambda b=button: self.on_button_click(b), bg='red', fg='white', width=5, height=2).grid(row=row_val, column=col_val, sticky='nsew')
            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1
        
       
        for i in range(5):  
            self.root.grid_rowconfigure(i, weight=1)
        for j in range(4):  
            self.root.grid_columnconfigure(j, weight=1)

    def on_button_click(self, char):
        if char == 'C':
            self.input_text.set('')
        elif char == 'Del':
            current_text = self.input_text.get()
            self.input_text.set(current_text[:-1])
        elif char == '=':
            try:
                expression = self.input_text.get()
                if 'sin' in expression:
                    expression = expression.replace('sin', 'math.sin')
                if 'cos' in expression:
                    expression = expression.replace('cos', 'math.cos')
                if 'tan' in expression:
                    expression = expression.replace('tan', 'math.tan')
                if 'sqrt' in expression:
                    expression = expression.replace('sqrt', 'math.sqrt')
                if 'log' in expression:
                    expression = expression.replace('log', 'math.log')
                if 'exp' in expression:
                    expression = expression.replace('exp', 'math.exp')

                result = eval(expression)
                self.input_text.set(result)
            except Exception as e:
                messagebox.showerror("Ошибка", "Некорректное выражение")
        else:
            current_text = self.input_text.get()
            self.input_text.set(current_text + char)

if __name__ == '__main__':
    root = tk.Tk()
    calculator = EngineeringCalculator(root)
    root.mainloop()
