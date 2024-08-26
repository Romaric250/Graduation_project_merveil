from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import * 
from kivy.lang import Builder

Builder.load_file("log.kv")
class Log(Screen):
    pass


class MyApp(App):
    def build(self):
        return Log()
    
MyApp().run()    