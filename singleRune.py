import random
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty
from kivy.uix.popup import Popup
import sqlite3

class PopupRune(Popup):

	RuneWorp = StringProperty("")
	RuneTeken = StringProperty("")
	RuneTekst = StringProperty("")

class SingleRuneScreen(Screen):

	def Display(self,RuneWorp1,keuze_Credo,keuze_RuneText, keuze_naam):

			self.b = BoxLayout(orientation="vertical")

			self.Image1 = Image(source=RuneWorp1)
			self.b1 = BoxLayout(orientation="vertical",spacing=10)
			self.label1 = Label(text=keuze_naam+": \n"+ keuze_Credo,
								font_size=36,bold=True,halign="left",color=[1,0,0,1], size_hint=(1,.1))
			self.label2 = Label(text="Keywords of the message: \n {}".format(keuze_RuneText),
						   font_size=28,halign="left",text_size=(350, None),color=[1,1,1,1],size_hint=(1,.1))

			self.b1.add_widget(self.label1)
			self.b1.add_widget(self.label2)
			self.b.add_widget(self.Image1)
			self.b.add_widget(self.b1)

			self.PopupWorp = Popup(title="Today's rune for you",
							  separator_color = [1,0,0,.6],
							  content=self.b,
							  title_size=28,
							  size_hint=(None,None),
							  size= (500,700),
							  pos_hint= {"center_x":.5,"center_y":.5},
							  background_color = [0,1,0,1],
							  background="Layout/road.jpg",
							  auto_dismiss=True)

			self.PopupWorp.open()

	def Worp(self):

		conn = sqlite3.connect("dataRunistica.db")
		c = conn.cursor()
		c.execute("SELECT RuneNaam,RuneCredo, RuneText, Signtype FROM Runistica")
		datarune = c.fetchall()

		rune_set = []
		for teken in datarune:
			rune_set.append(teken)

		a = random.choice(range(0, 40))
		keuze_rune = (rune_set[a][0]).lower() + ".png"
		keuze_Credo = rune_set[a][1]
		keuze_RuneText = rune_set[a][2]
		keuze_naam = rune_set[a][0]
		RuneWorp1 = "RunenTekens/" + keuze_rune

		conn.commit()
		conn.close()

		self.Display(RuneWorp1,keuze_Credo,keuze_RuneText, keuze_naam)








