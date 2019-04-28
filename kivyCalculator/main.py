from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

Window.size = (300, 400)

class CalculatorApp(App):
    def build(self):
        return CalculatorLayout()

class CalculatorLayout(BoxLayout):
    def calculate(self, equation):
        answer = eval(equation)
        self.display.text = str(answer)

if __name__ == "__main__":
    my_equation = "2+3"
    print(eval(my_equation))
    app = CalculatorApp()
    app.run()