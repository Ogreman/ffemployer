import random

class Job():
	def roll_job(self, game, tier):
		if ("ff3r" in game):
			if ("wind" in tier):
				jobs = ['Warrior','Monk','White Mage','Black Mage','Red Mage','Thief']
				windJob = random.choice(jobs)
				return windJob
			elif ("fire" in tier):
				jobs = ['Ranger','Knight','Scholar','Geomancer']
				fireJob = random.choice(jobs)
				return fireJob
			elif ("water" in tier):
				jobs = ['Dragoon','Viking','Dark Knight','Evoker','Bard']
				waterJob = random.choice(jobs)
				return waterJob
			elif ("earth" in tier):
				jobs = ['Black Belt','Devout','Magus','Summoner','Sage','Ninja']
				earthJob = random.choice(jobs)
				return earthJob
		elif ("ff3n" in game):
			if ("wind" in tier):
				jobs = ['Warrior','Monk','White Mage','Black Mage','Red Mage']
				windJob = random.choice(jobs)
				return windJob
			elif ("fire" in tier):
				jobs = ['Ranger','Knight','Scholar','Thief']
				fireJob = random.choice(jobs)
				return fireJob
			elif ("water" in tier):
				jobs = ['Dragoon','Viking','Dark Knight','Evoker','Bard','Geomancer','Black Belt']
				waterJob = random.choice(jobs)
				return waterJob
			elif ("earth" in tier):
				jobs = ['Devout','Magus','Summoner']
				earthJob = random.choice(jobs)
				return earthJob

	def return_job_info(self, game, jobName):
		#print(self.game + " " + self.jobName)
		#
		if ("ff3r" in game):
			if ("White Mage" in jobName):
				stat = [self.get_grade(52),self.get_grade(63),self.get_grade(63),self.get_grade(45),self.get_grade(71)]
				jobPic = "images/WhiteMage.gif"
			elif ("Warrior" in jobName):
				stat= [self.get_grade(71),self.get_grade(71),self.get_grade(63),self.get_grade(45),self.get_grade(45)]
				jobPic = "images/Warrior.gif"
			elif ("Black Mage" in jobName):
				stat= [self.get_grade(52),self.get_grade(63),self.get_grade(63),self.get_grade(71),self.get_grade(45)]
				jobPic = "images/BlackMage.gif"
			elif ("Red Mage" in jobName):
				stat= [self.get_grade(52),self.get_grade(52),self.get_grade(63),self.get_grade(63),self.get_grade(63)]
				jobPic = "images/RedMage.gif"
			elif ("Monk" in jobName):
				stat= [self.get_grade(85),self.get_grade(63),self.get_grade(71),self.get_grade(38),self.get_grade(45)]
				jobPic = "images/Monk.gif"
			elif ("Thief" in jobName):
				stat= [self.get_grade(63),self.get_grade(99),self.get_grade(63),self.get_grade(45),self.get_grade(38)]
				jobPic = "images/Thief.gif"
			elif ("Ranger" in jobName):
				stat= [self.get_grade(71),self.get_grade(85),self.get_grade(63),self.get_grade(45),self.get_grade(45)]
				jobPic = "images/Ranger.gif"
			elif ("Dark Knight" in jobName):
				stat= [self.get_grade(71),self.get_grade(52),self.get_grade(71),self.get_grade(52),self.get_grade(52)]
				jobPic = "images/DarkKnight.gif"
			elif ("Knight" in jobName):
				stat= [self.get_grade(85),self.get_grade(45),self.get_grade(85),self.get_grade(45),self.get_grade(52)]
				jobPic = "images/Knight.gif"
			elif ("Scholar" in jobName):
				stat= [self.get_grade(63),self.get_grade(71),self.get_grade(38),self.get_grade(99),self.get_grade(45)]
				jobPic = "images/Scholar.gif"
			elif ("Geomancer" in jobName):
				stat= [self.get_grade(52),self.get_grade(71),self.get_grade(52),self.get_grade(71),self.get_grade(52)]
				jobPic = "images/Geomancer.gif"
			elif ("Dragoon" in jobName):
				stat= [self.get_grade(71),self.get_grade(71),self.get_grade(52),self.get_grade(52),self.get_grade(52)]
				jobPic = "images/Dragoon.gif"
			elif ("Viking" in jobName):
				stat= [self.get_grade(99),self.get_grade(45),self.get_grade(71),self.get_grade(45),self.get_grade(52)]
				jobPic = "images/Viking.gif"
			elif ("Evoker" in jobName):
				stat= [self.get_grade(63),self.get_grade(52),self.get_grade(45),self.get_grade(71),self.get_grade(71)]
				jobPic = "images/Evoker.gif"
			elif ("Bard" in jobName):
				stat= [self.get_grade(45),self.get_grade(63),self.get_grade(63),self.get_grade(63),self.get_grade(63)]
				jobPic = "images/Bard.gif"
			elif ("Black Belt" in jobName):
				stat= [self.get_grade(99),self.get_grade(71),self.get_grade(99),self.get_grade(38),self.get_grade(38)]
				jobPic = "images/BlackBelt.gif"
			elif ("Devout" in jobName):
				stat= [self.get_grade(45),self.get_grade(63),self.get_grade(52),self.get_grade(52),self.get_grade(99)]
				jobPic = "images/Devout.gif"
			elif ("Magus" in jobName):
				stat= [self.get_grade(45),self.get_grade(63),self.get_grade(52),self.get_grade(99),self.get_grade(52)]
				jobPic = "images/Magus.gif"
			elif ("Summoner" in jobName):
				stat= [self.get_grade(45),self.get_grade(45),self.get_grade(52),self.get_grade(85),self.get_grade(85)]
				jobPic = "images/Summoner.gif"
			elif ("Sage" in jobName):
				stat= [self.get_grade(38),self.get_grade(38),self.get_grade(63),self.get_grade(85),self.get_grade(85)]
				jobPic = "images/Sage.gif"
			elif ("Ninja" in jobName):
				stat= [self.get_grade(71),self.get_grade(85),self.get_grade(52),self.get_grade(52),self.get_grade(52)]
				jobPic = "images/Ninja.gif"
		elif ("ff3n" in game):
			if ("White Mage" in jobName):
				stat = [self.get_grade(52),self.get_grade(63),self.get_grade(63),self.get_grade(45),self.get_grade(71)]
				jobPic = "images/WhiteMage.gif"
			elif ("Warrior" in jobName):
				stat= [self.get_grade(71),self.get_grade(71),self.get_grade(63),self.get_grade(45),self.get_grade(45)]
				jobPic = "images/Warrior.gif"
			elif ("Black Mage" in jobName):
				stat= [self.get_grade(52),self.get_grade(63),self.get_grade(63),self.get_grade(71),self.get_grade(45)]
				jobPic = "images/BlackMage.gif"
			elif ("Red Mage" in jobName):
				stat= [self.get_grade(52),self.get_grade(52),self.get_grade(63),self.get_grade(63),self.get_grade(63)]
				jobPic = "images/RedMage.gif"
			elif ("Monk" in jobName):
				stat= [self.get_grade(85),self.get_grade(63),self.get_grade(71),self.get_grade(38),self.get_grade(45)]
				jobPic = "images/Monk.gif"
			elif ("Thief" in jobName):
				stat= [self.get_grade(63),self.get_grade(99),self.get_grade(63),self.get_grade(45),self.get_grade(38)]
				jobPic = "images/Thief.gif"
			elif ("Ranger" in jobName):
				stat= [self.get_grade(71),self.get_grade(85),self.get_grade(63),self.get_grade(45),self.get_grade(45)]
				jobPic = "images/Ranger.gif"
			elif ("Dark Knight" in jobName):
				stat= [self.get_grade(71),self.get_grade(52),self.get_grade(71),self.get_grade(52),self.get_grade(52)]
				jobPic = "images/DarkKnight.gif"
			elif ("Knight" in jobName):
				stat= [self.get_grade(85),self.get_grade(45),self.get_grade(85),self.get_grade(45),self.get_grade(52)]
				jobPic = "images/Knight.gif"
			elif ("Scholar" in jobName):
				stat= [self.get_grade(63),self.get_grade(71),self.get_grade(38),self.get_grade(99),self.get_grade(45)]
				jobPic = "images/Scholar.gif"
			elif ("Geomancer" in jobName):
				stat= [self.get_grade(52),self.get_grade(71),self.get_grade(52),self.get_grade(71),self.get_grade(52)]
				jobPic = "images/Geomancer.gif"
			elif ("Dragoon" in jobName):
				stat= [self.get_grade(71),self.get_grade(71),self.get_grade(52),self.get_grade(52),self.get_grade(52)]
				jobPic = "images/Dragoon.gif"
			elif ("Viking" in jobName):
				stat= [self.get_grade(99),self.get_grade(45),self.get_grade(71),self.get_grade(45),self.get_grade(52)]
				jobPic = "images/Viking.gif"
			elif ("Evoker" in jobName):
				stat= [self.get_grade(63),self.get_grade(52),self.get_grade(45),self.get_grade(71),self.get_grade(71)]
				jobPic = "images/Evoker.gif"
			elif ("Bard" in jobName):
				stat= [self.get_grade(45),self.get_grade(63),self.get_grade(63),self.get_grade(63),self.get_grade(63)]
				jobPic = "images/Bard.gif"
			elif ("Black Belt" in jobName):
				stat= [self.get_grade(99),self.get_grade(71),self.get_grade(99),self.get_grade(38),self.get_grade(38)]
				jobPic = "images/BlackBelt.gif"
			elif ("Devout" in jobName):
				stat= [self.get_grade(45),self.get_grade(63),self.get_grade(52),self.get_grade(52),self.get_grade(99)]
				jobPic = "images/Devout.gif"
			elif ("Magus" in jobName):
				stat= [self.get_grade(45),self.get_grade(63),self.get_grade(52),self.get_grade(99),self.get_grade(52)]
				jobPic = "images/Magus.gif"
			elif ("Summoner" in jobName):
				stat= [self.get_grade(45),self.get_grade(45),self.get_grade(52),self.get_grade(85),self.get_grade(85)]
				jobPic = "images/Summoner.gif"
			elif ("Sage" in jobName):
				stat= [self.get_grade(38),self.get_grade(38),self.get_grade(63),self.get_grade(85),self.get_grade(85)]
				jobPic = "images/Sage.gif"
			elif ("Ninja" in jobName):
				stat= [self.get_grade(71),self.get_grade(85),self.get_grade(52),self.get_grade(52),self.get_grade(52)]
				jobPic = "images/Ninja.gif"
		return stat, jobPic

	#def get_job_pic(self, game, jobName):
		#if ("ff3" in game):


    # A+ A B+ B C+ C D+ D E F
	def get_grade(self, score):
		if (score < 10):
			return "F"
		elif (score < 20):
			return "E"
		elif (score < 30):
			return "D"
		elif (score < 40):
			return "D+"
		elif (score < 50):
			return "C"
		elif (score < 60):
			return "C+"
		elif (score < 70):
			return "B"
		elif (score < 80):
			return "B+"
		elif (score < 90):
			return "A"
		elif (score < 99):
			return "A+"
		elif (score == 99):
			return "A++"
		else:
			return "ERROR"