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

	def RunenWorp(self):

		conn = sqlite3.connect("dataRunistica.db")
		c = conn.cursor()
		c.execute("SELECT RuneNaam,RuneCredo, RuneText, Signtype FROM Runistica")
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

		if Runesign == "Help":

			keuze = self.ids._HelpButton.text
			conn = sqlite3.connect("dataRunistica.db")
			c = conn.cursor()
			c.execute("SELECT RuneNaam,RuneCredo, RuneText FROM Runistica WHERE RuneNaam = (?)", (keuze,))
			runeuitleg = c.fetchone()
			conn.commit()
			conn.close()
			self.Popup_uitleg(runeuitleg,tekst="Help")

		elif Runesign == "Past":
			keuze = self.ids._PastButton.text
			conn = sqlite3.connect("dataRunistica.db")
			c = conn.cursor()
			c.execute("SELECT RuneNaam,RuneCredo, RuneText FROM Runistica WHERE RuneNaam = (?)", (keuze,))
			runeuitleg = c.fetchone()
			conn.commit()
			conn.close()
			self.Popup_uitleg(runeuitleg,tekst="Past")

		elif Runesign == "Present":
			keuze = self.ids._PresentButton.text
			conn = sqlite3.connect("dataRunistica.db")
			c = conn.cursor()
			c.execute("SELECT RuneNaam,RuneCredo, RuneText FROM Runistica WHERE RuneNaam = (?)", (keuze,))
			runeuitleg = c.fetchone()
			conn.commit()
			conn.close()
			self.Popup_uitleg(runeuitleg,tekst="Present")

		elif Runesign == "Future":
			keuze = self.ids._FutureButton.text
			conn = sqlite3.connect("dataRunistica.db")
			c = conn.cursor()
			c.execute("SELECT RuneNaam,RuneCredo, RuneText FROM Runistica WHERE RuneNaam = (?)", (keuze,))
			runeuitleg = c.fetchone()
			conn.commit()
			conn.close()
			self.Popup_uitleg(runeuitleg,tekst="Future")

		elif Runesign == "Obstacle":
			keuze = self.ids._ObstacleButton.text
			conn = sqlite3.connect("dataRunistica.db")
			c = conn.cursor()
			c.execute("SELECT RuneNaam,RuneCredo, RuneText FROM Runistica WHERE RuneNaam = (?)", (keuze,))
			runeuitleg = c.fetchone()
			conn.commit()
			conn.close()

			self.Popup_uitleg(runeuitleg, tekst="Obstacle")

	def Popup_uitleg(self, runeuitleg, tekst):

		b = BoxLayout(orientation="vertical",size_hint=(1,.7))
		Image1 = Image(source="RunenTekens/"+ (runeuitleg[0]).lower()+ ".png",size_hint=(None,None),
					width=120,height=120,allow_stretch=True, keep_ratio=False,pos_hint={"center_x":.5,"center_y":.5})
		b1 = BoxLayout(orientation="vertical",spacing=5)
		label1 = Label(text=runeuitleg[0]+":\n"+runeuitleg[1], font_size=36, bold=True,
					   halign="left", color=[1, 0, 0, 1], size_hint=(1, .1))
		label3 = Label(text=format(runeuitleg[2]), font_size=28,
					   halign="left", text_size=(350, None), color=[1, 1, 1, 1], size_hint=(1, .1))
		label2 = Label(text="---Regarding your "+ format(tekst) +"---", font_size=28,
					   halign="left",color=[1, 1, 1, 1], size_hint=(1, .1))

		b1.add_widget(label1)
		b1.add_widget(label2)
		b1.add_widget(label3)
		b.add_widget(Image1)
		b.add_widget(b1)

		PopupUitleg = Popup(title="Interpretation",
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