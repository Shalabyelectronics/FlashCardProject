from tkinter import *
import pandas as pd

# --------------Load and Reset my data file index-----------#

data_file = pd.read_csv("en_ar_data.csv", index_col=0)
data_file.reset_index(drop=True, inplace=True)
index_length = len(data_file)
count_index = 0


# ---------------Increase_Count_Index------------#
def increase_count_index():
    global count_index
    count_index += 1
    next_word(count_index)


# ------------Show Next Word-------------------#
def next_word(index):
    if index_length >= 0:
        en_word = data_file.loc[index, "en"]
        ar_word = data_file.loc[index, "ar"]
        change_canvas_text(en_word)
        window.after(3000, change_canvas_text, ar_word)


# --------------------Change Canvas text----------------------#
def change_canvas_text(word):
    canvas.itemconfig(words_canvas, text=word)


# --------------------Flash Card functions--------------------#
def delete_words():
    global count_index
    data_file.drop(count_index, inplace=True)


# ------------------Yes Function-----------------#
def yes_fun():
    global count_index
    delete_words()
    increase_count_index()
    word_remaining()


# ------------------No Function--------------------#
def no_fun():
    global count_index
    increase_count_index()
    next_word(count_index)
    word_remaining()


# ------------------Save and exit--------------------#
def save_and_exit():
    data_file.to_csv("en_ar_data.csv", columns=["en", "ar"])
    window.destroy()


# --------------------Words_remaining Function--------#
def word_remaining():
    global count_index, index_length
    remaining_words = str(index_length - count_index)
    number_of_words.config(text=remaining_words)


# ---------------------Fonts and Colors---------------#
FONT = "Ubuntu-Medium"
FG_COLOR = "#274472"
BG_COLOR = "#C3E0E5"

# ---------------------Flash Card GUI------------------#
window = Tk()
window.title("Flash Card English Arabic v1.0")
window.config(padx=50, pady=50, bg=BG_COLOR)
# First row content Row =0 , with 0, 1, 2 columns.
'''
The Idea of this part is to show how many remaining words still you need to learn.
I will write (There are ) ( number of words ) (words to learn.)
as There are is a label (column=0,row=0), number of words another label (column=1 ,row=0),
words to learn another label (column=2,row=0)
'''
there_are = Label(text="  There are ", fg=FG_COLOR, bg=BG_COLOR, font=(FONT, 20))
there_are.grid(column=0, row=0, sticky=E)
# ------------------ This part will be refreshed each time user start the app-----#
total_words = str(index_length - count_index)
number_of_words = Label(text=total_words, fg=FG_COLOR, bg=BG_COLOR, font=(FONT, 50))
number_of_words.grid(column=1, row=0)
words_to_learn = Label(text="words to learn.", fg=FG_COLOR, bg=BG_COLOR, font=(FONT, 18))
words_to_learn.grid(column=2, row=0)
# My canvas Start here.
canvas = Canvas(width=500, height=350, bg=BG_COLOR, highlightthicknes=0)
# -----------First Face---------------#
face_card_image = PhotoImage(file="img/ar_word.png")
face_card = canvas.create_image(500, 350, image=face_card_image, anchor=NW)
# I created a flash card image as a frame.
flash_card_frame = PhotoImage(file="img/flashcardfram.png")
canvas.create_image(250, 175, image=flash_card_frame)
# ------------Loop and display Words-----------#
words_canvas = canvas.create_text(250, 175, text=None, fill="red", font=(FONT, 30, "bold"))
canvas.grid(column=0, row=1, columnspan=4)
# ----------Yes Button----------------#
yes_button_image = PhotoImage(file="img/yes.png")
yes_button = Button(image=yes_button_image, highlightthicknes=0, command=yes_fun)
yes_button.grid(column=0, row=2, sticky=W)
# ----------Exit and Save Button-------#
save_exit_image = PhotoImage(file="img/saveandexit.png")
save_exit_button = Button(image=save_exit_image, highlightthicknes=0, command=save_and_exit)
save_exit_button.grid(column=1, row=2, sticky=S)
# ---------No Button------------------#
no_image = PhotoImage(file="img/no.png")
no_button = Button(image=no_image, bg=BG_COLOR, highlightthicknes=0, command=increase_count_index)
no_button.grid(column=2, row=2, sticky=E)
next_word(count_index)
window.mainloop()
