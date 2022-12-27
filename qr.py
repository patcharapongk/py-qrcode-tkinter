import sys
import os
from dotenv import load_dotenv

import tkinter as tk
from tkinter import filedialog

import pyzbar.pyzbar 
from PIL import Image


load_dotenv()
path=os.getenv("path")

def getPath():
    global path    
    path = filedialog.askopenfilename(
        initialdir = os.getenv("initpath"),
        title = "Select file",
        filetypes= (("all files", "*.*"), ("jpg", "*.jpg"), ("png", "*.png")))
    # auto decode after openning
    decode()

def decode():
    updateLabel(path)
    data =  pyzbar.pyzbar.decode(Image.open(path))
    # https://note.nkmk.me/en/python-pyzbar-barcode-qrcode/
    # 11.23 26Dec : Added multiple QR support
    for item in data:
        print(type(item))
        text.insert(tk.END, item.data.decode("utf-8") + "\n")

def clearText():
    text.delete('1.0', tk.END)

def updateLabel(txt): 
    labelText.set(txt)
    root.title("Decode QR :: " + txt)

root = tk.Tk()

btn = tk.Button(root, text="open",command=getPath)
btn2 = tk.Button(root, text="decode", command=decode)
btn3 = tk.Button(root, text="clear", command=clearText)
text = tk.Text(root, height=16, font=('MS Sans Serif', 16))


labelText = tk.StringVar()
filelabel = tk.Label(root, textvariable=labelText)

## For CLI arguments
if len(sys.argv) > 1:
    path = sys.argv[1]
    decode()

# packing
text.grid(column=0, row=0, columnspan=3, sticky='nsew')
btn.grid(column=0, row=1, sticky='nsew', padx=10, pady=10)
btn2.grid(column=1, row=1,sticky='nsew', padx=10, pady=10)
btn3.grid(column=2, row=1,sticky='nsew', padx=10, pady=10)
filelabel.grid(column=0,row=2, columnspan=3)

# main loop
root.mainloop()
