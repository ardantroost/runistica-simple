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

			lijst_b = ["Today's rune for you", "votre rune pour aujourd'hui", "Ihre Rune für heute", "Jouw Dagrune"]
			lijst_a = ["Keywords of the message: \n {}","Schlüsselwörter der Nachricht: \n {}","Mots clés du message: \n {}","Kenwoorden van de boodschap: \n {}"]

			if self.lanquage == "en":
				self.lijst = lijst_b[0]
				self.lijs= lijst_a[0]
			if self.lanquage == "fr":
				self.lijst = lijst_b[1]
				self.lijs = lijst_a[2]
			if self.lanquage == "de":
				self.lijst = lijst_b[2]
				self.lijs = lijst_a[1]
			if self.lanquage == "nl":
				self.lijst = lijst_b[3]
				self.lijs = lijst_a[3]

			self.b = BoxLayout(orientation="vertical",size_hint=(1,.7))

			self.Image1 = Image(source=RuneWorp1, size_hint=(None,None),
					width=120,height=120,allow_stretch=True, keep_ratio=False,pos_hint={"center_x":.5,"center_y":.5})
			self.b1 = BoxLayout(orientation="vertical",spacing=10)
			self.label1 = Label(text=keuze_naam+": \n"+ keuze_Credo,
								font_size=36,bold=True,halign="left",color=[1,0,0,1], size_hint=(1,.1))
			self.label2 = Label(text= self.lijs.format(keuze_RuneText),
								font_size=28,halign="left",text_size=(350, None),color=[1,1,1,1],size_hint=(1,.1))
			self.b1.add_widget(self.label1)
			self.b1.add_widget(self.label2)
			self.b.add_widget(self.Image1)
			self.b.add_widget(self.b1)

			self.PopupWorp = Popup(title=self.lijst,
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

		self.lanquage = self.manager.lanquage

		if self.lanquage == 'en':
			c.execute("SELECT RuneNaam,RuneCredo_en,RuneText_en, Signtype_en FROM Runistica")
		elif self.lanquage == 'fr':
			c.execute("SELECT RuneNaam,RuneCredo_fr,RuneText_fr, Signtype_fr FROM Runistica")
		elif self.lanquage == 'de':
			c.execute("SELECT RuneNaam,RuneCredo_de,RuneText_de, Signtype_de FROM Runistica")
		elif self.lanquage == 'nl':
			c.execute("SELECT RuneNaam,RuneCredo_nl,RuneText_nl, Signtype_nl FROM Runistica")

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








