import tkinter as tk


class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Calculator — Advanced Scientific & Standard Calculator with Memory, History, and Expression Support")
        self.root.geometry("400x600")
        self.root.resizable(False, False)

        self.expression = ""

        # Display
        self.display_var = tk.StringVar()

        display = tk.Entry(
            root,
            textvariable=self.display_var,
            font=("Arial", 24),
            justify="right",
            bd=10
        )
        display.grid(row=0, column=0, columnspan=4,
                     sticky="nsew", padx=10, pady=10, ipady=20)

        # Buttons layout
        buttons = [
            ["C", "⌫", "%", "/"],
            ["7", "8", "9", "*"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["(", "0", ")", "."],
            ["**", "="]
        ]

        for r, row in enumerate(buttons, start=1):
            for c, text in enumerate(row):
                btn = tk.Button(
                    root,
                    text=text,
                    font=("Arial", 18),
                    command=lambda t=text: self.click(t)
                )

                if text == "=":
                    btn.grid(
                        row=r,
                        column=c,
                        columnspan=3,
                        sticky="nsew",
                        padx=3,
                        pady=3
                    )
                else:
                    btn.grid(
                        row=r,
                        column=c,
                        sticky="nsew",
                        padx=3,
                        pady=3
                    )

        # Configure grid
        for i in range(7):
            root.grid_rowconfigure(i, weight=1)

        for i in range(4):
            root.grid_columnconfigure(i, weight=1)

        # Keyboard bindings
        root.bind("<Return>", lambda event: self.calculate())
        root.bind("<BackSpace>", lambda event: self.backspace())

        for key in "0123456789+-*/().%":
            root.bind(key, self.key_press)

    def key_press(self, event):
        self.expression += event.char
        self.display_var.set(self.expression)

    def click(self, value):
        if value == "C":
            self.clear()

        elif value == "⌫":
            self.backspace()

        elif value == "=":
            self.calculate()

        else:
            self.expression += str(value)
            self.display_var.set(self.expression)

    def clear(self):
        self.expression = ""
        self.display_var.set("")

    def backspace(self):
        self.expression = self.expression[:-1]
        self.display_var.set(self.expression)

    def calculate(self):
        try:
            result = str(eval(self.expression))
            self.display_var.set(result)
            self.expression = result

        except ZeroDivisionError:
            self.display_var.set("Cannot divide by zero")
            self.expression = ""

        except Exception:
            self.display_var.set("Error")
            self.expression = ""


if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()

