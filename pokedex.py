from tkinter import *
from tkinter import Tk, Canvas
from random import randrange


class Pokemon:
    def __init__(self, type, evolution, heal, attack, speed, defence, weakness):
        self.type = type
        self.evolution = evolution
        self.heal = heal
        self.attack = attack
        self.speed = speed
        self.defence = defence
        self.weakness = weakness
    
# geometryW = 800
# geometryh = 600
# root = Tk()
# root.title("Pokedex")
# pokedex = Canvas(root, width=geometryW, height=geometryh, bg="black") 
# pokedex.create_rectangle(555,595,10,10, fill="deep sky blue", width=0) # Changer de color selon le type de pokemon
# pokedex.create_rectangle(790,595,565,10, fill="red", width=0)
# logo = PhotoImage(file="img/logo.png")
# pokedex.create_image(600, 20, image=logo, anchor=NW)
# pokedex.create_text(600, 100, text="Hello word !")

# pokedex.pack()
# root.mainloop()

root = Tk()
root.title("Pokedex")
root.geometry("800x600")
pokemon_profile = Frame(root, bg="red", width=0, height=595)
type_pokemon = Frame(root)

pokemon_profile.pack()
type_pokemon.pack()
root.mainloop()
