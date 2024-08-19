from kivy.uix.widget import Widget
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.screenmanager import *

Builder.load_file("second.kv")

class Second(Screen):
    pass

class MyApp(App):
    def build(self):
        return Second()
    
MyApp().run()    