#Jesus Romero
#MCS 260 Spring 2022 Project 3
#I hereby attest that I have adhered to the rules for projects as well as UIC’s Academic Integrity standards while completing this project.
import tkinter
import tkinter.ttk
from tkinter import messagebox
import re

pg = tkinter.Tk()
pg.geometry("1200x300")
pg.title("Wordle Help!")
entry_1 = tkinter.StringVar()
entry_2 = tkinter.StringVar()
entry_3 = tkinter.StringVar()
entry_4 = tkinter.StringVar()
entry_5 = tkinter.StringVar()
entry_6 = tkinter.StringVar()
entry_7 = tkinter.StringVar()
entry_8 = tkinter.StringVar()
entry_9 = tkinter.StringVar()
entry_10 = tkinter.StringVar()

"""Up to here in the code, I have imported all the modules that I use in the code. I also created the tkinter gui. I have also set the string entries for each entry box to its respective variable name. For example, the string entered in entry box 1 will be saved as the variale entry_1."""

lbl = tkinter.ttk.Label(pg,text="Enter letters in their respective spot. Otherwise, leave the spots blank",font=('Comic Sans MS',15,'bold italic')).grid(row=1,column=3)
entry1 = tkinter.ttk.Entry(pg,textvariable=entry_1,font=('Comic Sans MS',12,'bold italic'),width=5).grid(row=2,column=1,padx=10,pady=10)
entry2 = tkinter.ttk.Entry(pg,textvariable=entry_2,font=('Comic Sans MS',12,'bold italic'),width=5).grid(row=2,column=2,padx=10,pady=10)
entry3 = tkinter.ttk.Entry(pg,textvariable=entry_3,font=('Comic Sans MS',12,'bold italic'),width=5).grid(row=2,column=3,padx=10,pady=10)
entry4 = tkinter.ttk.Entry(pg,textvariable=entry_4,font=('Comic Sans MS',12,'bold italic'),width=5).grid(row=2,column=4,padx=10,pady=10)
entry5 = tkinter.ttk.Entry(pg,textvariable=entry_5,font=('Comic Sans MS',12,'bold italic'),width=5).grid(row=2,column=5,padx=10,pady=10)

lbl2 = tkinter.ttk.Label(pg,text="Enter letters you know belong in the word, but are unsure of its place in the word",font=('Comic Sans MS',15,'bold italic')).grid(row=3,column=3)
entry6 = tkinter.ttk.Entry(pg,textvariable=entry_6,font=('Comic Sans MS',12,'bold italic'),width=5).grid(row=4,column=1,padx=10,pady=10)
entry7 = tkinter.ttk.Entry(pg,textvariable=entry_7,font=('Comic Sans MS',12,'bold italic'),width=5).grid(row=4,column=2,padx=10,pady=10)
entry8 = tkinter.ttk.Entry(pg,textvariable=entry_8,font=('Comic Sans MS',12,'bold italic'),width=5).grid(row=4,column=3,padx=10,pady=10)
entry9 = tkinter.ttk.Entry(pg,textvariable=entry_9,font=('Comic Sans MS',12,'bold italic'),width=5).grid(row=4,column=4,padx=10,pady=10)
entry10 = tkinter.ttk.Entry(pg,textvariable=entry_10,font=('Comic Sans MS',12,'bold italic'),width=5).grid(row=4,column=5,padx=10,pady=10)

"""Up to here, I have created all the labels and entry boxes for the GUI. I have customized the size of the entry boxes and changed the text font and size."""

def function():
    global ExactLettersWord
    ExactLettersWord = ""
    global ContainsLettersWord
    ContainsLettersWord = ""
    Entry1 = entry_1.get()
    Entry2 = entry_2.get()
    Entry3 = entry_3.get()
    Entry4 = entry_4.get()
    Entry5 = entry_5.get()
    Entry6 = entry_6.get()
    Entry7 = entry_7.get()
    Entry8 = entry_8.get()
    Entry9 = entry_9.get()
    Entry10 = entry_10.get()

    """I have created a function named function() that will be called whenever the button in the GUI is clicked. I have created variables for the respective strings in the entry boxes so I could use later on. I also created two variables ExactLettersWord and ContainsLettersWord."""

    #print("Button has been clicked")

    if len(entry_1.get())==0:
        print("this empty")
        Entry1 = "_"
    elif len(entry_1.get())>1:
        messagebox.showerror("Error","Error: There is more than one letter in box 1")
    elif Entry1.isalpha()!=True:
        print("this is not a letter")
        messagebox.showerror("Error","Error: Entry in box 1 is not a letter")
        sys.exit()

    if len(entry_2.get())==0:
        Entry2 = "_"
    elif len(entry_2.get())>1:
        messagebox.showerror("Error","Error: There is more than one letter in box 2")
    elif Entry2.isalpha()!=True:
        print("this is not a letter")
        messagebox.showerror("Error","Error: Entry in box 2 is not a letter")

    if len(entry_3.get())==0:
        Entry3 = "_"
    elif len(entry_3.get())>1:
        messagebox.showerror("Error","Error: There is more than one letter in box 3")
    elif Entry3.isalpha()!=True:
        print("this is not a letter")
        messagebox.showerror("Error","Error: Entry in box 3 is not a letter")

    if len(entry_4.get())==0:
        Entry4 = "_"
    elif len(entry_4.get())>1:
        messagebox.showerror("Error","Error: There is more than one letter in box 4")
    elif Entry4.isalpha()!=True:
        print("this is not a letter")
        messagebox.showerror("Error","Error: Entry in box 4 is not a letter")

    if len(entry_5.get())==0:
        Entry5 = "_"
    elif len(entry_5.get())>1:
        messagebox.showerror("Error","Error: There is more than one letter in box 5")
    elif Entry5.isalpha()!=True:
        print("this is not a letter")
        messagebox.showerror("Error","Error: Entry in box 5 is not a letter")

    if len(entry_6.get())==0:
        Entry6 = "_"
    elif len(entry_6.get())>1:
        messagebox.showerror("Error","Error: There is more than one letter in box 6")
    elif Entry6.isalpha()!=True:
        print("this is not a letter")
        messagebox.showerror("Error","Error: Entry in box 6 is not a letter")

    if len(entry_7.get())==0:
        Entry7 = "_"
    elif len(entry_7.get())>1:
        messagebox.showerror("Error","Error: There is more than one letter in box 7")
    elif Entry7.isalpha()!=True:
        print("this is not a letter")
        messagebox.showerror("Error","Error: Entry in box 7 is not a letter")

    if len(entry_8.get())==0:
        Entry8 = "_"
    elif len(entry_8.get())>1:
        messagebox.showerror("Error","Error: There is more than one letter in box 8")
    elif Entry8.isalpha()!=True:
        print("this is not a letter")
        messagebox.showerror("Error","Error: Entry in box 8 is not a letter")

    if len(entry_9.get())==0:
        Entry9 = "_"
    elif len(entry_9.get())>1:
        messagebox.showerror("Error","Error: There is more than one letter in box 9")
    elif Entry9.isalpha()!=True:
        print("this is not a letter")
        messagebox.showerror("Error","Error: Entry in box 9 is not a letter")

    if len(entry_10.get())==0:
        Entry10 = "_"
    elif len(entry_10.get())>1:
        messagebox.showerror("Error","Error: There is more than one letter in box 10")
    elif Entry10.isalpha()!=True:
        print("this is not a letter")
        messagebox.showerror("Error","Error: Entry in box 10 is not a letter")

"""Up to here in my code, I have created if and elif statements for each of the Entry boxes. It may not have been the most efficient way of doing it but it definetly works. If the number of characters in the box is 0, it would set the variable for that entry box to an underscore. If the lengeth of the entry box was more than 1, it would provide an error message telling you that there is more than one letter in the box. Lastly, the last elif statement would check if all the characters in the entry box were alphabetic characters, if not it would provide an error message saying whatever was entered in the box isnt a letter."""

    ExactLettersWord = ExactLettersWord+Entry1+Entry2+Entry3+Entry4+Entry5
    ContainsLettersWord = ContainsLettersWord+Entry6+Entry7+Entry8+Entry9+Entry10

    """Here, I stuck all the strings in the entry boxes together in order to use the words in the exactletters function and containsletters function"""

    ExactLetters()
    #print(ContainsLettersWord)
    ContainsLetters()
    InBoth()

B = tkinter.Button(pg,text="Find Me Some Words!",command=function).grid(row=6,column=1)

"""-------------------------------------------------"""
File = open("AllWords.txt","r")
File2 = open("AllWordsLines.txt","w")
L = re.split(",",File.read())
for l in L:
    l = l +"\n"
    l = l.replace('"','')
    l = l.replace("[",'')
    l = l.replace("]",'')
    File2.write(l)
File.close()
File2.close()

"""Here, I have written all the words in the text file provided into a new text file name AllWordsLines. In that file, I have removed all commas, brackets, and quotation marks and set each word into its own line. Meaning there was one word per line in the file."""

file = open("AllWordsLines.txt","r")

def ExactLetters():
    global listofmatch
    listofmatch = []
    S = ExactLettersWord
    #print(S)
    x = ""
    for i in S:
        if i == "_":
            x = x+"[a-zA-Z]"
        else:
            x = x+i
    for line in file:
        listofmatch.append(re.findall(x,file.read()))
    #print(listofmatch)

"""In the exactletters function, I have replaced any underscores (meaning empty entry boxes) with a 'wild card'. The [a-zA-Z] replacing each underscore allows the finall function to search for any letter from a-z and A-Z."""

"""--------------------------------------------------------------"""
matchingChar = []
counter = []
def ContainsLetters():
    file = open("AllWordsLines.txt","r")
    S = ContainsLettersWord
    counter = []
    for line in file:
        for i in S:
            if i in line:
                counter.append(int(1))
        if len(S)==len(counter):
                matchingChar.append(line.rstrip())
                counter = []
        else:
            counter = []
    #print(matchingChar)
"""Up to here, I have created a function named ContainsLetters that makes a list of all the words in the text file that include all the letters provided by the user. I did this using a counter where it goes up with every match in the word. And if the len of the counter is equal to the len of the words given by the user, then it is considered a match. The counter is reset by the end of each word."""

"""----------------------------------------------------------------------"""
def InBoth():
    listofWordInBoth = ""
    listofWordInBoth = [i for i in listofmatch if i in matchingChar]
    print(listofWordInBoth)
    tkinter.messagebox.showinfo("Words",listofWordInBoth)

"""Lastly, I have created a function InBoth where using list comprehsion, the items in one list are compared to the items in the other list (the list of the exact matches is compared with the list of the matches containing the same letters). The new list is printed and showm in an info box."""




pg.mainloop()
