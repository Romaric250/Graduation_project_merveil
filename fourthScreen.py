# from kivy.app import App
# from kivy.lang import Builder
# from kivy.uix.screenmanager import Screen, ScreenManager
# from kivy.core.window import Window

# Window.clearcolor = 0,1,1,1

# class Home(Screen):
#     pass

# class Tutorial(App):
#     def build(self):
#         return Home()



# from kivy.app import App 
# from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.gridlayout import GridLayout
# from kivy.uix.textinput import TextInput
# from kivy.uix.label import Label

# class Purchase(GridLayout):
#     def __init__(self,**kwargs):
#         super(Purchase,self).__init__(**kwargs)
#         self.cols = 2
#         self.add_widget(Label(text = "Enter Your Name:"))
#         self.name = TextInput(multiline = False)
#         self.add_widget(self.name)
#         self.add_widget(Label(text = "Enter Your Contact: "))
#         self.contact = TextInput(multiline = False)
#         self.add_widget(self.contact)
#         self.add_widget(Label(text = "Enter the number of plates: "))
#         self.number = TextInput(multiline = False)
#         self.add_widget(self.number)

# class MyApp(App):
#     def build(self):
#         return Purchase()       


# MyApp().run()     
  
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.screenmanager import *
from kivy.lang import Builder
from kivy.core.window import Window

Window.clearcolor = 139, 128, 0

Builder.load_file("purchase.kv")

class Purchase(Screen):
    # my_text = "You have successfully pass your command"
    # def on_press_Button():
    #     self.my_text
    pass

class MyApp(App):
    def build(self):
        return Purchase()
MyApp().run()    
