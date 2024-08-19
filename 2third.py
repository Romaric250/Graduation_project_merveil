from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import *
from kivy.core.window import Window

Window.clearcolor = 200,200,200
Builder.load_file("sign.kv")

class Sign(Screen):
    pass

class MyApp(App):
    def build(self):
        return Sign()
    
MyApp().run()



