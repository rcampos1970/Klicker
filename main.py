# import kivy module
import kivy
c = 0
# this restrict the kivy version i.e
# below this kivy version you cannot
# use the app or software

# base Class of your App inherits from the App class.
# app:always refers to the instance of your application
from kivy.app import App

# creates the button in kivy
# if not imported shows the error
from kivy.uix.button import Button


# class in which we are creating the button
class ButtonApp(App):

    def build(self):
        btn = Button(text=f"{c}")
        return btn



# creating the object root for ButtonApp() class
root = ButtonApp()
c = c+1

# run function runs the whole program
# i.e run() method which calls the
# target function passed to the constructor.
root.run()

