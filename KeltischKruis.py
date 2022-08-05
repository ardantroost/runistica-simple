import random
import sqlite3

from kivy.app import App
from kivy.graphics.instructions import Canvas
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout

class KeltischKruisScreen(Screen):

	def RunenWorp(self):

		conn = sqlite3.connect("dataRunistica.db")
		c = conn.cursor()
		c.execute("SELECT RuneNaam,RuneCredo, RuneText, Signtype FROM Runistica")
		datarune = c.fetchall()

		rune_set = []
		for teken in datarune:
			rune_set.append(teken)

		runeworp = random.sample(rune_set,5)
		print(runeworp)

		conn.commit()
		conn.close()
		self.RunenDisplay(runeworp)

	def RunenDisplay(self,runeworp):

		past = runeworp[0]
		present = runeworp[1]
		future = runeworp[2]
		help = runeworp[3]
		obstacle = runeworp[4]

		self.ids._PastButton.text = runeworp[0][0]
		self.ids._PastImage.source = "RunenTekens/" + (runeworp[0][0]).lower() + ".png"
		self.ids._PresentButton.text =  runeworp[1][0]
		self.ids._PresentImage.source = "RunenTekens/" + (runeworp[1][0]).lower() + ".png"
		self.ids._FutureButton.text =  runeworp[2][0]
		self.ids._FutureImage.source = "RunenTekens/" + (runeworp[2][0]).lower() + ".png"
		self.ids._HelpButton.text =  runeworp[3][0]
		self.ids._HelpImage.source = "RunenTekens/" + (runeworp[3][0]).lower() + ".png"
		self.ids._ObstacleButton.text = runeworp[4][0]
		self.ids._ObstacleImage.source = "RunenTekens/" + (runeworp[4][0]).lower() + ".png"

	def Rune_interpretatie(self, Runesign):

		if Runesign == "Help":

			keuze = self.ids._HelpButton.text
			conn = sqlite3.connect("dataRunistica.db")
			c = conn.cursor()
			c.execute("SELECT RuneNaam,RuneCredo, RuneText FROM Runistica WHERE RuneNaam = (?)", (keuze,))
			runeuitleg = c.fetchone()
			conn.commit()
			conn.close()
			self.Popup_uitleg(runeuitleg)

		elif Runesign == "Past":
			keuze = self.ids._PastButton.text
			conn = sqlite3.connect("dataRunistica.db")
			c = conn.cursor()
			c.execute("SELECT RuneNaam,RuneCredo, RuneText FROM Runistica WHERE RuneNaam = (?)", (keuze,))
			runeuitleg = c.fetchone()
			conn.commit()
			conn.close()
			self.Popup_uitleg(runeuitleg)

		elif Runesign == "Present":
			keuze = self.ids._PresentButton.text
			conn = sqlite3.connect("dataRunistica.db")
			c = conn.cursor()
			c.execute("SELECT RuneNaam,RuneCredo, RuneText FROM Runistica WHERE RuneNaam = (?)", (keuze,))
			runeuitleg = c.fetchone()
			conn.commit()
			conn.close()
			self.Popup_uitleg(runeuitleg)

		elif Runesign == "Future":
			keuze = self.ids._FutureButton.text
			conn = sqlite3.connect("dataRunistica.db")
			c = conn.cursor()
			c.execute("SELECT RuneNaam,RuneCredo, RuneText FROM Runistica WHERE RuneNaam = (?)", (keuze,))
			runeuitleg = c.fetchone()
			conn.commit()
			conn.close()
			self.Popup_uitleg(runeuitleg)

		elif Runesign == "Obstacle":
			keuze = self.ids._ObstacleButton.text
			conn = sqlite3.connect("dataRunistica.db")
			c = conn.cursor()
			c.execute("SELECT RuneNaam,RuneCredo, RuneText FROM Runistica WHERE RuneNaam = (?)", (keuze,))
			runeuitleg = c.fetchone()
			conn.commit()
			conn.close()
			print(runeuitleg)
			self.Popup_uitleg(runeuitleg)

	def Popup_uitleg(self, runeuitleg):

		b = BoxLayout(orientation="vertical")
		Image1 = Image(source="RunenTekens/"+ (runeuitleg[0]).lower()+ ".png")
		b1 = BoxLayout(orientation="vertical", spacing=10)

		label1 = Label(text=runeuitleg[1], font_size=18, bold=True,
					   halign="left", color=[0, 1, 0, 1], size_hint=(1, .1))
		label2 = Label(text=format(runeuitleg[2]), font_size=12,
					   halign="left", text_size=(150, None), color=[0, 1, 0, 1], size_hint=(1, .1))

		b1.add_widget(label1)
		b1.add_widget(label2)
		b.add_widget(Image1)
		b.add_widget(b1)

		PopupUitleg = Popup(title="Interpretation",
							title_color= [0,1,0,1],
							title_size= 18,
							title_align= "justify",
							separator_color = [0,1,0,1],
							separator_height= 1,
						  content=b,
						  size_hint=(None, None),
						  size=(200, 200),
						  pos_hint= {"center_x":.7,"center_y":.25},
							# background_color = [1, 1, 1, 1],
							background = "Layout/road.jpg ",
						  auto_dismiss=True)

		PopupUitleg.open()

class KeltischKruisApp(App):
	def build(self):
		return KeltischKruisScreen()

if __name__ == "__main__":
	KeltischKruisApp.run()