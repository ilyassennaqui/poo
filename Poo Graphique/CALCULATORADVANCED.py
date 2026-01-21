import tkinter as tk
from tkinter import messagebox

# ---------- App Logic ----------
def calculer():
    try:
        n1 = float(entry_n1.get())
        n2 = float(entry_n2.get())
        result_var.set(str(n1 + n2))
    except ValueError:
        messagebox.showerror("Erreur", "Veuillez entrer des nombres valides")

def nouveau():
    entry_n1.delete(0, tk.END)
    entry_n2.delete(0, tk.END)
    result_var.set("")

def quitter():
    app.destroy()

# ---------- Main Window ----------
app = tk.Tk()
app.title("Simple Calculatrice")
app.geometry("500x500")
app.configure(bg="#0f172a")  # dark navy
app.resizable(False, False)

# ---------- Fonts ----------
TITLE_FONT = ("Segoe UI", 20, "bold")
LABEL_FONT = ("Segoe UI", 11)
ENTRY_FONT = ("Segoe UI", 12)
BTN_FONT = ("Segoe UI", 11, "bold")

# ---------- Title ----------
tk.Label(
    app,
    text="Simple Calculatrice",
    font=TITLE_FONT,
    fg="#38bdf8",
    bg="#0f172a"
).pack(pady=20)

# ---------- Form ----------
frame = tk.Frame(app, bg="#0f172a")
frame.pack(pady=10)

def labeled_entry(text):
    tk.Label(
        frame,
        text=text,
        font=LABEL_FONT,
        fg="#e5e7eb",
        bg="#0f172a"
    ).pack(anchor="w", pady=(10, 4))

    entry = tk.Entry(
        frame,
        font=ENTRY_FONT,
        bg="#020617",
        fg="#f8fafc",
        insertbackground="white",
        relief="flat",
        width=28
    )
    entry.pack(ipady=8)
    return entry

entry_n1 = labeled_entry("Nombre 1")
entry_n2 = labeled_entry("Nombre 2")

tk.Label(
    frame,
    text="Résultat",
    font=LABEL_FONT,
    fg="#e5e7eb",
    bg="#0f172a"
).pack(anchor="w", pady=(10, 4))

result_var = tk.StringVar()
result_entry = tk.Entry(
    frame,
    textvariable=result_var,
    font=ENTRY_FONT,
    bg="#020617",
    fg="#22c55e",
    relief="flat",
    state="readonly",
    width=28
)
result_entry.pack(ipady=8)

# ---------- Buttons ----------
btn_frame = tk.Frame(app, bg="#0f172a")
btn_frame.pack(pady=25)

def modern_button(text, cmd, color):
    return tk.Button(
        btn_frame,
        text=text,
        command=cmd,
        font=BTN_FONT,
        bg=color,
        fg="white",
        activebackground=color,
        relief="flat",
        width=12,
        pady=8
    )

modern_button("Nouveau", nouveau, "#475569").grid(row=0, column=0, padx=8)
modern_button("Calculer", calculer, "#2563eb").grid(row=0, column=1, padx=8)
modern_button("Quitter", quitter, "#dc2626").grid(row=0, column=2, padx=8)

# ---------- Run ----------
app.mainloop()