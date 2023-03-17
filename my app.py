from kivymd.app import MDApp
from kivy.lang import Builder

kv = '''
Screen:

    MDToolbar:
        title: "Car Number Plate Scanner"
        pos_hint: {"top": 1}
        elevation: 10

    MDLabel:
        text: "Scan car number plates from a video feed"
        halign: "center"
'''

class MyApp(MDApp):
    def build(self):
        return Builder.load_string(kv)

if __name__ == "__main__":
    MyApp().run()
