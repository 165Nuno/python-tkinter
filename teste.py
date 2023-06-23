import tkinter as tk

window = tk.Tk()
window.title("Paint 2.0")
window.geometry('1000x800')


label = tk.Label(window, text="Hello World!", font=('Arial',18))
#label.pack()
label.pack(padx=20, pady=20)
# Preciso do pack

# Cria-me uma caixa de texto, onde posso escrever
textbox = tk.Text(window,height = 5,font = ('Arial',16))
textbox.pack(padx=10)

#myentry = tk.Entry(window)
#myentry.pack()

window.mainloop()