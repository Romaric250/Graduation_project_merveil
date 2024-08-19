from kivy.app import App
from kivy.uix.screenmanager import *
from kivy.lang import Builder

Builder.load_file("fith.kv")
class Fith(Screen):
    pass

class MyApp(App):
    def build(self):
        return Fith()
    
MyApp().run()    


