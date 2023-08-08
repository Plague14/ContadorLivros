import tkinter as tk 
from tkinter import *
from tkinter import messagebox, filedialog 
import sys
import os
import time
  
def Widgets(): 
    link_label = Label(root,  
                       text="Link do Livro  :", 
                       bg="#E8D579") 
    link_label.grid(row=1, 
                    column=0, 
                    pady=5, 
                    padx=5) 
   
    root.linkText = Entry(root, 
                          width=55, 
                          textvariable=booklink) 
    root.linkText.grid(row=1,  
                       column=1, 
                       pady=5, 
                       padx=5, 
                       columnspan = 2) 
    
    Download_B = Button(root, 
                        text="Inserir",  
                        command=inserir,  
                        width=20, 
                        bg="#05E8E0") 
    Download_B.grid(row=3, 
                    column=1, 
                    pady=3, 
                    padx=3) 
    
    Download_a = Button(root, 
                        text="Ver Qtnd",  
                        command=contador,  
                        width=20, 
                        bg="#05E8E0") 
    Download_a.grid(row=3, 
                    column=2, 
                    pady=3, 
                    padx=3)
  
def inserir(): 
    link = booklink.get() 
    with open('livros.txt', 'a', encoding='utf-8') as txt:
        texto = txt.writelines(link + "\n")  
    messagebox.showinfo("Sucesso!","Livro incluso com sucesso!")
    time.sleep(1)
    python = sys.executable
    os.execl(python, python, * sys.argv)
   

def contador():
    with open('livros.txt', encoding='utf-8') as txt:
        lines = txt.readlines()
    num = len(lines)
    messagebox.showinfo("Sucesso!","Quantidade de livros lidos: " + str(num))
    
root = tk.Tk() 
   
root.geometry("500x80") 
root.resizable(False, False) 
root.title("Contador de livros lidos em 2022") 
root.config(background="#000000") 
   
booklink = StringVar()  
   
Widgets() 
   
root.mainloop() 