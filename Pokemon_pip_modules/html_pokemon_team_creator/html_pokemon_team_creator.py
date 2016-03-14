import os
import sys

class PokemonCreator:
	def __init__(self):
		filename = raw_input("Filename? ")
		os.system('touch ' + filename)
		apm = open(filename, 'w')
		self.head(apm)
		self.body(apm)
		apm.close()	

	# writes html for header
	def head(self, apm):
		apm.write("<!DOCTYPE html>\n")
		apm.write("<html>\n")
		apm.write("<head>\n")
		title = raw_input("Title? ")
		self.addcss(apm)
		apm.write("<title>" + title + "</title>\n")
		apm.write("</head>\n")

	# writes html for body
	def body(self, apm):
		nameone = raw_input("Pokemon One? ")
		ability = raw_input("Ability? ")
		item = raw_input("Held Item? ")
		moveone = raw_input("Move 1? ")
		movetwo = raw_input("Move 2? ")
		movethree = raw_input("Move 3? ")
		movefour = raw_input("Move 4? ")
		nature = raw_input("Nature? ")
		nametwo = raw_input("Pokemon Two? ")
		abilitytwo = raw_input("Ability? ")
		itemtwo = raw_input("Held Item? ")
		twomoveone = raw_input("Move 1? ")
		twomovetwo = raw_input("Move 2? ")
		twomovethree = raw_input("Move 3? ")
		twomovefour = raw_input("Move 4? ")
		naturetwo = raw_input("Nature? ")
		namethree = raw_input("Pokemon Three? ")
		abilitythree = raw_input("Ability? ")
		itemthree = raw_input("Held Item? ")
		threemoveone = raw_input("Move 1? ")
		threemovetwo = raw_input("Move 2? ")
		threemovethree = raw_input("Move 3? ")
		threemovefour = raw_input("Move 4? ")
		naturethree = raw_input("Nature? ")
		namefour = raw_input("Pokemon Four? ")
		abilityfour = raw_input("Ability? ")
		itemfour = raw_input("Held Item? ")
		fourmoveone = raw_input("Move 1? ")
		fourmovetwo = raw_input("Move 2? ")
		fourmovethree = raw_input("Move 3? ")
		fourmovefour = raw_input("Move 4? ")
		naturefour = raw_input("Nature? ")
		namefive = raw_input("Pokemon Five? ")
		abilityfive = raw_input("Ability? ")
		itemfive = raw_input("Held Item? ")
		fivemoveone = raw_input("Move 1? ")
		fivemovetwo = raw_input("Move 2? ")
		fivemovethree = raw_input("Move 3? ")
		fivemovefour = raw_input("Move 4? ")
		naturefive = raw_input("Nature? ")
		namesix = raw_input("Pokemon Six? ")
		abilitysix = raw_input("Ability? ")
		itemsix = raw_input("Held Item? ")
		sixmoveone = raw_input("Move 1? ")
		sixmovetwo = raw_input("Move 2? ")
		sixmovethree = raw_input("Move 3? ")
		sixmovefour = raw_input("Move 4? ")
		naturesix = raw_input("Nature? ")
		apm.write("<body>\n")
		apm.write("\t<h2>Pokemon Team List</h2>\n")
		apm.write("\t<table id='outputTable'>\n")
		apm.write("\t\t<tbody>\n")
		apm.write("\t\t\t<tr>\n")
		apm.write("\t\t\t\t<td>\n")
		apm.write("\t\t\t\t\t<table class='ptable'>\n")
		apm.write("\t\t\t\t\t\t<tbody>\n")
		apm.write("\t\t\t\t\t\t\t<tr>\n")
		apm.write("\t\t\t\t\t\t\t\t<th class='label'>Pokemon: </th>\n")
		apm.write("\t\t\t\t\t\t\t\t<td>" + nameone + "</td>\n")
		apm.write("\t\t\t\t\t\t\t</tr>\n")
		apm.write("\t\t\t\t\t\t\t<tr>\n")
		apm.write("\t\t\t\t\t\t\t\t<th class='label'>Ability: </th>\n")
		apm.write("\t\t\t\t\t\t\t\t<td>" + ability + "</td>\n")
		apm.write("\t\t\t\t\t\t\t</tr>\n")
		apm.write("\t\t\t\t\t\t\t<tr>\n")
		apm.write("\t\t\t\t\t\t\t\t<th class='label'>Held Item: </th>\n")
		apm.write("\t\t\t\t\t\t\t\t<td>" + item + "</td>\n")
		apm.write("\t\t\t\t\t\t\t</tr>\n")
		apm.write("\t\t\t\t\t\t\t<tr>\n")
		apm.write("\t\t\t\t\t\t\t\t<th class='label'>Move 1: </th>\n")
		apm.write("\t\t\t\t\t\t\t\t<td>" + moveone + "</td>\n")
		apm.write("\t\t\t\t\t\t\t</tr>\n")
		apm.write("\t\t\t\t\t\t\t<tr>\n")
		apm.write("\t\t\t\t\t\t\t\t<th class='label'>Move 2: </th>\n")
		apm.write("\t\t\t\t\t\t\t\t<td>" + movetwo + "</td>\n")
		apm.write("\t\t\t\t\t\t\t</tr>\n")
		apm.write("\t\t\t\t\t\t\t<tr>\n")
		apm.write("\t\t\t\t\t\t\t\t<th class='label'>Move 3: </th>\n")
		apm.write("\t\t\t\t\t\t\t\t<td>" + movethree + "</td>\n")
		apm.write("\t\t\t\t\t\t\t</tr>\n")
		apm.write("\t\t\t\t\t\t\t<tr>\n")
		apm.write("\t\t\t\t\t\t\t\t<th class='label'>Move 4: </th>\n")
		apm.write("\t\t\t\t\t\t\t\t<td>" + movefour + "</td>\n")
		apm.write("\t\t\t\t\t\t\t</tr>\n")
		apm.write("\t\t\t\t\t\t\t<tr>\n")
		apm.write("\t\t\t\t\t\t\t\t<th class='label'>Nature: </th>\n")
		apm.write("\t\t\t\t\t\t\t\t<td>" + nature + "</td>\n")
		apm.write("\t\t\t\t\t\t\t</tr>\n")
		apm.write("\t\t\t\t\t\t</tbody>\n")
		apm.write("\t\t\t\t\t</table>\n")
		apm.write("\t\t\t\t</td>\n")
		apm.write("\t\t\t\t<td>\n")
		apm.write("\t\t\t\t\t<table class='ptable'>\n")
		apm.write("\t\t\t\t\t\t<tbody>\n")
		apm.write("\t\t\t\t\t\t\t<tr>\n")
		apm.write("\t\t\t\t\t\t\t\t<th class='label'>Pokemon: </th>\n")
		apm.write("\t\t\t\t\t\t\t\t<td>" + nametwo + "</td>\n")
		apm.write("\t\t\t\t\t\t\t</tr>\n")
		apm.write("\t\t\t\t\t\t\t<tr>\n")
		apm.write("\t\t\t\t\t\t\t\t<th class='label'>Ability: </th>\n")
		apm.write("\t\t\t\t\t\t\t\t<td>" + abilitytwo + "</td>\n")
		apm.write("\t\t\t\t\t\t\t</tr>\n")
		apm.write("\t\t\t\t\t\t\t<tr>\n")
		apm.write("\t\t\t\t\t\t\t\t<th class='label'>Held Item: </th>\n")
		apm.write("\t\t\t\t\t\t\t\t<td>" + itemtwo + "</td>\n")
		apm.write("\t\t\t\t\t\t\t</tr>\n")
		apm.write("\t\t\t\t\t\t\t<tr>\n")
		apm.write("\t\t\t\t\t\t\t\t<th class='label'>Move 1: </th>\n")
		apm.write("\t\t\t\t\t\t\t\t<td>" + twomoveone + "</td>\n")
		apm.write("\t\t\t\t\t\t\t</tr>\n")
		apm.write("\t\t\t\t\t\t\t<tr>\n")
		apm.write("\t\t\t\t\t\t\t\t<th class='label'>Move 2: </th>\n")
		apm.write("\t\t\t\t\t\t\t\t<td>" + twomovetwo + "</td>\n")
		apm.write("\t\t\t\t\t\t\t</tr>\n")
		apm.write("\t\t\t\t\t\t\t<tr>\n")
		apm.write("\t\t\t\t\t\t\t\t<th class='label'>Move 3: </th>\n")
		apm.write("\t\t\t\t\t\t\t\t<td>" + twomovethree + "</td>\n")
		apm.write("\t\t\t\t\t\t\t</tr>\n")
		apm.write("\t\t\t\t\t\t\t<tr>\n")
		apm.write("\t\t\t\t\t\t\t\t<th class='label'>Move 4: </th>\n")
		apm.write("\t\t\t\t\t\t\t\t<td>" + twomovefour + "</td>\n")
		apm.write("\t\t\t\t\t\t\t</tr>\n")
		apm.write("\t\t\t\t\t\t\t<tr>\n")
		apm.write("\t\t\t\t\t\t\t\t<th class='label'>Nature: </th>\n")
		apm.write("\t\t\t\t\t\t\t\t<td>" + naturetwo + "</td>\n")
		apm.write("\t\t\t\t\t\t\t</tr>\n")
		apm.write("\t\t\t\t\t\t\t</tr>\n")
		apm.write("\t\t\t\t\t\t</tbody>\n")
		apm.write("\t\t\t\t\t</table>\n")
		apm.write("\t\t\t\t</td>\n")
		apm.write("\t\t\t\t<br>\n")
		apm.write("\t\t\t\t<td>\n")
		apm.write("\t\t\t\t\t<table class='ptable'>\n")
		apm.write("\t\t\t\t\t\t<tbody>\n")
		apm.write("\t\t\t\t\t\t\t<tr>\n")
		apm.write("\t\t\t\t\t\t\t\t<th class='label'>Pokemon: </th>\n")
		apm.write("\t\t\t\t\t\t\t\t<td>" + namethree + "</td>\n")
		apm.write("\t\t\t\t\t\t\t</tr>\n")
		apm.write("\t\t\t\t\t\t\t<tr>\n")
		apm.write("\t\t\t\t\t\t\t\t<th class='label'>Ability: </th>\n")
		apm.write("\t\t\t\t\t\t\t\t<td>" + abilitythree + "</td>\n")
		apm.write("\t\t\t\t\t\t\t</tr>\n")
		apm.write("\t\t\t\t\t\t\t<tr>\n")
		apm.write("\t\t\t\t\t\t\t\t<th class='label'>Held Item: </th>\n")
		apm.write("\t\t\t\t\t\t\t\t<td>" + itemthree + "</td>\n")
		apm.write("\t\t\t\t\t\t\t</tr>\n")
		apm.write("\t\t\t\t\t\t\t<tr>\n")
		apm.write("\t\t\t\t\t\t\t\t<th class='label'>Move 1: </th>\n")
		apm.write("\t\t\t\t\t\t\t\t<td>" + threemoveone + "</td>\n")
		apm.write("\t\t\t\t\t\t\t</tr>\n")
		apm.write("\t\t\t\t\t\t\t<tr>\n")
		apm.write("\t\t\t\t\t\t\t\t<th class='label'>Move 2: </th>\n")
		apm.write("\t\t\t\t\t\t\t\t<td>" + threemovetwo + "</td>\n")
		apm.write("\t\t\t\t\t\t\t</tr>\n")
		apm.write("\t\t\t\t\t\t\t<tr>\n")
		apm.write("\t\t\t\t\t\t\t\t<th class='label'>Move 3: </th>\n")
		apm.write("\t\t\t\t\t\t\t\t<td>" + threemovethree + "</td>\n")
		apm.write("\t\t\t\t\t\t\t</tr>\n")
		apm.write("\t\t\t\t\t\t\t<tr>\n")
		apm.write("\t\t\t\t\t\t\t\t<th class='label'>Move 4: </th>\n")
		apm.write("\t\t\t\t\t\t\t\t<td>" + threemovefour + "</td>\n")
		apm.write("\t\t\t\t\t\t\t</tr>\n")
		apm.write("\t\t\t\t\t\t\t<tr>\n")
		apm.write("\t\t\t\t\t\t\t\t<th class='label'>Nature: </th>\n")
		apm.write("\t\t\t\t\t\t\t\t<td>" + naturethree + "</td>\n")
		apm.write("\t\t\t\t\t\t\t</tr>\n")
		apm.write("\t\t\t\t\t\t\t</tr>\n")
		apm.write("\t\t\t\t\t\t</tbody>\n")
		apm.write("\t\t\t\t\t</table>\n")
		apm.write("\t\t\t\t</td>\n")
		apm.write("\t\t\t</tr>\n")
		apm.write("\t\t</tbody>\n")
		apm.write("\t</table>\n")
		apm.write("\t<table id='outputTable'>\n")
		apm.write("\t\t<tbody>\n")
		apm.write("\t\t\t<tr>\n")
		apm.write("\t\t\t\t<td>\n")
		apm.write("\t\t\t\t\t<table class='ptable'>\n")
		apm.write("\t\t\t\t\t\t<tbody>\n")
		apm.write("\t\t\t\t\t\t\t<tr>\n")
		apm.write("\t\t\t\t\t\t\t\t<th class='label'>Pokemon: </th>\n")
		apm.write("\t\t\t\t\t\t\t\t<td>" + namefour + "</td>\n")
		apm.write("\t\t\t\t\t\t\t</tr>\n")
		apm.write("\t\t\t\t\t\t\t<tr>\n")
		apm.write("\t\t\t\t\t\t\t\t<th class='label'>Ability: </th>\n")
		apm.write("\t\t\t\t\t\t\t\t<td>" + abilityfour + "</td>\n")
		apm.write("\t\t\t\t\t\t\t</tr>\n")
		apm.write("\t\t\t\t\t\t\t<tr>\n")
		apm.write("\t\t\t\t\t\t\t\t<th class='label'>Held Item: </th>\n")
		apm.write("\t\t\t\t\t\t\t\t<td>" + itemfour + "</td>\n")
		apm.write("\t\t\t\t\t\t\t</tr>\n")
		apm.write("\t\t\t\t\t\t\t<tr>\n")
		apm.write("\t\t\t\t\t\t\t\t<th class='label'>Move 1: </th>\n")
		apm.write("\t\t\t\t\t\t\t\t<td>" + fourmoveone + "</td>\n")
		apm.write("\t\t\t\t\t\t\t</tr>\n")
		apm.write("\t\t\t\t\t\t\t<tr>\n")
		apm.write("\t\t\t\t\t\t\t\t<th class='label'>Move 2: </th>\n")
		apm.write("\t\t\t\t\t\t\t\t<td>" + fourmovetwo + "</td>\n")
		apm.write("\t\t\t\t\t\t\t</tr>\n")
		apm.write("\t\t\t\t\t\t\t<tr>\n")
		apm.write("\t\t\t\t\t\t\t\t<th class='label'>Move 3: </th>\n")
		apm.write("\t\t\t\t\t\t\t\t<td>" + fourmovethree + "</td>\n")
		apm.write("\t\t\t\t\t\t\t</tr>\n")
		apm.write("\t\t\t\t\t\t\t<tr>\n")
		apm.write("\t\t\t\t\t\t\t\t<th class='label'>Move 4: </th>\n")
		apm.write("\t\t\t\t\t\t\t\t<td>" + fourmovefour + "</td>\n")
		apm.write("\t\t\t\t\t\t\t</tr>\n")
		apm.write("\t\t\t\t\t\t\t<tr>\n")
		apm.write("\t\t\t\t\t\t\t\t<th class='label'>Nature: </th>\n")
		apm.write("\t\t\t\t\t\t\t\t<td>" + naturefour + "</td>\n")
		apm.write("\t\t\t\t\t\t\t</tr>\n")
		apm.write("\t\t\t\t\t\t\t</tr>\n")
		apm.write("\t\t\t\t\t\t</tbody>\n")
		apm.write("\t\t\t\t\t</table>\n")
		apm.write("\t\t\t\t</td>\n")
		apm.write("\t\t\t\t<br>\n")
		apm.write("\t\t\t\t<td>\n")
		apm.write("\t\t\t\t\t<table class='ptable'>\n")
		apm.write("\t\t\t\t\t\t<tbody>\n")
		apm.write("\t\t\t\t\t\t\t<tr>\n")
		apm.write("\t\t\t\t\t\t\t\t<th class='label'>Pokemon: </th>\n")
		apm.write("\t\t\t\t\t\t\t\t<td>" + namefive + "</td>\n")
		apm.write("\t\t\t\t\t\t\t</tr>\n")
		apm.write("\t\t\t\t\t\t\t<tr>\n")
		apm.write("\t\t\t\t\t\t\t\t<th class='label'>Ability: </th>\n")
		apm.write("\t\t\t\t\t\t\t\t<td>" + abilityfive + "</td>\n")
		apm.write("\t\t\t\t\t\t\t</tr>\n")
		apm.write("\t\t\t\t\t\t\t<tr>\n")
		apm.write("\t\t\t\t\t\t\t\t<th class='label'>Held Item: </th>\n")
		apm.write("\t\t\t\t\t\t\t\t<td>" + itemfive + "</td>\n")
		apm.write("\t\t\t\t\t\t\t</tr>\n")
		apm.write("\t\t\t\t\t\t\t<tr>\n")
		apm.write("\t\t\t\t\t\t\t\t<th class='label'>Move 1: </th>\n")
		apm.write("\t\t\t\t\t\t\t\t<td>" + fivemoveone + "</td>\n")
		apm.write("\t\t\t\t\t\t\t</tr>\n")
		apm.write("\t\t\t\t\t\t\t<tr>\n")
		apm.write("\t\t\t\t\t\t\t\t<th class='label'>Move 2: </th>\n")
		apm.write("\t\t\t\t\t\t\t\t<td>" + fivemovetwo + "</td>\n")
		apm.write("\t\t\t\t\t\t\t</tr>\n")
		apm.write("\t\t\t\t\t\t\t<tr>\n")
		apm.write("\t\t\t\t\t\t\t\t<th class='label'>Move 3: </th>\n")
		apm.write("\t\t\t\t\t\t\t\t<td>" + fivemovethree + "</td>\n")
		apm.write("\t\t\t\t\t\t\t</tr>\n")
		apm.write("\t\t\t\t\t\t\t<tr>\n")
		apm.write("\t\t\t\t\t\t\t\t<th class='label'>Move 4: </th>\n")
		apm.write("\t\t\t\t\t\t\t\t<td>" + fivemovefour + "</td>\n")
		apm.write("\t\t\t\t\t\t\t</tr>\n")
		apm.write("\t\t\t\t\t\t\t<tr>\n")
		apm.write("\t\t\t\t\t\t\t\t<th class='label'>Nature: </th>\n")
		apm.write("\t\t\t\t\t\t\t\t<td>" + naturefive + "</td>\n")
		apm.write("\t\t\t\t\t\t\t</tr>\n")
		apm.write("\t\t\t\t\t\t\t</tr>\n")
		apm.write("\t\t\t\t\t\t</tbody>\n")
		apm.write("\t\t\t\t\t</table>\n")
		apm.write("\t\t\t\t</td>\n")
		apm.write("\t\t\t\t<td>\n")
		apm.write("\t\t\t\t\t<table class='ptable'>\n")
		apm.write("\t\t\t\t\t\t<tbody>\n")
		apm.write("\t\t\t\t\t\t\t<tr>\n")
		apm.write("\t\t\t\t\t\t\t\t<th class='label'>Pokemon: </th>\n")
		apm.write("\t\t\t\t\t\t\t\t<td>" + namesix + "</td>\n")
		apm.write("\t\t\t\t\t\t\t</tr>\n")
		apm.write("\t\t\t\t\t\t\t<tr>\n")
		apm.write("\t\t\t\t\t\t\t\t<th class='label'>Ability: </th>\n")
		apm.write("\t\t\t\t\t\t\t\t<td>" + abilitysix + "</td>\n")
		apm.write("\t\t\t\t\t\t\t</tr>\n")
		apm.write("\t\t\t\t\t\t\t<tr>\n")
		apm.write("\t\t\t\t\t\t\t\t<th class='label'>Held Item: </th>\n")
		apm.write("\t\t\t\t\t\t\t\t<td>" + itemsix + "</td>\n")
		apm.write("\t\t\t\t\t\t\t</tr>\n")
		apm.write("\t\t\t\t\t\t\t<tr>\n")
		apm.write("\t\t\t\t\t\t\t\t<th class='label'>Move 1: </th>\n")
		apm.write("\t\t\t\t\t\t\t\t<td>" + sixmoveone + "</td>\n")
		apm.write("\t\t\t\t\t\t\t</tr>\n")
		apm.write("\t\t\t\t\t\t\t<tr>\n")
		apm.write("\t\t\t\t\t\t\t\t<th class='label'>Move 2: </th>\n")
		apm.write("\t\t\t\t\t\t\t\t<td>" + sixmovetwo + "</td>\n")
		apm.write("\t\t\t\t\t\t\t</tr>\n")
		apm.write("\t\t\t\t\t\t\t<tr>\n")
		apm.write("\t\t\t\t\t\t\t\t<th class='label'>Move 3: </th>\n")
		apm.write("\t\t\t\t\t\t\t\t<td>" + sixmovethree + "</td>\n")
		apm.write("\t\t\t\t\t\t\t</tr>\n")
		apm.write("\t\t\t\t\t\t\t<tr>\n")
		apm.write("\t\t\t\t\t\t\t\t<th class='label'>Move 4: </th>\n")
		apm.write("\t\t\t\t\t\t\t\t<td>" + sixmovefour + "</td>\n")
		apm.write("\t\t\t\t\t\t\t</tr>\n")
		apm.write("\t\t\t\t\t\t\t<tr>\n")
		apm.write("\t\t\t\t\t\t\t\t<th class='label'>Nature: </th>\n")
		apm.write("\t\t\t\t\t\t\t\t<td>" + naturesix + "</td>\n")
		apm.write("\t\t\t\t\t\t\t</tr>\n")
		apm.write("\t\t\t\t\t\t</tbody>\n")
		apm.write("\t\t\t\t\t</table>\n")
		apm.write("\t\t\t\t</td>\n")
		apm.write("\t\t\t</tr>\n")
		apm.write("\t\t<tbody>\n")
		apm.write("\t</table>\n")
		apm.write("</body>\n")
		apm.write("</html>\n")

	def addcss(self, apm):
		addstyle = raw_input("Add Style (Yes or No)? ")
		if addstyle == 'yes':
			apm.write("<style>\n")
			apm.write("\t#outputTable {\n")
			apm.write("\t\twidth: 80%;\n")
			apm.write("\t\tborder: 1px solid black;\n")
			apm.write("\t } \n")
			apm.write("\t.ptable { \n")
			apm.write("\t\tdisplay: table; \n")
			apm.write("\t\twidth: 300px;\n")
			apm.write("\t\tborder: 1px solid black\n")
			apm.write("\t } \n")
			apm.write("\t .ptable td { \n")
			apm.write("\t\tfont-size: 1.5em; \n")
			apm.write("\t\tdisplay: table-cell; \n")
			apm.write("\t\tvertical-align: inherit; \n")
			apm.write("\t\tborder: 1px solid black")
			apm.write("\t } \n")
			apm.write("\t h2 { \n")
			apm.write("\t\t font-size: 1.5em;\n")
			apm.write("\t\t -webkit-margin-before: 0.83em;\n")
			apm.write("\t\t -webkit-margin-after: 0.83em\n")
			apm.write("\t\t -webkit-margin-start: 0px;\n")
			apm.write("\t\t -webkit-margin-end: 0px;\n")
			apm.write("\t\t vertical-align: inherit;\n")
			apm.write("\t\t font-weight: bold;\n")
			apm.write("\t } \n")
			apm.write("</style>")
		elif addstyle == "no":
			print 'Style not being added'
		else:
			print 'did not understand'
			self.addstyle(apm)

page = PokemonCreator()