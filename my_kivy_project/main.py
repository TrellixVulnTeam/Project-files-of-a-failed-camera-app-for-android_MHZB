import kivy
import random

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class MainApp(App):
    def build(self):
        layout = BoxLayout(padding=10, orientation="vertical")
        layout.add_widget(Image(source='./picture.png', pos_hint={'center_x':0.5, 'center_y':0.5}))
        layout.add_widget(Label(text='Hello from Kivy', pos_hint={'center_x': 0.5, 'center_y': 0.5}))
        return layout

if __name__ == '__main__':
    app = MainApp()
    app.run()
