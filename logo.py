import tkinter.filedialog
import tkinter as tk
from turtle import width


f = tkinter.filedialog.askopenfile("r")
fname = f.name
f.close()

logostr = ""

from PIL import Image
 
# creating a image object
im = Image.open(f.name)
px = im.load()
oldcolor = (0, 0, 0)
color = (0, 0, 0)
logostr += f"setpensize 2000 bk 1000 fd 2000 bk 1000 setpensize 1 pu fd {im.height//2} rt 90 bk {im.width//2} pd\n"
fdcount = 0
for y in range(im.height):
    for x in range(im.width):
        color = px[x, y][0:3]
        if(len(color)==4) and color==(0, 0, 0):
            color=(255,255,255)
        if color != oldcolor:
            oldcolor = color
            logostr += f"color [{color[0]} {color[1]} {color[2]}] "
        logostr += "fd 1\n"
        fdcount += 1
    logostr += f"pu bk {fdcount} rt 90 fd 1 lt 90 pd\n"
    fdcount = 0

root = tk.Tk()

lineedit = tk.Text(root)
lineedit.insert(tk.END, logostr)
lineedit.pack()
root.mainloop()
print(logostr)
# using getpixel method
