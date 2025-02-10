from tkinter import *
from PIL import ImageTk, Image

class Pokemon:
    def __init__(self, type, evolution, heal, attack, speed, defence, weakness):
        self.type = type
        self.evolution = evolution
        self.heal = heal
        self.attack = attack
        self.speed = speed
        self.defence = defence
        self.weakness = weakness
    
root = Tk()
# Titre
root.title("Pokedex")
# Taille
root.geometry("900x600")
# Frame : pokemon_profile
pokemon_profile = Frame(root, bg="deep sky blue", width=675, height=600, highlightbackground="Black", highlightthickness=7)
# positionnement
pokemon_profile.place(x=0, y=0)
# Frame : type_pokemon
type_pokemon = Frame(root, bg="red", width=230, height=600, highlightbackground="Black", highlightthickness=7)
# Positionnement
type_pokemon.place(x=670, y=0)
# Logo pokemon
place_logo = Frame(root)
place_logo.pack()
place_logo.place(anchor=NE , relx=0.96, rely=0.05)

logo = ImageTk.PhotoImage(Image.open("img/logo.png"))
label = Label(place_logo, image=logo)
label.pack()
root.mainloop()