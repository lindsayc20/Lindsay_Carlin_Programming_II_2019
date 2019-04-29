# kivy universal gravity calculator (30pts)

# When we learned about exceptions, I asked you to make a Universal Gravity calculator

# G is the universal gravity constant (6.674×10−11 N m^2 / kg^2)
# m1 is the mass of object 1 in kg
# m2 is the mass of object 2 in kg
# r is the distance between the two objects in meters (center to center distance)
# F is force in Newtons 
# F = G * (m1 * m2) / r ** 2

# Make a universal gravity calculator app using kivy
# Your app will have the following:
# -a label widget that shows the title of your app (2pts)
# -a label widget and TextInput to input two masses and the radius (6pts)
# -textInput widgets should not accept non-numerical input. (2pts)  
# -a calculate button to execute the gravity calculation (3pts)
# -answer label to show the calculation after you click on the button (3pts)
# -when calculate button pressed, the answer appears in the answer label (5pts)
# -value errors, and divide by zero errors do not occur (4pts)
# -answer is formatted in scientific notation to two decimals (2pts)
# -layout is formatted in a meaningful way to make application user friendly and attractive (3pts)   

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

Window.size = (300, 400)

class GravityApp(App):
    def build(self):
        return GravityLayout()

class GravityLayout(BoxLayout):
    def calculate(self):
        g_constant = 6.67e-11
        try:
            m1 = float(self.m1.text)
            m2 = float(self.m2.text)
            radius = float(self.radius.text)
            if m1 == "" or m2 == "" or radius == "":
                return
            gravity = g_constant * (m1 * m2) / radius ** 2
            self.gravity.text = "Gravitational force\nbetween the objects:\n" + str("{:.2e}".format(gravity)) + str(" Newtons")
        except ZeroDivisionError:
            self.gravity.text = "Unable to divide by 0"
        except ValueError:
            self.gravity.text = "Input not recognizable"

if __name__ == "__main__":
    app = GravityApp()
    app.run()