import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

kivy.require('2.2.1')

# class MyApp(App):
#     def build(self):
#         return Label(text="Hello, Kivy!")


class childApp(GridLayout):
    def __init__(self, **kwargs):
        super(childApp, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text='Name'))
        self.stu_name = TextInput()
        self.add_widget(self.stu_name)

        self.add_widget(Label(text='Age'))
        self.stu_age = TextInput()
        self.add_widget(self.stu_age)

        self.add_widget(Label(text='Gender'))
        self.stu_gender = TextInput()
        self.add_widget(self.stu_gender)


class parentApp(App):
    def build(self):
        return childApp()

if __name__ == '__main__':
    # MyApp().run()
    parentApp().run()
