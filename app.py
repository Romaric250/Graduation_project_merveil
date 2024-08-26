from kivy.app import App
from kivy.uix.screenmanager import *

class Log(Screen):
    pass

class First(Screen):
    pass

class Sign(Screen):
    pass

class Third(Screen):
    pass

class Second(Screen):
    pass

class Purchase(Screen):
    pass

class Windowmanager(ScreenManager):
    pass

class MainApp(App):
    def build(self):
        return Windowmanager()

MainApp().run()