import tkinter as tk
import tkinter.ttk as ttk
import winsound

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

def beep():
    winsound.MessageBeep()

def select(arg):
    global STARTED, COUNT
    entry['state'] = 'normal'
    STARTED = False
    entry.delete(0, tk.END)
    entry.insert(tk.END, OPTIONS[arg])
    COUNT = 0
    count_label['text'] = "Press Spacebar to start counting..."

def count(arg):
    global STARTED, TARGET, COUNT
    if STARTED:
        COUNT += 1
        count_label['text'] = f"{COUNT}/{TARGET}"
        if COUNT == TARGET:
            beep()
            count_label['text'] = "You have completed! ٱلْحَمْدُ لِلَّٰهِ! Press Spacebar to restart"
            entry['state'] = 'normal'
            STARTED = False
            COUNT = 0        
    else:
        try:
            TARGET = int(entry.get())
            entry['state'] = 'disabled'
            STARTED = True
            count_label['text'] = f"{COUNT}/{TARGET}"
        except ValueError:
            count_label['text'] = "Invalid number"

window = tk.Tk()
window.title("Tasbih")
window.bind("<space>", count)
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
count_label = tk.Label(window, text="Press Spacebar to start counting...")
count_label.grid(column=0, row=3, columnspan=2)

# Gets the requested values of the height and width.
window_width = window.winfo_reqwidth()
window_height = window.winfo_reqheight()
# print("Width", windowWidth, "Height", windowHeight)
 
# Gets both half the screen width/height and window width/height
position_right = int(window.winfo_screenwidth()/2 - window_width/2)
position_down = int(window.winfo_screenheight()/2 - window_height/2)
 
# Positions the window in the center of the page.
window.geometry(f"+{position_right}+{position_down}")

tk.mainloop()