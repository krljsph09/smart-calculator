from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window

Window.size = (400, 500)


class CalculatorLayout(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=20, spacing=10, **kwargs)

        # Title
        self.add_widget(Label(text="Smart Arithmetic Calculator",
                              font_size=22,
                              size_hint=(1, 0.15)))

        # First number input
        self.num1 = TextInput(
            hint_text="Enter First Number",
            multiline=False,
            input_filter='float'
        )
        self.add_widget(self.num1)

        # Second number input
        self.num2 = TextInput(
            hint_text="Enter Second Number",
            multiline=False,
            input_filter='float'
        )
        self.add_widget(self.num2)

        # Buttons
        self.add_operation_button("Add (+)", "add")
        self.add_operation_button("Subtract (-)", "subtract")
        self.add_operation_button("Multiply (*)", "multiply")
        self.add_operation_button("Divide (/)", "divide")
        self.add_operation_button("Modulus (%)", "modulus")

        # Result Label
        self.result_label = Label(text="Result: ",
                                  font_size=18,
                                  size_hint=(1, 0.2))
        self.add_widget(self.result_label)

    # Create buttons dynamically
    def add_operation_button(self, text, operation):
        btn = Button(text=text, size_hint=(1, 0.12))
        btn.bind(on_press=lambda instance: self.calculate(operation))
        self.add_widget(btn)

    # Event-driven calculation
    def calculate(self, operation):
        try:
            num1 = float(self.num1.text)
            num2 = float(self.num2.text)

            if operation == "add":
                result = num1 + num2

            elif operation == "subtract":
                result = num1 - num2

            elif operation == "multiply":
                result = num1 * num2

            elif operation == "divide":
                if num2 == 0:
                    self.result_label.text = "Error: Cannot divide by zero"
                    return
                result = num1 / num2

            elif operation == "modulus":
                if num2 == 0:
                    self.result_label.text = "Error: Cannot perform modulus by zero"
                    return
                result = num1 % num2

            else:
                self.result_label.text = "Error: Invalid operation"
                return

            self.result_label.text = f"Result: {result}"

        except ValueError:
            self.result_label.text = "Error: Enter valid numbers"


class SmartCalculatorApp(App):
    def build(self):
        return CalculatorLayout()


if __name__ == "__main__":
    SmartCalculatorApp().run()