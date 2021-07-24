#Robert Marsh
#May 12, 2021
#App generates Harry Potter name


from tkinter import *
import tkinter as tk
import random
import pygame


def spell(mnames, fnames, lnames, alphabet):
    
    radio = var.get()
    
    entryone = entry0.get()
    entrytwo = entry1.get()

    firstname = ""
    lastname = ""

    if radio == 0:
        for i in range(len(mnames)):
            if entryone[0].lower() == alphabet[i]:
                firstname = mnames[i]
            if entrytwo[0].lower() == alphabet[i]:
                lastname = lnames[i]    
        
                
    elif radio == 1:
        for i in range(len(mnames)):
            if entryone[0].lower() == alphabet[i]:
                firstname = fnames[i]
            if entrytwo[0].lower() == alphabet[i]:
                lastname = lnames[i]
                
    elif radio == 2:
        rand = random.randint(0, 1)
        if rand == 0:
            for i in range(len(mnames)):
                if entryone[0].lower() == alphabet[i]:
                    firstname = mnames[i]
                if entrytwo[0].lower() == alphabet[i]:
                    lastname = lnames[i]
        else:
            for i in range(len(mnames)):
                if entryone[0].lower() == alphabet[i]:
                    firstname = fnames[i]
                if entrytwo[0].lower() == alphabet[i]:
                    lastname = lnames[i]

    label.config(text = firstname + " " + lastname)



    
choices = [("Male", 0),
           ("Female", 1),
           ("Don't Care", 2)]

mnames = ("Draco", "Albus", "Cedric",
          "Remus", "Arthur", "George",
          "Fred", "Oliver", "Neville",
          "Kingsley", "Percival", "Harry",
          "Rubeus", "James", "Seamus",
          "Peter", "Severus", "Draco",
          "Alastor", "Ron", "Percy",
          "Sirius", "Tom", "Gellert",
          "Gilderoy", "Dudley")

fnames = ("Alecto", "Bellatrix", "Cho",
          "Dolores", "Fleur", "Ginny",
          "Griselda", "Helena", "Irma",
          "Lily", "Mafalda", "Millicent",
          "Molly", "Nymphadora","Myrtle",
          "Orla", "Pandora", "Parvati",
          "Rowena", "Wilhelmina", "Hermoine",
          "Helga", "Doris", "Celestina",
          "Bathilda", "Augusta")

lnames = ("Carrow", "Longbottom", "Tonks",
          "Figg", "Dumbledore", "Greengrass",
          "Sinistra", "Bagshot", "Lestrange",
          "Trewlawny", "Burbage", "Umbridge",
          "Delacour", "Weasley", "Ravenclaw",
          "Granger", "Potter", "Lovegood",
          "Dursley", "Bagnold", "McGonagall",
          "Malfoy", "Patil", "Hooch",
          "Hufflepuff", "Gudgeon")
          
alphabet = "abcdefghijklnmopqrstuvwxyz"

pygame.mixer.init()
root = tk.Tk()
root.geometry("600x337")
root.resizable(width = False, height = False)
root.title("Hairy Potter Name Generator")
pygame.mixer.music.load("s.mp3")
pygame.mixer.music.play()

#set background image

image = tk.PhotoImage(file = "./hp.png")
bg_label = tk.Label(root, image = image, bg = "grey").pack()

#top label

top_label = tk.Label(root, text = "Select a gender for name selection",
                     bg = "black", fg = "white", font = ("Comic Sans MS", 12))
top_label.place(relx = .02, rely = .02, relheight = 0.1)

#radio buttons and labels

rad_label = tk.Label(root, text = "Male",
                     bg = "black", fg = "white", font = ("Comic Sans MS", 12))
rad_label.place(relx = .07, rely = .1, relheight = 0.1)

rad1_label = tk.Label(root, text = "Female",
                     bg = "black", fg = "white", font = ("Comic Sans MS", 12))
rad1_label.place(relx = .07, rely = .2, relheight = 0.1)

rad2_label = tk.Label(root, text = "Don't Care",
                     bg = "black", fg = "white", font = ("Comic Sans MS", 12))
rad2_label.place(relx = .07, rely = .3, relheight = 0.1)

var = tk.IntVar()
count = 0
for choice, val in choices:
    tk.Radiobutton(root,
                bg = "black",
                fg = "black",
                activebackground = "black",
                #activeforeground = "black",
                #selectcolor = "black",
                text = "",
                font = ("Comic Sans MS", 12),
                variable = var,
                value = val,
                command = lambda: print(var.get())).place(relx = .02, rely = .1 + count/10 , relheight = 0.1)
    count += 1
    

#name entries and labels

first_label = tk.Label(root, text = "Enter your first name",
                       bg = "black", fg = "white", font = ("Comic Sans MS", 12))
first_label.place(relx = .02, rely = .4, relheight = 0.1)

entry0 = tk.Entry(root, bg = "white")
entry0.place(relx = .02, rely = .5, relheight = 0.07)

last_label = tk.Label(root, text = "Enter your last name",
                      bg = "black", fg = "white", font = ("Comic Sans MS", 12))
last_label.place(relx = .02, rely = .6, relheight = 0.1)

entry1 = tk.Entry(root, bg = "white")
entry1.place(relx = .02, rely = .7, relheight = 0.07)

#spell button

button = tk.Button(root, text = "Lavate los manos",
                   bg = "black", fg = "white", command = lambda: spell(mnames, fnames, lnames, alphabet), font = ("Comic Sans MS", 9))
button.place(relx = .02, rely = .85, relwidth = .20)


#display name

gen_label = tk.Label(root, text = "Your Hairy Potter name is",
                     bg = "black", fg = "white", font = ("Comic Sans MS", 12))
gen_label.place(relx = .25, rely = .75, relheight = 0.1)

label = tk.Label(root, text = "",
                 bg = "black", fg = "white", font = ("Comic Sans MS", 12))
label.place(relx = .25, rely = .85, relheight = 0.1)

root.mainloop()
