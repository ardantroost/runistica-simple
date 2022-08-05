import random
import sqlite3

from kivy.app import App
from kivy.uix.screenmanager import Screen

class JaNeeScreen(Screen):



	def runensetwerpen(self):

		conn = sqlite3.connect("dataRunistica.db")
		c = conn.cursor()
		c.execute("SELECT RuneNaam,RuneCredo, RuneText, Signtype FROM Runistica")
		datarune = c.fetchall()

		rune_set = []
		for teken in datarune:
			rune_set.append(teken)

		runeworp = random.sample(rune_set, 3)
		print(runeworp)
		conn.commit()
		conn.close()

		self.JaNeeCheck(runeworp)

	def JaNeeCheck(self, runeworp):

		steen1 = runeworp[0][0].find("V")
		steen2 = runeworp[1][0].find("V")
		steen3 = runeworp[2][0].find("V")

		# bereken het aantal omgekeerde runen in de worp
		analyse = (runeworp[0][0].count("V")+runeworp[1][0].count("V")+runeworp[2][0].count("V"))
		#print("Aantal V's in worp bedraagt:{}".format(analyse))

		validatie = False
		# retourneert een negatief getal indien "V" niet in steen
		if steen1 < 0:
			aa = runeworp[1][0].find(runeworp[0][0])
			ab = runeworp[2][0].find(runeworp[0][0])

			if aa >= 0 or ab >= 0:
				validatie = True

		if steen2 < 0:
			ac = runeworp[0][0].find(runeworp[1][0])
			ad = runeworp[2][0].find(runeworp[1][0])

			if ac >= 0 or ad >= 0:
				validatie = True

		if steen3 < 0:
			ae = runeworp[0][0].find(runeworp[2][0])
			af = runeworp[1][0].find(runeworp[2][0])

			if ae >= 0 or af >= 0:
				validatie = True

		if validatie == False:

			self.ids._plaatje1.source = "RunenTekens/"+ (runeworp[0][0]).lower() +".png"
			self.ids._plaatje2.source = "RunenTekens/"+ (runeworp[1][0]).lower() +".png"
			self.ids._plaatje3.source = "RunenTekens/"+ (runeworp[2][0]).lower() +".png"
			self.ids._RuneNaam1.text  = "Runeteken\n" + runeworp[0][0]
			self.ids._RuneNaam2.text  = "Runeteken\n" + runeworp[1][0]
			self.ids._RuneNaam3.text  = "Runeteken\n" + runeworp[2][0]

			antwoord1 = ["The answer is Yes.\nNone of your runes indicate any form of doubt.",
						"The answer is No.\nYour runes indicate a clear no",
						"Overall the answer will be Yes.\nNevertheless the first rune {0} is warning you.This {1} rune is associated with: {2}".format(runeworp[0][0].strip("V"),runeworp[0][3] ,runeworp[0][2]),
						"Overall the answer will be Yes.\nNevertheless the second rune {0} is warning you.This {1} rune is associated with: {2}".format( runeworp[1][0].strip("V"),runeworp[1][3] ,runeworp[1][2]),
						"Overall the answer will be Yes.\nNevertheless the third and last rune {0} is warning you.This {1} rune is associated with: {2}".format( runeworp[2][0].strip("V"),runeworp[2][3], runeworp[2][2] )]
			antwoord2 = ["Finally the answer is No.\nTake caution of the first rune {} in the process. This {} rune stands for: {} ".format(runeworp[0][0],runeworp[0][3],runeworp[0][2]) ,
						"Finally the answer is No.\nTake caution of the second rune {} in the process. This {} rune stands for: {} ".format(runeworp[1][0],runeworp[1][3],runeworp[1][2]),
						"Finally the answer is No.\nTake caution of the third and last rune {} in the process. This {} rune stands for: {} ".format(runeworp[2][0],runeworp[2][3],runeworp[2][2])]

			if analyse == 0:
				self.ids._UitlegAntwoord.text = antwoord1[0]

			elif analyse == 1:
				if "V" in runeworp[0][0]:
					self.ids._UitlegAntwoord.text = antwoord1[2]
				elif "V" in runeworp[1][0]:
					self.ids._UitlegAntwoord.text = antwoord1[3]
				elif "V" in runeworp[2][0]:
					self.ids._UitlegAntwoord.text = antwoord1[4]

			elif analyse == 2:
				if "V" in runeworp[0][0] and "V" in runeworp[1][0]:
					self.ids._UitlegAntwoord.text = antwoord2[2]
				elif "V" in runeworp[1][0] and  "V" in runeworp[2][0]:
					self.ids._UitlegAntwoord.text = antwoord2[0]
				elif "V" in runeworp[0][0] and "V" in runeworp[2][0]:
					self.ids._UitlegAntwoord.text = antwoord2[1]

			elif analyse == 3:
				self.ids._UitlegAntwoord.text = antwoord1[1]

		else:
			print("Runenconflict: opnieuw geworpen!")
			self.runensetwerpen()



class JaNeeApp(App):

	def build(self):
		return JaNeeScreen()
