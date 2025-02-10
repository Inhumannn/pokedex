import tkinter as tk

class ListeboxCanvas:
    def __init__(self, master, items, width=200, height=300):
        self.canvas = tk.Canvas(master, width=width, height=height)
        self.canvas.pack()

        self.items = items
        self.item_rects = []  # Liste pour stocker les éléments de la "liste"
        self.sub_items_rects = []  # Liste pour stocker les sous-éléments
        self.selected_item = None  # Aucun élément sélectionné au départ
        self.sub_items_visibility = {}  # Dictionnaire pour gérer l'affichage des sous-éléments

        self.draw_items()

    def draw_items(self):
        """Dessine les éléments de la liste sur le canevas."""
        y_position = 10  # Position de départ pour l'affichage des éléments
        for idx, (item, sub_items) in enumerate(self.items):
            # Dessin du rectangle pour l'élément principal
            rect = self.canvas.create_rectangle(10, y_position, 190, y_position + 30, fill="lightgrey", outline="black")
            label = self.canvas.create_text(100, y_position + 15, text=item, anchor="center")
            
            # Ajouter un événement de clic pour chaque élément
            self.canvas.tag_bind(rect, "<Button-1>", lambda event, idx=idx: self.on_item_click(idx))
            self.canvas.tag_bind(label, "<Button-1>", lambda event, idx=idx: self.on_item_click(idx))

            self.item_rects.append((rect, label))
            self.sub_items_visibility[idx] = False  # Par défaut, les sous-éléments sont cachés

            # Dessiner les sous-éléments (ils sont cachés initialement)
            sub_y_position = y_position + 30  # Position initiale des sous-éléments
            sub_item_rects = []
            for sub_item in sub_items:
                sub_rect = self.canvas.create_rectangle(20, sub_y_position, 190, sub_y_position + 30, fill="lightblue", outline="black")
                sub_label = self.canvas.create_text(100, sub_y_position + 15, text=sub_item, anchor="center")
                sub_item_rects.append((sub_rect, sub_label))
                sub_y_position += 40  # Espacer les sous-éléments

            self.sub_items_rects.append(sub_item_rects)
            y_position = sub_y_position  # Déplacer la position de l'élément suivant

    def on_item_click(self, idx):
        """Gère le clic sur un élément."""
        # Alterner l'affichage des sous-éléments
        if self.sub_items_visibility[idx]:
            # Cacher les sous-éléments
            for sub_rect, sub_label in self.sub_items_rects[idx]:
                self.canvas.itemconfig(sub_rect, state="hidden")
                self.canvas.itemconfig(sub_label, state="hidden")
        else:
            # Afficher les sous-éléments
            for sub_rect, sub_label in self.sub_items_rects[idx]:
                self.canvas.itemconfig(sub_rect, state="normal")
                self.canvas.itemconfig(sub_label, state="normal")

        # Inverser la visibilité
        self.sub_items_visibility[idx] = not self.sub_items_visibility[idx]
        print(f"Élément principal sélectionné : {self.items[idx][0]}")

root = tk.Tk()
root.title("Listebox Canvas avec sous-éléments")

# Exemple de données : liste avec des sous-éléments
items = [
    ("Élément 1", ["Sous-élément 1a", "Sous-élément 1b"]),
    ("Élément 2", ["Sous-élément 2a", "Sous-élément 2b"]),
    ("Élément 3", ["Sous-élément 3a", "Sous-élément 3b"]),
    ("Élément 4", ["Sous-élément 4a", "Sous-élément 4b"]),
]

listebox = ListeboxCanvas(root, items)

root.mainloop()
