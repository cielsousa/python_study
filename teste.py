from kivy.app import App
from kivy.uix.widget import Widget


class PongBall(Widget):
    VElocity_x = NumericProperty(0)

class MyGame(Widget):
    pass


class MyApp(App):
    def build(self):
        return MyGame()
    

if __name__ == '__main__':
    MyApp().run()