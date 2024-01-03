import tkinter as tk
import time
from tkinter import Tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


root = Tk()
root.withdraw()

notification_windows = []

def show_notification(title, message, duration, bg, fg, font, fade_duration):
    # Récupération des dimensions de l'écran
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # Calcul de la position de la notification en bas à droite de l'écran
    pos_x = screen_width - 200 - 10
    pos_y = screen_height - 100 - 10

    # Création de la fenêtre
    window = tk.Toplevel()
    window.title(title)
    window.geometry("200x100")
    window.resizable(False, False)
    window.overrideredirect(True)
    window.configure(bg=bg)
    window.attributes("-alpha", 0.0)

    # Déplacement de la fenêtre en bas à droite de l'écran
    window.geometry("+{}+{}".format(pos_x, pos_y))

    # Ajout d'un label avec le message de la notification
    label = tk.Label(window, text=message, bg=bg, fg=fg, font=font)
    label.pack(padx=10, pady=10)


    fade_steps = int(fade_duration / 50)

    # Affichage de la notification avec un fondu
    for i in range(fade_steps):
        window.attributes("-alpha", i / fade_steps)
        window.update()
        time.sleep(0.05)

    # Ajout de la fenêtre à la liste des fenêtres affichées
    notification_windows.append(window)

    # Repositionnement de toutes les fenêtres affichées
    for i, w in enumerate(notification_windows):
        w.geometry("+{}+{}".format(pos_x, pos_y - (i + 1) * 100))

    # Fermeture de la fenêtre au bout de la durée spécifiée
    window.after(duration, window.destroy)
    notification_windows.remove(window)

# Exemple d'utilisation de la fonction
show_notification("Notification 1", "Voici une première notification de test.", 5000, "white", "black", "Helvetica 14", 2000)
time.sleep(0.5)
show_notification("Notification 2", "Voici une deuxième notification de test.", 5000, "blue", "pink", "Helvetica 14", 2000)
time.sleep(0.5)
show_notification("Notification 3", "Voici une deuxième notification de test.", 5000, "red", "yellow", "Helvetica 14", 2000)
time.sleep(0.5)
show_notification("Notification 4", "Voici une quatrième notification de test.", 5000, "purple", "orange", "Helvetica 14", 2000)
time.sleep(0.5)
show_notification("Notification 5", "Voici une cinquième notification de test.", 5000, "green", "cyan", "Helvetica 14", 2000)

root = tk.Tk()

frame = tk.Frame(root)
frame.pack()

fig = plt.figure()

ax = fig.add_subplot(111)

# Tableau de données comme exemple
data = [10, 20, 15, 25, 30, 35, 40]
ax.plot(range(1, len(data)+1), data, color='lightblue', linewidth=3)
ax.scatter(range(1, len(data)+1), data, color='darkgreen', marker='^')

# Création du widget
canvas = FigureCanvasTkAgg(fig, master=frame)
canvas.draw()
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

root.mainloop()