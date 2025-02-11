from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
import pickle

# Class Pokemon
class Pokemon:
    def __init__(self, name, types, heal, attack, speed, defence, weakness, image):
        self.name = name
        self.types = types
        self.heal = heal
        self.attack = attack
        self.speed = speed
        self.defence = defence
        self.weakness = weakness
        self.image = image

    # Affichage lisible pour le print
    def __str__(self):
        return f"Nom : {self.name}\nType : {self.types}\nHeal : {self.heal}\nAttack : {self.attack}\nSpeed : {self.speed}\nDefence : {self.defence}\nWeakness : {self.weakness}"
    # Rajouter un history

# List of Pokemon
list_pokemon = [
    Pokemon("Bulbizarre", "Plante", 45, 49, 45, 49, "Feu", "img/carapuce.png"),
    Pokemon("Salamèche", "Feu", 39, 52, 65, 50, "Eau", "img/carapuce.png"),
    Pokemon("Carapuce", "Eau", 44, 48, 43, 65, "Electrique", "img/carapuce.png"),
    Pokemon("Pikachu", "Electrique", 60, 50, 90, 30, "combat", "img/pichachu.png")
]

# Sérialisation
with open("data.pickle", "wb") as file:
    pickle.dump(list_pokemon, file)

# Désérialisation avec gestion d'erreur
try:
    with open("data.pickle", "rb") as file:
        objet_deserialise = pickle.load(file)
except FileNotFoundError:
    print("Fichier non trouvé. Assurez-vous que la sérialisation a été effectuée.")
    objet_deserialise = []  # Pour plus tard

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
pokemon_profile = Frame(root, bg="deep sky blue", width=675, height=600, highlightbackground="Black", highlightthickness=7)
# positionnement
pokemon_profile.place(x=0, y=0)
## Droite
# Frame : type_pokemon
type_pokemon = Frame(root, bg="red", width=230, height=600, highlightbackground="Black", highlightthickness=7)
# Positionnement
type_pokemon.place(x=670, y=0)

############################################################################################################################
# image de base ##210px
img_pokedex_base = Frame(root)
img_pokedex_base.pack()
# Positionnement
img_pokedex_base.place(anchor=NE , relx=0.3, rely=0.2)
# Affichage
img_base = ImageTk.PhotoImage(Image.open("img/base.png"))
# Label
label_img = Label(img_pokedex_base, image=img_base, borderwidth=0, highlightthickness=0)
label_img.pack()

# Types
types_pokemon = Frame(root)
types_pokemon.pack()
# Positionnement
types_pokemon.place(anchor=NE, relx=0.5, rely=0.23)
# Label pour afficher les informations
label = Label(root, text="", font=("Arial", 12), bg="deep sky blue", width=30, height=10, anchor="nw", justify="left")
label.place(x=300, y=160)
############################################################################################################################
# Logo pokemon
place_logo = Frame(root)
place_logo.pack()
# Positionnement
place_logo.place(anchor=NE , relx=0.96, rely=0.05)
# Affichage
logo = ImageTk.PhotoImage(Image.open("img/logo.png"))
# Label
label_logo = Label(place_logo, image=logo, borderwidth=0, highlightthickness=0)
label_logo.pack()

# Positionnement lb
frame = Frame(root)
frame.place(x=725, y=100)

# Menu déroulant (Listbox)
lb = Listbox(frame, bg="red", borderwidth=1, highlightthickness=2)
lb.pack()
# Element de liste
for pokemon in objet_deserialise:
    lb.insert(END, pokemon.name)

# Fonction pour afficher les détails du Pokémon sélectionné
def afficher_details(event):
    selected_index = lb.curselection()
    if selected_index:
        # On récupère l'index de l'élément sélectionné
        pokemon = objet_deserialise[selected_index[0]]
        label.config(text=pokemon)  # On met à jour le label avec les infos du Pokémon

# Bind l'événement de sélection
lb.bind('<<ListboxSelect>>', afficher_details)

# Styles cbb
style = ttk.Style(root)
style.theme_use('clam')
style.configure("TCombobox", fieldbackground="red", background="red")

# Combobox pour les types et autres
types = ttk.Combobox(root)
types.set("Types ")
types.place(x=720, y=295)

name = Entry(root, bg="Red")
name.insert(0, "Name")
name.place(x=725, y=270)

heal = ttk.Combobox(root)
heal.set("Heal")
heal.place(x=720, y=320)

attack = ttk.Combobox(root)
attack.set("Attack")
attack.place(x=720, y=345)

speed = ttk.Combobox(root)
speed.set("Speed")
speed.place(x=720, y=370)


defence = ttk.Combobox(root)
defence.set("Defence")
defence.place(x=720, y=395)

# Weakness
weak = Entry(root, bg="Red")
weak.insert(0, "Weak")
weak.place(x=727, y=420)

# Liste des types
types['values'] = ("Normal", "Feu", "Eau", "Plante", "Électrik", "Glace", "Combat", "Poison", "Sol", "Vol", "Psy", "Insecte", "Roche", "Fantôme", "Dragon", "Ténèbres", "Acier", "Fée")
heal['values'] = ("50-70", "70-90", "90-120", "120+")
attack['values'] = ("45-60", "60-80", "80-100", "100-150+")
speed['values'] = ("50-70", "70-90", "90-120", "120+")
defence['values'] = ("40-60", "60-80", "80-100", "100+")

# Bouton Enregistrer
enregistrer = Button(root, text="Enregistrer", bg="red", borderwidth=1, highlightthickness=2)
enregistrer.place(x=758, y=485)

# Fin
root.mainloop()
