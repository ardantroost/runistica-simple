from kivy.config import Config

Config.set('graphics', 'width',350)
Config.set('graphics', 'height',700)
Config.set('graphics', 'resizable',1)


from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.properties import StringProperty,ListProperty

Builder.load_file('welcome.kv')
Builder.load_file('settings.kv')
Builder.load_file('jaNee.kv')
Builder.load_file('keltischKruis.kv')
Builder.load_file('singleRune.kv')

class RunenScreenManager(ScreenManager):

		lanquage = StringProperty("")
		press_text = ListProperty([])
		RuneCredo= StringProperty("")
		RuneText = StringProperty("")
		Signtype = StringProperty("")

		press_text_Ned = ["Jouw\nDagRune\nwerpen", "Ja-of-Néé\nvragen\stellen", "Een\nopenvraag\nstellen"]
		Throw_button = ["Throw\n the runes","Gooi\n de runen","Wirf\n ihre Runen","Lance\n les runes"]
		press_text_Eng = ["Throw\n Today's\n rune", "Yes-or-No\n Questions", "Pose\n an open\n question"]
		press_text_Dts = ["Wirf\n ihre\nTagesrune", "Ja-oder-Nein\nFragen", "Eine\noffene Frage\nstellen"]
		press_text_Fra = ["Lancez\nvotre\nrune du jour", "Oui\nou\nNon", "Posez\nune question\nouverte"]

		def vertaling(self):

			self.screens[1].ids._B3.text = self.press_text[2]
			self.screens[1].ids._B2.text = self.press_text[1]
			self.screens[1].ids._B1.text = self.press_text[0]
			self.screens[4].ids._B4a.text = self.Throw_button
			self.screens[3].ids._B4c.text = self.Throw_button
			self.screens[2].ids._B4b.text = self.Throw_button

		def Proef(self, taal):

			self.RuneCredo = "RuneCredo"+"_"+taal
			self.RuneText = "RuneText"+"_"+taal
			self.Signtype = "Signtype"+"_"+taal

			if self.lanquage == "en":
				self.press_text = self.press_text_Eng
				self.Throw_button = self.Throw_button[0]

			elif self.lanquage == "nl":
				self.press_text = self.press_text_Ned
				self.Throw_button = self.Throw_button[1]

			elif self.lanquage == "de":
				self.press_text = self.press_text_Dts
				self.Throw_button = self.Throw_button[2]

			elif self.lanquage == "fr":

				self.press_text = self.press_text_Fra
				self.Throw_button = self.Throw_button[3]

			self.vertaling()
			return self.press_text


		# op te roepen Popup in de hele APP
		# call met:   self.manager.Popup_Choose(infotype)
		# infotype om mee te geven: ......

		def Popup_Choose(self, infotype):

			self.PopupPressed = Popup(title="Warning",
									  title_color=[1, 1, 1, 1],
									  title_size=36,
									  separator_color=[0, 1, 0, .6],
									  content=Label(text=f"Please\n{infotype}", halign="center", font_size=28),
									  size_hint=(None, None),
									  size=(300, 500),
									  pos_hint={"center_x": .5, "center_y": .5},
									  background_color=[0, 1, 0, .6],
									  auto_dismiss=True)
			self.PopupPressed.open()

class MainApp(App):

	def build(self):
		# 256 x 256 pixels
		self.icon = "icon.png"

		return RunenScreenManager()

if __name__== "__main__":
	MainApp().run()