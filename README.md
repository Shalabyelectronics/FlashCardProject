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


