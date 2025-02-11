from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
import pickle
# Class Pokemon
class Pokemon:
    def __init__(self, name, types, heal, attack, speed, defence, weakness):
        self.name = name
        self.types = types
        self.heal = heal
        self.attack = attack
        self.speed = speed
        self.defence = defence
        self.weakness = weakness
 # Information
    def afficher_informations(self):
        return self.name, self.types, self.heal, self.attack, self.speed, self.defence, self.weakness
# list_Pokemon
list_pokemon = [
    Pokemon("Bulbizarre", "Plante", 60, 50, 90, 30, "combat"),
    Pokemon("Salamèche", "Feu", 60, 50, 90, 30, "combat"),
    Pokemon("Carapuce", "Eau", 60, 50, 90, 30, "combat"),
    Pokemon("Pikachou", "Electrique", 60, 50, 90, 30, "combat")
]
# Séréalisation
with open("date.pickle","wb") as file:
    pickle.dump(list_pokemon, file)

# Déséralisation
with open("data.pickle","rb") as file:
    objet_deserialise = pickle.load(file)
# Affichage de l'objet
for pokemon in objet_deserialise:
    print(pokemon)

## Principale
root = Tk()
# Titre
root.title("Pokedex")
# Logo
root.tk.call('wm','iconphoto', root._w, PhotoImage(file="img/icon.png"))
# Taille
root.geometry("900x600")
# Frame : pokemon_profile
pokemon_profile = Frame(root, bg="deep sky blue", width=675, height=600, highlightbackground="Black", highlightthickness=7)
# positionnement
pokemon_profile.place(x=0, y=0)
## Droite
# Frame : type_pokemon
type_pokemon = Frame(root, bg="red", width=230, height=600, highlightbackground="Black", highlightthickness=7)
# Positionnement
type_pokemon.place(x=670, y=0)
############################################################################################################################
# Nom pokemon
name_pokemon = Frame(root)
name_pokemon.pack()
# Positionnement
name_pokemon.place(anchor=NE, relx=0.28, rely=0.1)
# Label
label = Label(name_pokemon, text="name_pokemon", font=("Arial", 22), bg="deep sky blue")
label.pack()
# image de base ##210px
img_pokedex_base = Frame(root)
img_pokedex_base.pack()
# Positionnement
img_pokedex_base.place(anchor=NE , relx=0.3, rely=0.2)
# Affichage
img_base = ImageTk.PhotoImage(Image.open("img/base.png"))
# Label
label = Label(img_pokedex_base, image=img_base, borderwidth=0, highlightthickness=0)
label.pack()
# Types
types_pokemon = Frame(root)
types_pokemon.pack()
# Positionnement
types_pokemon.place(anchor=NE, relx=0.5, rely=0.23)
# Label
label = Label(types_pokemon, text="Types : ", font=("Arial", 12), bg="deep sky blue")
label.pack()
# Heal
heal_pokemon = Frame(root)
heal_pokemon.pack()
# Positionnement
heal_pokemon.place(anchor=NE, relx=0.5, rely=0.28)
# Label
label = Label(heal_pokemon, text="Heal : ", font=("Arial", 12), bg="deep sky blue")
label.pack()
# Attack
attack_pokemon = Frame(root)
attack_pokemon.pack()
# Positionnement
attack_pokemon.place(anchor=NE, relx=0.5, rely=0.33)
# Label
label = Label(attack_pokemon, text="Attack : ", font=("Arial", 12), bg="deep sky blue")
label.pack()
# Speed
speed_pokemon = Frame(root)
speed_pokemon.pack()
# Positionnement
speed_pokemon.place(anchor=NE, relx=0.5, rely=0.38)
# Label
label = Label(speed_pokemon, text="Speed : ", font=("Arial", 12), bg="deep sky blue")
label.pack()
# Weak
defence_pokemon = Frame(root)
defence_pokemon.pack()
# Positionnement
defence_pokemon.place(anchor=NE, relx=0.5, rely=0.43)
# Label
label = Label(defence_pokemon, text="Defence : ", font=("Arial", 12), bg="deep sky blue")
label.pack()
# Weak
weak_pokemon = Frame(root)
weak_pokemon.pack()
# Positionnement
weak_pokemon.place(anchor=NE, relx=0.5, rely=0.48)
# Label
label = Label(weak_pokemon, text="Weak : ", font=("Arial", 12), bg="deep sky blue")
label.pack()
############################################################################################################################
# Logo pokemon
place_logo = Frame(root)
place_logo.pack()
# Positionnement
place_logo.place(anchor=NE , relx=0.96, rely=0.05)
# Affichage
logo = ImageTk.PhotoImage(Image.open("img/logo.png"))
# Label
label = Label(place_logo, image=logo, borderwidth=0, highlightthickness=0)
label.pack()
# Positionnnement lb
frame = Frame(root)
frame.place(x=725, y=100)
# Menu déroulant
lb = Listbox(frame, bg="red", borderwidth=0, highlightthickness=0)
lb.pack()
# Element de liste
lb.insert(END, "Bulbizarre")
lb.insert(END, "Salamèche")
lb.insert(END, "Carapuce")
lb.insert(END, "Pikachu")
# Bouton Envoyer
envoyer = Button(root, text="Selectionner", borderwidth=0, bg="red")
envoyer.place(x=755, y=270)
# Styles cbb
style = ttk.Style(root)
style.theme_use('clam')
style.configure("TCombobox", fieldbackground="red", background="red", borderwidth=65)
# Border
# .....
# Combobox
types = ttk.Combobox(root)
types.set("Types ")
types.place(x=720, y=335)
# name
name = Entry(root, bg="Red")
name.insert(0, "Name")
name.place(x=727, y=310)
#
heal = ttk.Combobox(root)
heal.set("Heal")
heal.place(x=720, y=360)
attack = ttk.Combobox(root)
attack.set("Attack")
attack.place(x=720, y=385)
speed = ttk.Combobox(root)
speed.set("Speed")
speed.place(x=720, y=410)
defence = ttk.Combobox(root)
defence.set("Defence")
defence.place(x=720, y=435)
# Weak
weak = Entry(root, bg="Red")
weak.insert(0, "Weak")
weak.place(x=727, y=460)
# Types
types['values'] = ("Normal", "Feu", "Eau", "Plante", "Électrik", "Glace", "Combat", "Poison", "Sol", "Vol", "Psy", "Insecte", "Roche", "Fantôme", "Dragon", "Ténèbres", "Acier", "Fée")
# heal
heal['values'] = (" 50-70", "70-90", "90-120", "120+")
# attack
attack['values'] = ("45-60", "60-80", "80-100", "100-150+")
# speed
speed['values'] = ("50-70", "70-90", "90-120", "120+")
# defence
defence['values'] = ("40-60", "60-80", "80-100", "100+")
# Bouton Enregistrer
enregistrer = Button(root, text="Enregistrer", borderwidth=0, bg="red")
enregistrer.place(x=758, y=485)
# Fin
root.mainloop()