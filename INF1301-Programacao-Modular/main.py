from tkinter import *
from view import draw_canvas
from model import game_rules

W = 600  # x
H = 600  # y

top = Tk()
cnv = Canvas(top, bg="white", height=H, width=W)
top.title("LUDO")

game_rules.novo_jogo()
draw_canvas.desenha_1a_vez(cnv, top)

cnv.pack()
top.mainloop()
