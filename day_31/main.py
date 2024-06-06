BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import pandas
import random
current_card = {}
to_learn = {}


# -------------------------- PANDAS ----------------------- #
try:
  df = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
  original_data = pandas.read_csv("data/french_words.csv")
  to_learn = original_data.to_dict(orient = "records")
else:
  # Creating a dictionary from the dataframe
  to_learn = df.to_dict(orient = "records")


# print(to_learn)

# Function to get random keys from the dictionary
def next_card():
  global current_card, flip_timer
  window.after_cancel(flip_timer)
  current_card = random.choice(to_learn)
  canvas.itemconfig(card_title, text = "French", fill = "black")
  canvas.itemconfig(card_word, text = current_card["French"], fill = "black")
  canvas.itemconfig(card_background, image = card_front_img)
  flip_timer = window.after(3000, func=flip_card)

# ------------------------ CARD FLIP ----------------------- #
def flip_card():

  canvas.itemconfig(card_title, text = "English", fill = "white")
  canvas.itemconfig(card_word, text = current_card["English"], fill = "white")
  canvas.itemconfig(card_background, image = card_back_img)


# ------------------------ KNOWN CARD FUNCTION ------------------- #
def is_known():
  to_learn.remove(current_card)
  data = pandas.DataFrame(to_learn)
  data.to_csv("data/words_to_learn.csv", index = False)
  next_card()




# --------------------------- UI SETUP -------------------- #
window = Tk()

window.title("Flash Card Program")
window.config(padx = 50, pady = 50, bg = BACKGROUND_COLOR)
# Flipping the card after 3 seconds
flip_timer = window.after(3000,func=flip_card)

canvas = Canvas(width = 800, height = 526)
card_front_img = PhotoImage(file = "images/card_front.png")
card_back_img = PhotoImage(file = "images/card_back.png")
card_background = canvas_image = canvas.create_image(400, 263, image = card_front_img)
canvas.config(bg = BACKGROUND_COLOR, highlightthickness=0)
card_title = canvas.create_text(400, 150, text = "", font=("Aerial", 40, "italic"))
card_word = canvas.create_text(400, 263, text = "", fill = "black", font = ("Ariel", 60, "bold"))
cross_button_image = PhotoImage(file = "images/wrong.png")
cross_button = Button(image = cross_button_image, highlightthickness=0, command = next_card)
tick_button_image = PhotoImage(file = "images/right.png")
tick_button = Button(image = tick_button_image, highlightthickness=0, command = is_known)
canvas.grid(row = 0, column = 0, columnspan=2)
cross_button.grid(row = 1, column = 0)
tick_button.grid(row = 1, column = 1)

next_card()




window.mainloop()

