# Flashcard technique
![](/readme_img/readme_gui.png)
## Introduction:
#### This small application is a Python tkinter library practice as I designed and functioned a flashcard learning technique to learn english from the most frequency list, and I used it [from hermitdave project](https://github.com/hermitdave/FrequencyWords).
#### The project will show the english word firs then after three seconds will show the translated word in arabic so if user know this word will click yes so this particular word will be removed from the data file, else if user do not know about this word will click NO button.
#### Finally, if user want to save his progress and exit will click Save and Exit button.
## How I build this project?
* ### Designing my user interface.
First I struggled on from which area should I start building this application, so I figured out to start with the graphic user interface first.
I used Tk() class to create a window and mainloop method to keep it open then I start adding yes button, no button and save and exit button as well.
Finally, regarding the flash card position where the words supposed to appear I used Canvas class, with flashcard frame and 
updating the remaining numbers of words.
Note: I used Adobe photoshop to design my flashcard frame and the buttons as well.
* ### Get my data file and prepared it.
I used english data file from [hermitdave project](https://github.com/hermitdave/FrequencyWords) and then I used Google sheet to
translate the english word list to arabic by applying `=GOOGLETRANSLATE()` formula.
* ### Read, Reset index and drop rows.
Here we use pandas libraries because it is very useful in this case, so I start with reading and reset index to the data file, but why I'm resetting the data file index?
because when I drop any row later and when saving the data file the index well be different, and that will cause an error later.
and to reset my index I used reset_index method `data_file.reset_index(drop=True, inplace=True)`
I turned the drop parameter to True so when it reset the current index it will not add an old index in secret column, and we add inplace to True to apply my changes.
Also, I got the number of remaining words to learn from `remaining_words = str(index_length - count_index)` as I add it in 
words_remaining function.
* ### Updating the words.
The next step was to update the words on the canvas, so I created show_words function that took index as a parameter.
```buildoutcfg
def show_words(index):
    if index_length >= 0:
        en_word = data_file.loc[index, "en"]
        ar_word = data_file.loc[index, "ar"]
        word_remaining() # Will  update the remaing words number in the program canvas.
        change_canvas_text(words_canvas, en_word)
        window.after(3000, change_canvas_text, words_canvas, ar_word)
```
As we can see we display the english word first then the arabic word and the period of time between them is 3 seconds.
* ### Yes button and drop a row.
Here when the user press Yes button as the user knows the Yes and delete row Function will be triggered.
```buildoutcfg
# ------------------Yes and delete row Function-----------------#
def yes_delete_row():
    global count_index
    data_file.drop(count_index, inplace=True)
    increase_count_index()
    word_remaining()
```
* ### No button and go to next word.
Here when the user click No button as the user do not know this word then No_function will be triggered.
```buildoutcfg
# ------------------No Function--------------------#
def no_fun():
    global count_index
    increase_count_index()
    show_words(count_index)
    word_remaining()
```
Here as we do not know the word so will keep it in our data file to review it later.
* ## Save and Exit.
Here when the user click save and exit button (save and exit function) will be triggered.
```buildoutcfg
# ------------------Save and exit--------------------#
def save_and_exit():
    data_file.to_csv("en_ar_data.csv", columns=["en", "ar"])
    window.destroy()
```
## Updates and Improvements.
I'm working in this project as a practice about using tkinter library and what I noticed is
working on application design side is too important also, so if I'm going to improve this project,
I will focus on GUI and add more options as:
* Translate application to the Arabic language.
* Add show word button instead to wait for 3 seconds between each word.
* Add Next and Previous word button.