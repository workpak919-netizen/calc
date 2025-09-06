# advanced_calculator.py
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window

# Background color
Window.clearcolor = (1, 1, 1, 1)  # white

class Calculator(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"

        # Display bar
        self.display = TextInput(
            multiline=False,
            readonly=True,
            halign="right",
            font_size=42,
            background_color=(0.9, 0.9, 0.9, 1),
            foreground_color=(0, 0, 0, 1)
        )
        self.add_widget(self.display)

        # Button layout (4x5 grid)
        button_layout = GridLayout(cols=4, spacing=5, padding=5)

        buttons = [
            ("C", (1, 0.5, 0.5, 1)),
            ("⌫", (1, 0.7, 0.2, 1)),
            ("(", (0.7, 0.9, 1, 1)),
            (")", (0.7, 0.9, 1, 1)),

            ("7", (0.8, 0.8, 0.8, 1)),
            ("8", (0.8, 0.8, 0.8, 1)),
            ("9", (0.8, 0.8, 0.8, 1)),
            ("/", (0.7, 0.9, 1, 1)),

            ("4", (0.8, 0.8, 0.8, 1)),
            ("5", (0.8, 0.8, 0.8, 1)),
            ("6", (0.8, 0.8, 0.8, 1)),
            ("*", (0.7, 0.9, 1, 1)),

            ("1", (0.8, 0.8, 0.8, 1)),
            ("2", (0.8, 0.8, 0.8, 1)),
            ("3", (0.8, 0.8, 0.8, 1)),
            ("-", (0.7, 0.9, 1, 1)),

            ("0", (0.8, 0.8, 0.8, 1)),
            (".", (0.8, 0.8, 0.8, 1)),
            ("=", (0.6, 1, 0.6, 1)),
            ("+", (0.7, 0.9, 1, 1))
        ]

        # Add buttons dynamically
        for label, color in buttons:
            button = Button(
                text=label,
                font_size=32,
                background_color=color
            )
            button.bind(on_press=self.on_button_press)
            button_layout.add_widget(button)

        self.add_widget(button_layout)

    def on_button_press(self, instance):
        text = instance.text

        if text == "C":
            # Clear screen
            self.display.text = ""
        elif text == "⌫":
            # Backspace
            self.display.text = self.display.text[:-1]
        elif text == "=":
            try:
                # Evaluate safely
                expression = self.display.text
                self.display.text = str(eval(expression))
            except Exception:
                self.display.text = "Error"
        else:
            # Add pressed button to display
            self.display.text += text


class CalculatorApp(App):
    def build(self):
        self.title = "Advanced Calculator"
        return Calculator()


if __name__ == "__main__":
    CalculatorApp().run()
