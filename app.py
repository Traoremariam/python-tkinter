import tkinter as tk
from datetime import datetime

# Création de la fenêtre principale
window = tk.Tk()
window.title("Mon formulaire")

# Création des champs de saisie
label_name = tk.Label(window, text="Nom :")
label_name.pack()
entry_name = tk.Entry(window)
entry_name.pack()

label_prenom = tk.Label(window, text="Prenom :")
label_prenom.pack()
entry_prenom = tk.Entry(window)
entry_prenom.pack()

label_email = tk.Label(window, text="Email :")
label_email.pack()
entry_email = tk.Entry(window)
entry_email.pack()

label_tel = tk.Label(window, text="Telephone :")
label_tel.pack()
entry_tel = tk.Entry(window)
entry_tel.pack()


# Fonction pour sauvegarder les données dans un fichier
def save_data():
    with open("data.txt", "a") as f:
        f.write(f"Nom : {entry_name.get()}\nPrenom : {entry_prenom.get()}\nEmail : {entry_email.get()}\nTel : {entry_tel.get()}\n\n")

    entry_name.delete(0, tk.END)
    entry_prenom.delete(0, tk.END)
    entry_email.delete(0, tk.END)
    entry_tel.delete(0, tk.END)


# Bouton pour sauvegarder les données
button_save = tk.Button(window, text="Enregistrer", command=save_data)
button_save.pack()

# Affichage de la fenêtre
window.mainloop()
