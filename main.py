from tkinter import *
import pandas as pd

# --------------Load and Reset my data file index----------- First Step-------#

data_file = pd.read_csv("en_ar_data.csv", index_col=0)
data_file.reset_index(drop=True, inplace=True)
index_length = len(data_file)
count_index = 0
ar_word_side = None
en_word = None
ar_word = None


# ------------Show Next Word------------------- we call this function in line 125#
def show_words(index):
    global ar_word_side, en_word, ar_word, count_index
    if index_length >= 0:
        try:
            en_word = data_file.loc[index, "en"]
            ar_word = data_file.loc[index, "ar"]
        except KeyError:
            count_index += 1
            show_words(count_index)
        else:
            word_remaining()
            change_canvas_text(words_canvas, en_word)
            ar_word_side = window.after(3000, change_canvas_text, words_canvas, ar_word)


# ----------------Show word-----------------------#
def show_next_word():
    global ar_word_side, ar_word
    window.after_cancel(ar_word_side)
    change_canvas_text(words_canvas, ar_word)


# -------------Show previous word---------------#
def show_previous_word():
    global count_index, en_word, ar_word, ar_word_side
    window.after_cancel(ar_word_side)
    if 0 <= count_index and index_length >= 0:
        count_index -= 1
        try:
            en_word = data_file.loc[count_index, "en"]
            ar_word = data_file.loc[count_index, "ar"]
        except KeyError:
            show_previous_word()
        else:
            word_remaining()
            show_words(count_index)


# ---------------Show_next pair without waiting in same time--------#
def show_both_word():
    global count_index
    window.after_cancel(ar_word_side)
    en_and_ar = f"{en_word} : {ar_word}"
    change_canvas_text(words_canvas, en_and_ar)


# ---------------Increase_Count_Index------------#
def increase_count_index():
    global count_index
    count_index += 1
    show_words(count_index)


# --------------------Change Canvas text----------------------#
def change_canvas_text(item, word):
    canvas.itemconfig(item, text=word)


# ----------------Change words background---------------------#
def change_word_bg():
    canvas.itemconfig(bg_word_rectangle, fill="black")


# ------------------Yes and delete row Function-----------------#
def yes_delete_row():
    global count_index
    window.after_cancel(ar_word_side)
    data_file.drop(count_index, inplace=True)
    increase_count_index()
    word_remaining()


# ------------------No Function--------------------#
def no_fun():
    global count_index
    window.after_cancel(ar_word_side)
    increase_count_index()
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
FONT = "Coiny"
WORDS_COLOR = "darkorange"
FG_COLOR = "#274472"
BG_COLOR = "#8FDDE7"

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
# bg_word_rectangle = canvas.create_rectangle(40, 400, 500, 90, fill="white", outline="white")
# total_words = str(index_length - count_index)
number_of_words = canvas.create_text(260, 30, text=None, fill="lightseagreen", font=(FONT, 50))
# -----------First Face---------------#
# face_card_image = PhotoImage(file="img/ar_word.png")
# face_card = canvas.create_image(500, 350, image=face_card_image, anchor=NW)
# I created a flash card image as a frame.
flash_card_frame = PhotoImage(file="img/flashcardfram.png")
canvas.create_image(250, 290, image=flash_card_frame)
# ------------Loop and display Words-----------#
words_canvas = canvas.create_text(250, 290, text=None, fill=WORDS_COLOR, font=(FONT, 30, "bold"))
# -------------- Do you know this word?--------#
you_now = canvas.create_text(250, 350, text="Do you know this word?", fill=FG_COLOR, font=(FONT, 20, "bold"))
# --------------Test Remaining words text---------#
remaining_word_text = canvas.create_text(260, 80, text="Words Remaining ", fill="navajowhite", font=(FONT, 20, "bold"))
# -----------Show next word without waiting----------------#
show_word_image = PhotoImage(file="img/show_word_direct.png")
show_word_button = Button(text="test", border=0, highlightthicknes=0, activebackground=BG_COLOR, bg=BG_COLOR,
                          image=show_word_image,
                          command=show_both_word).grid(column=3, row=3, sticky=E)
# ----------Yes Button----------------#
yes_button_image = PhotoImage(file="img/yes.png")
yes_button = Button(image=yes_button_image, activebackground=BG_COLOR, bg=BG_COLOR, highlightthicknes=0, border="0",
                    command=yes_delete_row)
yes_button.grid(column=0, row=2)
# ----------Exit and Save Button-------#
save_exit_image = PhotoImage(file="img/saveandexit.png")
save_exit_button = Button(image=save_exit_image, width=250, activebackground=BG_COLOR, bg=BG_COLOR, highlightthicknes=0,
                          border="0", command=save_and_exit)
save_exit_button.grid(column=1, row=3, columnspan=2)
# ---------No Button------------------#
no_image = PhotoImage(file="img/no.png")
no_button = Button(image=no_image, bg=BG_COLOR, activebackground=BG_COLOR, highlightthicknes=0, border="0",
                   command=no_fun)
no_button.grid(column=3, row=2)
# ------------back button--------------#
previous_b_img = PhotoImage(file="img/previous_b.png")
previous_b = Button(image=previous_b_img, bg=BG_COLOR, activebackground=BG_COLOR, highlightthicknes=0, border="0",
                    command=show_previous_word).grid(column=0, row=3, sticky=W)
# ---------------- Canvas grid-----------------#
canvas.grid(column=0, row=1, columnspan=4)
# ---------------Call show words function--------#
show_words(count_index)
window.mainloop()
