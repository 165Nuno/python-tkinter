import tkinter as tk

class MyGUI:


    def __init__ (self):

        self.root = tk.Tk()
        self.root.title("TKinter 2.0")

        self.label = tk.Label(self.root,text="165Grinch",font=('Arial',16))
        self.label.pack(padx=10,pady=10)

        self.textbox = tk.Text(self.root,height=5,font=('Arial,16'))
        #self.textbox.bind("<KeyPress>",self.shortcut)
        self.textbox.pack(padx=10,pady=10)

        self.check_state = tk.IntVar()

        self.check = tk.Checkbutton(self.root,text="Show MessageBox",font=('Arial',16))
        self.check.pack(padx=10,pady=10)

        self.button = tk.Button(self.root,text="Shoow Message", font=('Arial',16),command=self.show_message)
        self.button.pack(padx=10,pady=10)

        self.root.protocol("WM_DELETE_WINDOW",self.on_closing)
        self.root.mainloop()

    def show_message(self):
        if self.check_state.get() == 0:
            print(self.textbox.get('1.0',tk.END))
        else:
            messagebox.showinfo(tittle="Message",message="Erro")

    #def shortcut(self,event):
    #   print(event)
    
    def on_closing(self):
        if messagebox.askyesno(title="Fechar Janela?",message="Tem a certeza que pretende fechar a janela?"):
         self.root.destroy()





MyGUI()

