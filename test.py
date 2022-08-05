import kivy
from kivy.config import Config
Config.set('graphics', 'width',350)
Config.set('graphics', 'height',700)
Config.set('graphics', 'resizable',1)

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

#def write_rune(datarune, Runefolder):

#	with open(Runefolder,"wb") as file:
#		file.write(datarune)

class DezeApp(BoxLayout):
	pass

class TestApp (App):
	def build(self):
		return DezeApp()

if __name__ == "__main__":

	TestApp().run()