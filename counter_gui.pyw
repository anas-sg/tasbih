import tkinter as tk
import tkinter.ttk as ttk
try:
    import winsound
    def beep():
        winsound.MessageBeep()
except ImportError:
    def beep(): pass

OPTIONS = {
    "Subḥānallāh (سُبْحَانَ ٱللَّٰهِ)": 33,
    "Alḥamdulillāh (ٱلْحَمْدُ لِلَّٰهِ)": 33,
    "Lā ilāha illallāh (لَا إِلَٰهَ إِلَّا ٱللَّٰهُ)": 100,
    "Allāhu akbar (ٱللَّٰهُ أَكْبَرُ)": 34,
    "Astaġfirullāh (أَسْتَغْفِرُ ٱللَّٰهَ)": 100,
    "Ṣalāt al-Fātih (صَلَاةُ الْفَاتِحِ)": 100,
    "custom": ""
}
COUNT = TARGET = 0
STARTED = False

def select(arg):
    global STARTED, COUNT
    entry['state'] = 'normal'
    STARTED = False
    entry.delete(0, tk.END)
    entry.insert(tk.END, OPTIONS[arg])
    COUNT = 0
    count_label['text'] = "Press Spacebar/→ to start counting..."

def count(arg):
    global STARTED, TARGET, COUNT
    if STARTED:
        if arg.keysym in {"space", "Right"}:
            COUNT += 1
        elif arg.keysym == "Left":
            COUNT -= 1
        count_label['text'] = f"←\t{COUNT}/{TARGET}\t→"
        if COUNT == TARGET:
            beep()
            count_label['text'] = "You have completed! ٱلْحَمْدُ لِلَّٰهِ! Press Spacebar/→ to restart"
            entry['state'] = 'normal'
            STARTED = False
            COUNT = 0        
    else:
        try:
            TARGET = int(entry.get())
            entry['state'] = 'disabled'
            STARTED = True
            count_label['text'] = f"←\t{COUNT}/{TARGET}\t→"
        except ValueError:
            count_label['text'] = "Invalid number"

window = tk.Tk()
window.title("Tasbih")
window.bind("<space>", count)
window.bind("<Right>", count)
window.bind("<Left>", count)
window.resizable(0,0)

variable = tk.StringVar(window)
dropdown_label = tk.Label(window, text="Choose recitation:")
dropdown_label.grid(column=0, row=0)
default_recital, default_count = list(OPTIONS.items())[0]
dropdown = ttk.OptionMenu(window, variable, default_recital, *list(OPTIONS), command=select)
dropdown.grid(column=1, row=0)
entry_label = tk.Label(window, text="No. of times:")
entry_label.grid(column=0, row=1)
entry = tk.Entry(window)
entry.grid(column=1, row=1)

entry.insert(0, default_count)
count_label = tk.Label(window, text="Press Spacebar/→ to start counting...")
count_label.grid(column=0, row=3, columnspan=2)

window.update()
offset_x = int(window.winfo_screenwidth()/2 - window.winfo_width()/2)
offset_y = int(window.winfo_screenheight()/2 - window.winfo_height()/2)
window.geometry(f"+{offset_x}+{offset_y}")

tk.mainloop()