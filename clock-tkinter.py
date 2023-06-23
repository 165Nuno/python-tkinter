import sys
import tkinter as tk
import time

class CLOCK:

    def __init__(self):
        self.root=tk.Tk()
        # Titulo da janela
        self.root.title("Clock")
        # Colocamos o tamanho da janela
        self.root.geometry('500x300')
        self.backg = 'white'
        self.root.configure(bg=self.backg)

        # Criamos a label a dizer Clock
        self.label = tk.Label(self.root,text="CLOCK",font=("Times", "24", "bold italic"),bg=self.backg)
        self.label.pack(padx=20,pady=35)


        # Label que indica as horas
        self.clock = tk.Label(self.root,font=("Times", "50", "bold italic"),bg=self.backg)
        self.clock.pack(pady=1,padx=35)
        self.tempo()


        # Ultima label que indica "Hours    Minutes    Seconds"
        self.nota = tk.Label(self.root,text="Hours     Minutes     Seconds",font=("Times", "15", "bold italic"),bg=self.backg)
        self.nota.pack(pady=1,padx=50)

        # Butão do check
        self.check_state = tk.IntVar()
        self.check = tk.Checkbutton(self.root,text="Change Background",font=("Times", "15", "bold italic"),bg=self.backg,variable=self.check_state,command=self.muda_bg)
        self.check.pack(padx=10,pady=10)

        self.root.mainloop()


    # Função que dá-nos o tempo
    def tempo(self):
        current_time = time.strftime("%H:%M:%S")
        self.clock.config(text=current_time)
        #self.clock.after(200,times)


    # Função que pretendo que mude o background
    def muda_bg(self):
        if self.check_state.get() == 0:
            self.backg='blue'
            print(self.backg)
            print("1")
        else:
            pass

CLOCK()
