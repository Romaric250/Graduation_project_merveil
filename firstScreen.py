from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import *
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.uix.widget import Widget

Builder.load_file("first.kv")   
class First(Screen):
    pass

class MyApp(App):
    def build(self):
        return First()
    
MyApp().run()       