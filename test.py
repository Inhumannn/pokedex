from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
import pickle


class Pokemon:
    def __init__(self, name, type, level):
        self.name = name
        self.type = type
        self.level = level

    def __str__(self):
        return f"{self.name} (Type: {self.type}, Level: {self.level})"

pokemon_list = [
    Pokemon("Pikachu", "Electric", 5),
    Pokemon("Bulbasaur", "Grass", 7),
    Pokemon("Charmander", "Fire", 10)
]

# Sérialisation de la liste de Pokémon
with open('pokemon_list.pkl', 'wb') as f:
    pickle.dump(pokemon_list, f)

# Désérialisation de la liste de Pokémon
with open('pokemon_list.pkl', 'rb') as f:
    loaded_pokemon_list = pickle.load(f)

# Affichage des Pokémon désérialisés
for pokemon in loaded_pokemon_list:
    print(pokemon)
