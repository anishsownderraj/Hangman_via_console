# Module for GUI
from tkinter import *
from PIL import Image, ImageTk
import tkinter as Tkr


class WelcomePage(object):

	def __init__ (self, main_window, HEIGHT, WIDTH):
		canvas = Tkr.Canvas(main_window, height=HEIGHT, width=WIDTH)
		canvas.pack()

		# IMAGE
		background_image = ImageTk.PhotoImage(file = 'WildWest.jpg')
		background_label = Tkr.Label(main_window, image=background_image)
		background_label.image = background_image
		background_label.place(relx=0, rely=0, relwidth=1,relheight=1,anchor= NW)

		# BUTTON
		button = Tkr.Button(main_window, text = "Start Game!", font=50)
		button.pack()
		# lace(anchor=N, relwidth= 0.15, relheight = 0.15 )


# Instatiating a window, and keeping it displaying
main_window = Tkr.Tk()
g = WelcomePage(main_window,500,500)
main_window.mainloop()

# class GUI(object):

#     def __init__(self, main_window):
#         frame = Frame()





# class Hangman(object):
# 	'''
# 	This is a class for running a Hangman game.

# 	Attributes:
# 		total_guesses(int): The total amount of guesses a user can have.
# 		available_word(list): Randomly generates a single word inside a list based on parameters.
		
# 	'''
# 	total_guesses = 4
# 	available_word = random_words().get_random_word(hasDictionaryDef='true', includePartOfSpeech="noun,verb",  minCorpusCount=5, maxCorpusCount=15, minLength=3, maxLength=8)

# 	def __init__(self,chosen_word):
# 		'''
# 		The constructor for Hangman class.

# 		Parameters:
# 			chosen_word(list) = available_word(list)
# 		'''
		
# 		self.chosen_word = chosen_word

# 		self.prompted_user = False

# 		self.correct_guess = False

# 		self.wrong_guesses = 0

# 		self.remaining_guesses = self.total_guesses - self.wrong_guesses

# 		self.list_chosen_word = list(chosen_word)

# 		self.list_of_correct_guesses = []

# 		self.updated_list = self.list_chosen_word.copy()

		

# 	def general_information(self):
# 		print("Welcome to Hangman")
# 		print("Your word is {} characters long".format(len(self.chosen_word)))
# 		print("You will have a total of {} guesses".format(self.total_guesses))

# 	def total_guesses_left(self):
# 		print("You have a total of {} remaining guesses".format(self.remaining_guesses))


# 	def word_display(self):

# 		if self.prompted_user == False:
# 			for i in range(len(self.chosen_word)):
# 				print("_", end =" ")
# 		elif self.prompted_user == True:
# 			if self.correct_guess == True:
# 				self.list_of_correct_guesses.append(self.guess)
# 				print(self.list_chosen_word)
# 				for index, character in enumerate(self.list_chosen_word):
# 					if character in self.list_of_correct_guesses:
# 						self.updated_list[index] = character
# 					else:
# 						self.updated_list[index] = '_'
# 			print(self.updated_list)
# 			print(self.list_of_correct_guesses)



# 	def check_character_guess(self):

# 		# Makes sure input is type str() and length 1
# 		self.guess = input("Enter a letter: ")
# 		self.prompted_user = True
		
# 		# Check if user wants to type in the whole word
# 		if self.guess == "insert":
# 			self.word_guess = input("Please type the word your thinking of: ")
# 			self.check_word_guess()




# 		while (len(self.guess) != 1 or self.guess != 'insert'):
# 			self.guess = input("Incorrect length of an input, Enter a single letter: ")
# 			print(self.guess)
			

# 		# Checks whether guess is correct
# 		if self.guess in self.chosen_word:
# 			self.correct_guess = True
# 		else:
# 			self.correct_guess = False
# 			self.wrong_guesses += 1
# 			print(self.wrong_guesses)

# 	def check_word_guess():
# 		if self.chosen_word == self.word_guess:
# 			self.win_information()
# 		else:
# 			self.wrong_guesses += 1
# 			self.correct_guess = False
# 			print("Sorry your word guess was wrong, try again")
# 			print("If you still wish to insert a word, simply input insert, otherwise you can continue guessing away!")





# 	def win_information(self):
# 		print("Congrats, you just won Hangman!")
# 		exit()



# 	def lose_information(self):
# 		print("Sorry but your out of guesses, maybe next time you'll win")
# 		exit()
		







# 	def hangman_drawing(self):
# 		if self.wrong_guesses >= 0:
# 			print("------|")
		
		


	
# 		if self.wrong_guesses >= 1:
# 			print("      |")



	
# 		if self.wrong_guesses >= 2:
# 			print("      __")
# 			print("     |  |")
# 			print("      --  ")


	
# 		if self.wrong_guesses >= 3:
# 			print("       | ")
# 			print("    ---|--- ")
# 			print("       | ")



	
# 		if self.wrong_guesses >= 4:
# 			print("      --        ")
# 			print("     |  |    ")
# 			print("     |  |    ")
		 

		


	
# # Instatiating the class Hangman by creating an object h
# h = Hangman(Hangman.available_word)
# print(h.chosen_word)


# # Welcome_page
# h.general_information()

# # Print out length of word in "_"
# h.word_display()

# while h.wrong_guesses < 4:

# 	h.check_guess()

# 	h.hangman_drawing()

# 	h.word_display()

# 	h.win_information()

# # Lost game
# h.lose_information()


	









