from kivy.config import Config
Config.set('graphics', 'width',350)
Config.set('graphics', 'height',700)
Config.set('graphics', 'resizable',1)

from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager

Builder.load_file('Welcome.kv')
Builder.load_file('Settings.kv')
Builder.load_file('JaNee.kv')
Builder.load_file('KeltischKruis.kv')
Builder.load_file('SingleRune.kv')

class RunenScreenManager(ScreenManager):
	pass

class RunenApp(App):
	def build(self):
		return RunenScreenManager()

if __name__== "__main__":
	RunenApp().run()