import tkinter as tk
from tkinter import messagebox

FICHIER = "tasks.txt"

# ---------- Fonctions ----------
def charger_tasks():
    try:
        with open(FICHIER, "r", encoding="utf-8") as f:
            for ligne in f:
                listbox.insert(tk.END, ligne.strip())
    except FileNotFoundError:
        pass

def sauvegarder_tasks():
    with open(FICHIER, "w", encoding="utf-8") as f:
        for i in range(listbox.size()):
            f.write(listbox.get(i) + "\n")

def ajouter_task():
    task = entry.get()
    if task == "":
        messagebox.showwarning("Attention", "Veuillez entrer une tâche")
    else:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
        sauvegarder_tasks()

def supprimer_task():
    try:
        index = listbox.curselection()[0]
        listbox.delete(index)
        sauvegarder_tasks()
    except:
        messagebox.showwarning("Attention", "Sélectionnez une tâche")

def terminer_task():
    try:
        index = listbox.curselection()[0]
        task = listbox.get(index)
        listbox.delete(index)
        listbox.insert(index, f"✔ {task}")
        sauvegarder_tasks()
    except:
        messagebox.showwarning("Attention", "Sélectionnez une tâche")

# ---------- Fenêtre ----------
fenetre = tk.Tk()
fenetre.title("To-Do List")
fenetre.geometry("400x450")
fenetre.resizable(False, False)

# ---------- Widgets ----------
titre = tk.Label(fenetre, text="📝 To-Do List", font=("Arial", 16))
titre.pack(pady=10)

entry = tk.Entry(fenetre, font=("Arial", 12))
entry.pack(padx=20, fill=tk.X)

btn_ajouter = tk.Button(fenetre, text="Ajouter", command=ajouter_task)
btn_ajouter.pack(pady=5)

listbox = tk.Listbox(fenetre, font=("Arial", 12))
listbox.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)

frame_btn = tk.Frame(fenetre)
frame_btn.pack(pady=10)

btn_terminer = tk.Button(frame_btn, text="Terminé", command=terminer_task)
btn_terminer.grid(row=0, column=0, padx=5)

btn_supprimer = tk.Button(frame_btn, text="Supprimer", command=supprimer_task)
btn_supprimer.grid(row=0, column=1, padx=5)

# Charger les tâches au démarrage
charger_tasks()

fenetre.mainloop()
