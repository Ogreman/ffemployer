import tkinter
from job import Job
from PIL import Image, ImageTk

class ff_job_roll(tkinter.Tk):

    def __init__(self,parent):
        tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialise()

    # main menu. new game, load progress
    # new game: FF1, FF3 NES, FF3 iOS, FF5 (any/melee/magic), FF12, BD
	def initialise(self):

		def start_game(self, game, new_game_frame, ff3new_frame):
			def OnFF3WindButtonClick(
				windButton,
				fireButton,
				windLabel,
				windPicLabel,
				windStatsLabel,
				summaryText
			):
				windButton['state'] = 'disabled'
				windButton['text'] = 'Wind Crystal Complete!'
				fireButton['state'] = 'normal'

				windLabel.grid(column=0,row=1)
				windPicLabel.grid(column=0,row=3,columnspan=1,sticky='WE')
				windStatsLabel.grid(column=0,row=4,columnspan=1)

				summaryText.set("Defeat Salamander to unlock fire jobs...")

			def OnFF3FireButtonClick(
				fireButton,
				waterButton,
				fireLabel,
				firePicLabel,
				fireStatsLabel,
				summaryText
			):
				fireButton['state'] = 'disabled'
				fireButton['text'] = 'Fire Crystal Complete!'
				waterButton['state'] = 'normal'

				fireLabel.grid(column=1,row=1)
				firePicLabel.grid(column=1,row=3,columnspan=1,sticky='WE')
				fireStatsLabel.grid(column=1,row=4,columnspan=1)

				summaryText.set("Defeat Salamander to unlock water jobs...")

			def OnFF3WaterButtonClick(
				waterButton,
				earthButton,
				waterLabel,
				waterPicLabel,
				waterStatsLabel,
				summaryText
			):
				waterButton['state'] = 'disabled'
				waterButton['text'] = 'Water Crystal Complete!'
				earthButton['state'] = 'normal'

				waterLabel.grid(column=2,row=1)
				waterPicLabel.grid(column=2,row=3,columnspan=1,sticky='WE')
				waterStatsLabel.grid(column=2,row=4,columnspan=1)

				summaryText.set("Defeat Salamander to unlock earth jobs...")

			def OnFF3EarthButtonClick(
				earthButton,
				earthLabel,
				earthPicLabel,
				earthStatsLabel,
				summaryText
			):
				earthButton['state'] = 'disabled'
				earthButton['text'] = 'Earth Crystal Complete!'

				earthLabel.grid(column=3,row=1)
				earthPicLabel.grid(column=3,row=3,columnspan=1,sticky='WE')
				earthStatsLabel.grid(column=3,row=4,columnspan=1)

				summaryText.set("COMPLETE THE CRYSTAL TOWER!")

			self.configure(background='white')
			self.geometry("800x430")
			#ff3new_frame = tkinter.Frame(self)
			new_game_frame.destroy()
			statsFont=('Helvetica', 18)

			#ff3new_frame.destroy()
			ff3new_frame.pack()


			'''counter = 0
			for f in self.winfo_children():
				counter += 1

			if counter == 2:

				ff3new_frame.pack()
			else:
				print("destroying")
				ff3new_frame.destroy()
				ff3new_frame = tkinter.Frame(self)
				ff3new_frame.pack()'''


			ff3new_frame.configure(bg="white")
			#self.configure(background='white')
			#self.geometry("800x430")
			labelFont=('Helvetica', 24)

			windLabelVariable = tkinter.StringVar()
			fireLabelVariable = tkinter.StringVar()
			waterLabelVariable = tkinter.StringVar()
			earthLabelVariable = tkinter.StringVar()

			windStatsText = tkinter.StringVar()
			fireStatsText = tkinter.StringVar()
			waterStatsText = tkinter.StringVar()
			earthStatsText = tkinter.StringVar()
			summaryText = tkinter.StringVar()

			#
			windJob = Job()
			windJobText = windJob.roll_job(game,"wind")
			(windStats, windJobPath) = windJob.return_job_info(game, windJobText)
			windLabelVariable.set(windJobText)

			#
			windStatsText.set("STR: " + windStats[0] +
				"\nAGL: " + windStats[1] +
				"\nVIT: " + windStats[2] +
				"\nINT: " + windStats[3] +
				"\nMND: " + windStats[4])

			#
			fireJob = Job()
			fireJobText = fireJob.roll_job(game,"fire")
			(fireStats, fireJobPath) = fireJob.return_job_info(game, fireJobText)
			fireLabelVariable.set(fireJobText)

			#
			fireStatsText.set("STR: " + fireStats[0] +
				"\nAGL: " + fireStats[1] +
				"\nVIT: " + fireStats[2] +
				"\nINT: " + fireStats[3] +
				"\nMND: " + fireStats[4])

			#
			waterJob = Job()
			waterJobText = waterJob.roll_job(game,"water")
			(waterStats, waterJobPath) = waterJob.return_job_info(game, waterJobText)
			waterLabelVariable.set(waterJobText)

			#
			waterStatsText.set("STR: " + waterStats[0] +
				"\nAGL: " + waterStats[1] +
				"\nVIT: " + waterStats[2] +
				"\nINT: " + waterStats[3] +
				"\nMND: " + waterStats[4])

			#
			earthJob = Job()
			earthJobText = earthJob.roll_job(game,"earth")
			(earthStats, earthJobPath) = earthJob.return_job_info(game, earthJobText)
			earthLabelVariable.set(earthJobText)

			#
			earthStatsText.set("STR: " + earthStats[0] +
				"\nAGL: " + earthStats[1] +
				"\nVIT: " + earthStats[2] +
				"\nINT: " + earthStats[3] +
				"\nMND: " + earthStats[4])

			#
			summaryLabel = tkinter.Label(
				ff3new_frame,
				textvariable=summaryText,
				anchor="w",
				fg="white",
				bg="black"
			)
			windStatsLabel = tkinter.Label(
				ff3new_frame,
				textvariable=windStatsText
			)
			fireStatsLabel = tkinter.Label(
				ff3new_frame,
				textvariable=fireStatsText
			)
			waterStatsLabel = tkinter.Label(
				ff3new_frame,
				textvariable=waterStatsText
			)
			earthStatsLabel = tkinter.Label(
				ff3new_frame,
				textvariable=earthStatsText
			)

			#
			windImage = ImageTk.PhotoImage(Image.open(windJobPath))
			fireImage = ImageTk.PhotoImage(Image.open(fireJobPath))
			waterImage = ImageTk.PhotoImage(Image.open(waterJobPath))
			earthImage = ImageTk.PhotoImage(Image.open(earthJobPath))

			#
			windLabel = tkinter.Label(
				ff3new_frame,
				textvariable=windLabelVariable
			)
			fireLabel = tkinter.Label(
				ff3new_frame,
				textvariable=fireLabelVariable
			)
			waterLabel = tkinter.Label(
				ff3new_frame,
				textvariable=waterLabelVariable
			)
			earthLabel = tkinter.Label(
				ff3new_frame,
				textvariable=earthLabelVariable
			)

			#
			windPicLabel = tkinter.Label(ff3new_frame, image=windImage)
			windPicLabel.image = windImage
			firePicLabel = tkinter.Label(ff3new_frame, image=fireImage)
			firePicLabel.image = fireImage
			waterPicLabel = tkinter.Label(ff3new_frame, image=waterImage)
			waterPicLabel.image = waterImage
			earthPicLabel = tkinter.Label(ff3new_frame, image=earthImage)
			earthPicLabel.image = earthImage

			#windPicLabel.grid(column=0,row=3,columnspan=1,sticky='WE')
			#
			windButton = tkinter.Button(
				ff3new_frame,
				text=u"Wind Crystal Get!",
				state='normal'
			)
			fireButton = tkinter.Button(
				ff3new_frame,
				text=u"Fire Crystal Get!",
				state='disabled'
			)
			waterButton = tkinter.Button(
				ff3new_frame,
				text=u"Water Crystal Get!",
				state='disabled'
			)
			earthButton = tkinter.Button(
				ff3new_frame,
				text=u"Earth Crystal Get!",
				state='disabled'
			)

			#
			windStatsLabel.config(anchor="center",font=statsFont,bg='white')
			fireStatsLabel.config(anchor="center",font=statsFont,bg='white')
			waterStatsLabel.config(anchor="center",font=statsFont,bg='white')
			earthStatsLabel.config(anchor="center",font=statsFont,bg='white')

			#
			summaryLabel.grid(column=0,row=2,columnspan=4,sticky='EW')
			summaryLabel.config(height=2,anchor='center')
			summaryText.set(u"Defeat Salamander to unlock wind jobs...")

			#
			windLabel.config(font=labelFont,bg='white')
			fireLabel.config(font=labelFont,bg='white')
			waterLabel.config(font=labelFont,bg='white')
			earthLabel.config(font=labelFont,bg='white')

			#
			windButton.grid(column=0,row=0,sticky='EW')
			fireButton.grid(column=1,row=0,sticky='EW')
			waterButton.grid(column=2,row=0,sticky='EW')
			earthButton.grid(column=3,row=0,sticky='EW')

			#
			windButton.config(
				height=2,
				command=lambda: OnFF3WindButtonClick(
					windButton,
					fireButton,
					windLabel,
					windPicLabel,
					windStatsLabel,
					summaryText
				)
			)
			fireButton.config(
				height=2,
				command=lambda: OnFF3FireButtonClick(
					fireButton,
					waterButton,
					fireLabel,
					firePicLabel,
					fireStatsLabel,
					summaryText
				)
			)
			waterButton.config(
				height=2,
				command=lambda: OnFF3WaterButtonClick(
					waterButton,
					earthButton,
					waterLabel,
					waterPicLabel,
					waterStatsLabel,
					summaryText
				)
			)
			earthButton.config(
				height=2,
				command=lambda: OnFF3EarthButtonClick(
					earthButton,
					earthLabel,
					earthPicLabel,
					earthStatsLabel,
					summaryText
				)
			)

	        # Stretches components in column 0 with window resize
			ff3new_frame.grid_columnconfigure(0,minsize=200,weight=1)
			ff3new_frame.grid_columnconfigure(1,minsize=200,weight=1)
			ff3new_frame.grid_columnconfigure(2,minsize=200,weight=1)
			ff3new_frame.grid_columnconfigure(3,minsize=200,weight=1)

	        # Resizable: Horizontal no, vertical no
			self.resizable(False,False)

		def ff1():
			print("ff1")

		def ff3nes():
			start_game("ff3n")

		def ff3new(new_game_frame, ff3new_frame):
			start_game(self, "ff3r", new_game_frame, ff3new_frame)

		def ff5():
			print("ff5")

		def ff12():
			print("ff12 izjs")

		def bravelyd():
			print("Bravely Default")

		self.grid()

		menuBar = tkinter.Menu()

		newGameMenu = tkinter.Menu(menuBar, tearoff=0)
		newGameMenu.add_command(label="Final Fantasy I", command=ff1)
		newGameMenu.add_command(label="Final Fantasy III (NES)", command=ff3nes)
		newGameMenu.add_command(
			label="Final Fantasy III (Remake)",
			command=lambda: ff3new(
				new_game_frame,
				ff3new_frame
			 )
		)
		newGameMenu.add_command(label="Final Fantasy V", command=ff5)
		newGameMenu.add_command(
			label="Final Fantasy XII International",
			command=ff12
		)
		newGameMenu.add_command(label="Bravely Default", command=bravelyd)
		menuBar.add_cascade(label="New Game", menu=newGameMenu)
		self.config(menu=menuBar)

		new_game_frame = tkinter.Frame(self)
		ff3new_frame = tkinter.Frame(self)
		new_game_frame.configure(bg="white")
		ff3rButton = tkinter.Button(
			new_game_frame,
			text=u"Final Fantasy III!",
			state='normal'
		)
		ff3rButton.config(
			height=2,
			command=lambda: ff3new(
				new_game_frame,
				ff3new_frame
			)
		)
		ff3rButton.grid(column=0,row=0,sticky='EW')
		new_game_frame.pack()

		self.update()
		self.geometry("800x430")
		self.configure(background='white')

if __name__ == "__main__":
	app = ff_job_roll(None)
	app.title('FF Employer: Now Hiring for Final Fantasy III (Remake)')
	app.mainloop()
