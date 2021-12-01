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
        word_remaining()
        change_canvas_text(words_canvas, en_word)
        window.after(3000, change_canvas_text, words_canvas, ar_word)


# --------------------Change Canvas text----------------------#
def change_canvas_text(item, word):
    canvas.itemconfig(item, text=word)


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
    change_canvas_text(number_of_words, remaining_words)


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
# there_are = Label(text="  There are ", fg=FG_COLOR, bg=BG_COLOR, font=(FONT, 20))
# there_are.grid(column=0, row=0, sticky=E)
# words_to_learn = Label(text="words to learn.", fg=FG_COLOR, bg=BG_COLOR, font=(FONT, 18))
# words_to_learn.grid(column=2, row=0)
# My canvas Start here.
canvas = Canvas(width=500, height=500, bg=BG_COLOR, highlightthicknes=0)
# ------------------ This part will be refreshed each time user start the app-----#
bg_word_rectangle= canvas.create_rectangle(40,400,500,90, fill="white", outline="white")
# total_words = str(index_length - count_index)
number_of_words = canvas.create_text(155, 50, text=None, fill=FG_COLOR, font=(FONT, 50))
# -----------First Face---------------#
face_card_image = PhotoImage(file="img/ar_word.png")
face_card = canvas.create_image(500, 350, image=face_card_image, anchor=NW)
# I created a flash card image as a frame.
flash_card_frame = PhotoImage(file="img/flashcardfram.png")
canvas.create_image(250, 250, image=flash_card_frame)
# ------------Loop and display Words-----------#
words_canvas = canvas.create_text(250, 260, text=None, fill="red", font=(FONT, 50, "bold"))
# -------------- Do you know this word?--------#
you_now = canvas.create_text(250, 450, text="Do you know this word?", fill=FG_COLOR, font=(FONT, 20, "bold"))
# --------------Test Remaining words text---------#
remaining_word_text = canvas.create_text(350, 50, text="Words Remaining ", fill="black", font=(FONT, 20, "bold"))
canvas.grid(column=0, row=1, columnspan=4)
# ----------Yes Button----------------#
yes_button_image = PhotoImage(file="img/yes.png")
yes_button = Button(image=yes_button_image, highlightthicknes=0, border="0", command=yes_fun)
yes_button.grid(column=0, row=2, sticky=W)
# ----------Exit and Save Button-------#
save_exit_image = PhotoImage(file="img/saveandexit.png")
save_exit_button = Button(image=save_exit_image, highlightthicknes=0, border="0", command=save_and_exit)
save_exit_button.grid(column=1, row=2, sticky=S)
# ---------No Button------------------#
no_image = PhotoImage(file="img/no.png")
no_button = Button(image=no_image, bg=BG_COLOR, highlightthicknes=0, border="0", command=increase_count_index)
no_button.grid(column=2, row=2, sticky=E)
next_word(count_index)
window.mainloop()
