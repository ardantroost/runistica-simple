import random
import sqlite3

from kivy.app import App
from kivy.graphics.instructions import Canvas
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen

class KeltischKruisScreen(Screen):

	def on_enter(self, *args):

		self.lanquage = self.manager.lanquage
		print(self.lanquage+" !test!")
		if self.lanquage == 'en':
			self.ids._HelpButton.text = "Help"
			self.ids._PastButton.text = "Past"
			self.ids._PresentButton.text = "Present"
			self.ids._FutureButton.text = "Future"
			self.ids._ObstacleButton.text = "Obstacle"
			self.ids._Header.text = \
				"The Celtic Cross\n[color=#FFFFFF][size=24] Fortune telling by a five-runes-reading[/color][/size]"
		elif self.lanquage == 'fr':
			self.ids._HelpButton.text = "l'aide"
			self.ids._PastButton.text = "le passée"
			self.ids._PresentButton.text = "le present"
			self.ids._FutureButton.text = "le future"
			self.ids._ObstacleButton.text = "Les obstacles"
			self.ids._Header.text = \
				"La Croix celtique\n[color=#FFFFFF][size=24] Des prédictions par une lecture de cinq runes[/color][/size]"

		elif self.lanquage == 'de':
			self.ids._HelpButton.text = "Hielfe"
			self.ids._PastButton.text = "Vergangenheit"
			self.ids._PresentButton.text = "Heute"
			self.ids._FutureButton.text ="Zukunft"
			self.ids._ObstacleButton.text = "Hindernisse"
			self.ids._Header.text = \
				"Das keltisches Kreuz\n[color=#FFFFFF][size=24] Wahrsagen durch eine Fünf-Runen-Lesung[/color][/size]"

		elif self.lanquage == 'nl':
			self.ids._HelpButton.text = "Hulp"
			self.ids._PastButton.text = "Verleden"
			self.ids._PresentButton.text = "Heden"
			self.ids._FutureButton.text ="Toekomst"
			self.ids._ObstacleButton.text = "Hindernissen"
			self.ids._Header.text = \
				"Het keltisch Kruis\n[color=#FFFFFF][size=24] Toekomstvoorspelling door een vijf-runen-lezing[/color][/size]"

	def RunenWorp(self):

		conn = sqlite3.connect("dataRunistica_nw.db")
		c = conn.cursor()
		c.execute("SELECT RuneNaam,RuneCredo, RuneText, Signtype FROM Runistica_en")
		datarune = c.fetchall()

		rune_set = []
		for teken in datarune:
			rune_set.append(teken)

		runeworp = random.sample(rune_set,5)

		conn.commit()
		conn.close()
		self.RunenDisplay(runeworp)

	def RunenDisplay(self,runeworp):

		past = runeworp[0]
		present = runeworp[1]
		future = runeworp[2]
		help = runeworp[3]
		obstacle = runeworp[4]


		a= "RunenTekens/" + (runeworp[0][0]).lower() + ".png"
		b= "RunenTekens/" + (runeworp[1][0]).lower() + ".png"
		c= "RunenTekens/" + (runeworp[2][0]).lower() + ".png"
		d= "RunenTekens/" + (runeworp[3][0]).lower() + ".png"
		e= "RunenTekens/" + (runeworp[4][0]).lower() + ".png"
		self.ids._PastButton.text = runeworp[0][0]
		self.ids._PastImage.source = a
		self.ids._PresentButton.text =  runeworp[1][0]
		self.ids._PresentImage.source = b
		self.ids._FutureButton.text =  runeworp[2][0]
		self.ids._FutureImage.source = c
		self.ids._HelpButton.text =  runeworp[3][0]
		self.ids._HelpImage.source = d
		self.ids._ObstacleButton.text = runeworp[4][0]
		self.ids._ObstacleImage.source = e

	def Rune_interpretatie(self, Runesign):

		self.lanquage = self.manager.lanquage

		if Runesign == "Help":
			try:
				keuze = self.ids._HelpButton.text
				conn = sqlite3.connect("dataRunistica_nw.db")
				c = conn.cursor()

				if self.lanquage == 'en':
					c.execute("SELECT RuneNaam,RuneCredo, RuneText FROM Runistica_en WHERE RuneNaam = (?)", (keuze,))
					tekst="Help"
				elif self.lanquage == 'fr':
					c.execute("SELECT RuneNaam,RuneCredo_fr,RuneText_fr, Signtype_fr FROM Runistica_en WHERE RuneNaam = (?)", (keuze,))
					tekst = "l'aide"
				elif self.lanquage == 'de':
					c.execute("SELECT RuneNaam,RuneCredo_de,RuneText_de, Signtype_de FROM Runistica_en WHERE RuneNaam = (?)", (keuze,))
					tekst = "die Hielfe"
				elif self.lanquage == 'nl':
					c.execute("SELECT RuneNaam,RuneCredo_nl,RuneText_nl, Signtype_nl FROM Runistica_en WHERE RuneNaam = (?)", (keuze,))
					tekst = "Hulp"
				runeuitleg = c.fetchone()
				conn.commit()
				conn.close()
				self.Popup_uitleg(runeuitleg,tekst=tekst)
			except:
				self.manager.Popup_Choose("press throw!")

		elif Runesign == "Past":
			try:
				keuze = self.ids._PastButton.text
				conn = sqlite3.connect("dataRunistica_nw.db")
				c = conn.cursor()
				if self.lanquage == 'en':
					c.execute("SELECT RuneNaam,RuneCredo, RuneText FROM Runistica_en WHERE RuneNaam = (?)", (keuze,))
					tekst="the past"
				elif self.lanquage == 'fr':
					c.execute("SELECT RuneNaam,RuneCredo_fr,RuneText_fr, Signtype_fr FROM Runistica_en WHERE RuneNaam = (?)",
						(keuze,))
					tekst="le temps passé"

				elif self.lanquage == 'de':
					c.execute("SELECT RuneNaam,RuneCredo_de,RuneText_de, Signtype_de FROM Runistica_en WHERE RuneNaam = (?)",
						(keuze,))
					tekst = "Vergangenheit"
				elif self.lanquage == 'nl':
					c.execute("SELECT RuneNaam,RuneCredo_nl,RuneText_nl, Signtype_nl FROM Runistica_en WHERE RuneNaam = (?)",
						(keuze,))
					tekst = "het verleden"

				runeuitleg = c.fetchone()
				conn.commit()
				conn.close()
				self.Popup_uitleg(runeuitleg,tekst=tekst)
			except:
				self.manager.Popup_Choose("press throw!")

		elif Runesign == "Present":
			try:
				keuze = self.ids._PresentButton.text
				conn = sqlite3.connect("dataRunistica_nw.db")
				c = conn.cursor()
				if self.lanquage == 'en':
					c.execute("SELECT RuneNaam,RuneCredo, RuneText FROM Runistica_en WHERE RuneNaam = (?)", (keuze,))
					tekst= "the present"
				elif self.lanquage == 'fr':
					c.execute("SELECT RuneNaam,RuneCredo_fr,RuneText_fr, Signtype_fr FROM Runistica_en WHERE RuneNaam = (?)",
						(keuze,))
					tekst = "le present"
				elif self.lanquage == 'de':
					c.execute("SELECT RuneNaam,RuneCredo_de,RuneText_de, Signtype_de FROM Runistica_en WHERE RuneNaam = (?)",
						(keuze,))
					tekst = "heute"
				elif self.lanquage == 'nl':
					c.execute("SELECT RuneNaam,RuneCredo_nl,RuneText_nl, Signtype_nl FROM Runistica_en WHERE RuneNaam = (?)",
						(keuze,))
					tekst = "heute"

				runeuitleg = c.fetchone()
				conn.commit()
				conn.close()
				self.Popup_uitleg(runeuitleg,tekst=tekst)
			except:
				self.manager.Popup_Choose("press throw!")

		elif Runesign == "Future":
			try:
				keuze = self.ids._FutureButton.text
				conn = sqlite3.connect("dataRunistica_nw.db")
				c = conn.cursor()
				if self.lanquage == 'en':
					c.execute("SELECT RuneNaam,RuneCredo, RuneText FROM Runistica_en WHERE RuneNaam = (?)", (keuze,))
					tekst= 'The future'
				elif self.lanquage == 'fr':
					c.execute("SELECT RuneNaam,RuneCredo_fr,RuneText_fr, Signtype_fr FROM Runistica_en WHERE RuneNaam = (?)",
						(keuze,))
					tekst = "le futur"
				elif self.lanquage == 'de':
					c.execute("SELECT RuneNaam,RuneCredo_de,RuneText_de, Signtype_de FROM Runistica_en WHERE RuneNaam = (?)",
						(keuze,))
					tekst = "die Zukunft"
				elif self.lanquage == 'nl':
					c.execute("SELECT RuneNaam,RuneCredo_nl,RuneText_nl, Signtype_nl FROM Runistica_en WHERE RuneNaam = (?)",
						(keuze,))
					tekst = "de toekomst"

				runeuitleg = c.fetchone()
				conn.commit()
				conn.close()
				self.Popup_uitleg(runeuitleg,tekst=tekst)
			except:
				self.manager.Popup_Choose("press throw!")

		elif Runesign == "Obstacle":
			try:
				keuze = self.ids._ObstacleButton.text
				conn = sqlite3.connect("dataRunistica_nw.db")
				c = conn.cursor()
				if self.lanquage == 'en':
					c.execute("SELECT RuneNaam,RuneCredo, RuneText FROM Runistica_en WHERE RuneNaam = (?)", (keuze,))
					tekst= "obstacles"
					self.ids._ObstacleButton.tekst="Obstacle"
				elif self.lanquage == 'fr':
					c.execute("SELECT RuneNaam,RuneCredo_fr,RuneText_fr, Signtype_fr FROM Runistica_en WHERE RuneNaam = (?)",
						(keuze,))
					tekst= "des obstacles"
					self.root.ids._ObstacleButton.tekst = "Obstacles"
				elif self.lanquage == 'de':
					c.execute(
						"SELECT RuneNaam,RuneCredo_de,RuneText_de, Signtype_de FROM Runistica_en WHERE RuneNaam = (?)",
						(keuze,))
					tekst="Hindernisse"
					self.ids._ObstacleButton.tekst = "Obstacle"
				elif self.lanquage == 'nl':
					c.execute("SELECT RuneNaam,RuneCredo_nl,RuneText_nl, Signtype_nl FROM Runistica_en WHERE RuneNaam = (?)",
						(keuze,))
					tekst="obstakels"
					self.ids._ObstacleButton.tekst = "Hindernissen"
				runeuitleg = c.fetchone()
				conn.commit()
				conn.close()
				self.Popup_uitleg(runeuitleg, tekst=tekst)
			except:
				self.manager.Popup_Choose("press throw!")

	def Popup_uitleg(self, runeuitleg, tekst):

		if self.lanquage == "en":
			self.a = "Interpretation of the rune"
			self.c ="--- Regarding "+ format(tekst) +"---"
		if self.lanquage == "fr":
			self.a = "Interprétation de la rune"
			self.c = "--- Quant à " + format(tekst) + "---"
		if self.lanquage == "de":
			self.a = "Interpretation der Rune"
			self.c = "--- Was ihre " + format(tekst) + " angeht""---"
		if self.lanquage == "nl":
			self.a = "Interpretatie van de rune"
			self.c = "--- Wat betreft uw " + format(tekst) + "---"

		b = BoxLayout(orientation="vertical",size_hint=(1,.7))
		Image1 = Image(source="RunenTekens/"+ (runeuitleg[0]).lower()+ ".png",size_hint=(None,None),
					width=120,height=120,allow_stretch=True, keep_ratio=False,pos_hint={"center_x":.5,"center_y":.5})
		b1 = BoxLayout(orientation="vertical",spacing=5)
		label1 = Label(text=runeuitleg[0]+":\n"+runeuitleg[1], font_size=36, bold=True,
					   halign="left", color=[1, 0, 0, 1], size_hint=(1, .1))
		label3 = Label(text=format(runeuitleg[2]), font_size=28,
					   halign="left", text_size=(350, None), color=[1, 1, 1, 1], size_hint=(1, .1))
		label2 = Label(text=self.c, font_size=28,
					   halign="left",color=[1, 1, 1, 1], size_hint=(1, .1))

		b1.add_widget(label1)
		b1.add_widget(label2)
		b1.add_widget(label3)
		b.add_widget(Image1)
		b.add_widget(b1)

		PopupUitleg = Popup(title=self.a,
							title_color= [1,1,1,1],
							title_size= 36,
							title_align= "justify",
							separator_color = [0,1,0,1],
							separator_height= 1,
							content=b,
						  	size_hint=(None, None),
						  	size=(500, 700),
						  	pos_hint= {"center_x":.5,"center_y":.5},
							background_color=[1, 1, 1, 1],
							background="Layout/road.jpg",
							auto_dismiss=True)

		PopupUitleg.open()

class KeltischKruisApp(App):
	def build(self):
		return KeltischKruisScreen()

if __name__ == "__main__":
	KeltischKruisApp.run()