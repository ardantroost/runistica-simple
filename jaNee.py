import random
import sqlite3

from kivy.app import App
from kivy.uix.screenmanager import Screen

class JaNeeScreen(Screen):

	def on_enter(self):

		self.lanquage = self.manager.lanquage

		if self.lanquage == "en":
			self.ids._Header.text="Yes-or-No\n [color=#FFFFFF][size=24]Throw three runes and get your answer[/color][/size]"
			self.ids._UitlegAntwoord.text="Ask a yes-or-no question\n and throw the runestones"
		if self.lanquage == "de":
			self.ids._Header.text="Ja-oder-Nein\n [color=#FFFFFF][size=24]Wirf drei Runen und erhalte eine Antwort[/color][/size]"
			self.ids._UitlegAntwoord.text="Stellen Sie eine Ja-oder-Nein-Frage\n und werfen Sie die Runensteine"
		if self.lanquage == "fr":
			self.ids._Header.text="Oui-ou-Non\n [color=#FFFFFF][size=24]Lancez trois runes et obtiennez une réponse[/color][/size]"
			self.ids._UitlegAntwoord.text="Posez d'abord une question par oui ou par non, puis lancez les pierres runiques"
		if self.lanquage == "nl":
			self.ids._Header.text="Ja-of-Néé\n [color=#FFFFFF][size=24]Gooi drie runen en krijg antwoord op je vraag{/color][/size]"
			self.ids._UitlegAntwoord.text="Stel allereerst een ja-nee-vraag en gooi vervolgens de runenstenen."

	def runensetwerpen(self):

		self.lanquage = self.manager.lanquage

		#conn = sqlite3.connect("dataRunistica.db")
		conn = sqlite3.connect("dataRunistica_nw.db")
		c = conn.cursor()

		if self.lanquage == 'en':
			#c.execute("SELECT RuneNaam,RuneCredo_en,RuneText_en, Signtype_en FROM Runistica")
			c.execute("SELECT RuneNaam,RuneCredo,RuneText, Signtype FROM Runistica_en")
		elif self.lanquage == 'fr':
			#c.execute("SELECT RuneNaam,RuneCredo_fr,RuneText_fr, Signtype_fr FROM Runistica")
			c.execute("SELECT RuneNaam,RuneCredo,RuneText, Signtype FROM Runistica_fr")
		elif self.lanquage == 'de':
			#c.execute("SELECT RuneNaam,RuneCredo_de,RuneText_de, Signtype_de FROM Runistica")
			c.execute("SELECT RuneNaam,RuneCredo,RuneText, Signtype FROM Runistica_de")
		elif self.lanquage == 'nl':
			#c.execute("SELECT RuneNaam,RuneCredo_nl,RuneText_nl, Signtype_nl FROM Runistica")
			c.execute("SELECT RuneNaam,RuneCredo,RuneText, Signtype FROM Runistica_nl")
		#c.execute("SELECT RuneNaam,RuneCredo, RuneText, Signtype FROM Runistica")

		datarune = c.fetchall()

		rune_set = []
		for teken in datarune:
			rune_set.append(teken)

		runeworp = random.sample(rune_set, 3)

		conn.commit()
		conn.close()

		self.JaNeeCheck(runeworp)

	def JaNeeCheck(self, runeworp):

		self.lanquage = self.manager.lanquage

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
			self.ids._RuneNaam1.text  = runeworp[0][0]
			self.ids._RuneNaam2.text  = runeworp[1][0]
			self.ids._RuneNaam3.text  = runeworp[2][0]

		if self.lanquage == 'en':
				self.antwoord1 = ["The answer is Yes.\nNone of your runes show any sign of doubt about it.",
						"The answer is No.\nYour runes indicate a clear no",
						"Overall the answer will be Yes.\nNevertheless the first rune {0} is warning you.This {1} rune is associated with: {2}".format(runeworp[0][0].strip("V"),runeworp[0][3] ,runeworp[0][2]),							"Overall the answer will be Yes.\nNevertheless the second rune {0} is warning you.This {1} rune is associated with: {2}".format( runeworp[1][0].strip("V"),runeworp[1][3] ,runeworp[1][2]),
							"Overall the answer will be Yes.\nNevertheless the third and last rune {0} is warning you.This {1} rune is associated with: {2}".format( runeworp[2][0].strip("V"),runeworp[2][3], runeworp[2][2] )]
				self.antwoord2 = ["Finally the answer is No.\nTake caution of the first rune {}. This {} rune stands for: {} ".format(runeworp[0][0],runeworp[0][3],runeworp[0][2]) ,
							"Finally the answer is No.\nTake caution of the second rune {}. This {} rune stands for: {} ".format(runeworp[1][0],runeworp[1][3],runeworp[1][2]),
							"Finally the answer is No.\nTake caution of the third and last rune {}. This {} rune stands for: {} ".format(runeworp[2][0],runeworp[2][3],runeworp[2][2])]

		elif self.lanquage == 'fr':
				self.antwoord1 = ["La réponse est oui.\nAucune de vos runes n'indique un signe de doute.",
							 "La réponse est non.\nVos runes indiquent un non clair",
							 "En général, la réponse sera oui.\nSoit prudente, la première rune {0} vous avertit. Cette rune, {1}, signifie : {2}".format(runeworp[0][0].strip("V"), runeworp[0][3], runeworp[0][2]),
							 "En général, la réponse sera oui.\nSoit prudente, la deuxième rune {0} vous avertit. Cette rune, {1}, signifie : {2}".format(runeworp[1][0].strip("V"), runeworp[1][3], runeworp[1][2]),
							 "En général, la réponse sera oui.\nSoit prudente, la dernière rune {0} vous avertit. Cette rune, {1}, signifie : {2}".format(runeworp[2][0].strip("V"), runeworp[2][3], runeworp[2][2])]
				self.antwoord2 = ["Finalement le respons sera Non.\nFaites attention à la première rune {} du lancer. Cette rune {} signifie : {} ".format(runeworp[0][0], runeworp[0][3], runeworp[0][2]),
							"Finalement le respons sera Non.\nFaites attention à la deuxième rune {} du lancer. Cette rune, {}, signifie : {} ".format(runeworp[1][0], runeworp[1][3], runeworp[1][2]),
							"Finalement le respons sera Non.\nFaites attention à la dernière rune {} du lancer. Cette rune, {}, signifie : {} ".format(runeworp[2][0], runeworp[2][3], runeworp[2][2])]
		elif self.lanquage == 'nl':
				self.antwoord1 = ["Het antwoord is Ja.\nGeen enkele rune vertoont twijfel.",
							 "Het antwoord is Néé.\nJouw runen geven daarover een heel duidelijk signaal af",
							 "Uiteindelijk zal het anwoord toch Ja zijn. \nLet op de eerste rune {0} die waarschuwt echter . Deze rune , {1}, houdt verband met: {2}".format(runeworp[0][0].strip("V"), runeworp[0][3], runeworp[0][2]),
							 "Uiteindelijk is het anwoord toch Ja.\nLet op de tweede rune {0} die waarschuwt echter. Deze rune , {1}, houdt verband met: {2}".format(runeworp[1][0].strip("V"), runeworp[1][3], runeworp[1][2]),
							 "Uiteindelijk zal het anwoord toch Ja zijn.\nLet op de derde en laatste rune {0} die waarschuwt echter. Deze rune , {1}, houdt verband met: {2}".format(runeworp[2][0].strip("V"), runeworp[2][3], runeworp[2][2])]
				self.antwoord2 = ["Uiteindelijk is het antwoord wel degelijk Ja.\nLet op de eerste rune {0} die waarschuwt. Deze rune {1} houdt verband met: {2}".format(runeworp[0][0], runeworp[0][3], runeworp[0][2]),
							"Uiteindelijk is het antwoord toch Néé.\nLet op de tweede rune {0} die waarschuwt. Deze rune {1} houdt verband met: {2}".format(runeworp[1][0], runeworp[1][3], runeworp[1][2]),
							"Uiteindelijk is het antwoord toch Néé.\nLet op de laatste rune {0} die waarschuwt echter. Deze rune {1} houdt verband met: {2}".format(runeworp[2][0], runeworp[2][3], runeworp[2][2])]
		elif self.lanquage == 'de':
				self.antwoord1 = ["Die Antwort ist ja.\nKeine Ihrer Runen weist auf irgendeinen Zweifel hin .",
							 "The answer is No.\nIhre Runen zeigen ein klares Nein",
							 "Insgesamt ist die Antwort Ja.\nTrotzdem warnt die erste Rune {0}. Diese Rune, {1}, ist verbunden mit: {2}".format(runeworp[0][0].strip("V"), runeworp[0][3], runeworp[0][2]),
							 "Insgesamt ist die Antwort Ja.\nTrotzdem warnt die zweite Rune {0}. Diese Rune,{1}, ist verbunden mit: {2}".format(runeworp[1][0].strip("V"), runeworp[1][3], runeworp[1][2]),
							 "Insgesamt ist die Antwort Ja.\nTrotzdem warnt die dritte und letzte Rune {0}. Diese Rune,{1}, ist verbunden mit: {2}".format(runeworp[2][0].strip("V"), runeworp[2][3], runeworp[2][2])]
				self.antwoord2 = ["Irgendwann wird die Antwort nein sein.\nAchten Sie dabei auf die erste Rune {}. Diese Rune, {}, ist verbunden mit: {} ".format(runeworp[0][0], runeworp[0][3], runeworp[0][2]),
							"Irgendwann wird die Antwort nein sein.\nAchten Sie dabei auf die zweite Rune {}. Diese Rune, {}, Rune ist verbunden mit: {} ".format(runeworp[1][0], runeworp[1][3], runeworp[1][2]),
							"Irgendwann wird die Antwort nein sein.\nAchten Sie dabei auf die dritte und letzte Rune {}. Diese Rune, {}, ist verbunden mit: {} ".format(runeworp[2][0], runeworp[2][3], runeworp[2][2])]

		if analyse == 0:
					self.ids._UitlegAntwoord.text = self.antwoord1[0]

		elif analyse == 1:
					if "V" in runeworp[0][0]:
						self.ids._UitlegAntwoord.text = self.antwoord1[2]
					elif "V" in runeworp[1][0]:
						self.ids._UitlegAntwoord.text = self.antwoord1[3]
					elif "V" in runeworp[2][0]:
						self.ids._UitlegAntwoord.text = self.antwoord1[4]

		elif analyse == 2:
					if "V" in runeworp[0][0] and "V" in runeworp[1][0]:
						self.ids._UitlegAntwoord.text = self.antwoord2[2]
					elif "V" in runeworp[1][0] and  "V" in runeworp[2][0]:
						self.ids._UitlegAntwoord.text = self.antwoord2[0]
					elif "V" in runeworp[0][0] and "V" in runeworp[2][0]:
						self.ids._UitlegAntwoord.text = self.antwoord2[1]

		elif analyse == 3:
					self.ids._UitlegAntwoord.text = self.antwoord1[1]

		else:
			self.runensetwerpen()

class JaNeeApp(App):

	def build(self):
		return JaNeeScreen()
