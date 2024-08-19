from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import *
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout

Window.clearcolor = 200,200,200
Builder.load_file("third.kv")

class Third(Screen):
    def __init__(self, **kwargs):
        super(). __init__(**kwargs)

    def validate_user(self):    
        user = self.ids.Username_field
        pwd = self.ids.pwd_field
        inf= self.ids.info

        uname = user.text
        passwd = pwd.text

        if uname == "" or passwd == "":
            inf.text = "[color = #FF0000]username and/ password required[/color]"
        else:
            if uname == "Admin" and passwd == "Admin":
                inf.text = "[color = #00FF00]signed in successfully!!!!![/color]"
            


class MyApp(App):
    def build(self):
        return Third()
MyApp().run()    
