from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk

class Pokemon:
    def __init__(self, name, types, heal, attack, speed, defence, weakness):
        self,name = name
        self.types = types
        self.heal = heal
        self.attack = attack
        self.speed = speed
        self.defence = defence
        self.weakness = weakness
    
## Principale
root = Tk()
# Titre
root.title("Pokedex")
# Logo
root.tk.call('wm','iconphoto', root._w, PhotoImage(file="img/icon.png"))
# Taille
root.geometry("900x600")
## Gauche
name = Text(root, height=4, width=50)
name.pack()
text = "#000 Pokemon"
name.insert(END, text)


## Droite
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
lb.insert(END, "blabla")
# Bouton Envoyer
envoyer = Button(root, text="Selectionner", borderwidth=0, bg="red")
envoyer.place(x=764, y=270)
# Styles cbb
style = ttk.Style()
style.theme_use('clam')
style.configure("TCombobox", fieldbackground="red", background="red", borderwidth=0)
# Border
# .....
# Combobox
types = ttk.Combobox(root)
types.set("Types ")
types.place(x=720, y=335)
name = ttk.Combobox(root)
name.set("Name")
name.place(x=720, y=310)
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
weak = ttk.Combobox(root)
weak .set("Weak")
weak.place(x=720, y=460)
# name
name['values'] = ("option 1", "option 2")
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
# weak
weak['values'] = ("option 1", "option 2")
# Bouton Enregistrer
enregistrer = Button(root, text="Enregistrer", borderwidth=0, bg="red")
enregistrer.place(x=764, y=485)
# Fin
root.mainloop()