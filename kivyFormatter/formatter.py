'''
Formatter (26pts)

Create a kivy app with the following rough layout

############
#  LABEL   #
#  SPINNER #
#  RADIOS  #
#  SLIDERS #
#  SWITCH  #
############

The label will be the formatting target for this application

- The spinner will change the font of the label (minimum 2 fonts) (6pts)
- The radios will be used to select the text for the label (3pts)
- Three sliders will be used to adjust the rgba values of the label background canvas color. (6pts)
- A switch will be used to change the font color from black to white. (3pts)

Each control will have an associated label. (8pts)

'''

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

Window.size = (600, 400)
Window.clearcolor = (1, 1, 1, 1)

class FormatterApp(App):
    def build(self):
        return FormatterLayout()

class FormatterLayout(BoxLayout):
    def font_color(self, value):
        if value:
            self.switch_text.color = (1, 1, 1, 1)
        else:
            self.switch_text.color = (0, 0, 0, 1)
    def color_slide(self, r_value, g_value, b_value):
        Window.clearcolor = (r_value, g_value, b_value, 1)
    def spinner_clicked(self, text):
        self.spin_label.font_name = self.value
    def checked(self, active):
        self.radio_label.text = self.text

if __name__ == "__main__":
    app = FormatterApp()
    app.run()