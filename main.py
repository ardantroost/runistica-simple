from kivy.config import Config

Config.set('graphics', 'width',350)
Config.set('graphics', 'height',700)
Config.set('graphics', 'resizable',1)

from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager

Builder.load_file('welcome.kv')
Builder.load_file('settings.kv')
Builder.load_file('jaNee.kv')
Builder.load_file('keltischKruis.kv')
Builder.load_file('singleRune.kv')

class RunenScreenManager(ScreenManager):
	pass

class MainApp(App):
	def build(self):
		return RunenScreenManager()

if __name__== "__main__":
	MainApp().run()