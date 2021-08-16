# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 15:54:25 2021

@author: Al Yalkun
"""


from tkinter import *

class Pong:
    def __init__(self):

        my_window = Tk() # create a window
        my_window.title("Pong Game!")

        my_width = 500
        my_height = 300
        self.my_canvas = Canvas(my_window, bg = 'white', \
                           width = my_width, height = my_height)
        self.my_canvas.pack()

        radius = 20
        x = radius
        y = my_height/2
        self.ball = self.my_canvas.create_oval(x - radius, my_height/2 + \
                              radius, x + radius, my_height/2 - radius,\
                              fill = "red", tags = "disk") 
            
        #x1, x2 , y1 , y2 = self.my_canvas.coords(self.ball)
        
        line_x = 500
        line_top = 75
        line_bot = 150
        paddle_width = 15
        self.my_paddle = self.my_canvas.create_line(line_x, line_top, \
                              line_x, line_bot, \
          width = paddle_width, fill = "blue", tags = "paddle")
        slot_x = 1
        slot_top = 0
        slot_bot = 110
        slot_width = 18
        self.my_slot1 = self.my_canvas.create_line(slot_x, slot_top, \
                              slot_x, slot_bot, \
          width = slot_width, fill = "black", tags = "slot1")
        slot_x = 1
        slot_top1 = 190
        slot_bot1= 300
        slot_width = 18
        self.my_slot2 = self.my_canvas.create_line(slot_x, slot_top1, \
                              slot_x, slot_bot1, \
          width = slot_width, fill = "black", tags = "slot2")
        
        my_window.bind("<Up>" , self.up)
        my_window.bind("<Down>" , self.down)
        dx = 2
        dy = 2
        while True :  # move to new x and update x-position
            self.my_canvas.move("disk", dx, dy) # move disk dx amount            
            self.my_canvas.after(10) # sleep for a few millisecs
            
            # redraw/update the canvas w/ new disk position
            self.my_canvas.update()
            
            x += dx
            if x + radius > line_x or x + radius >= my_width: # hit paddle
                dx = -dx
            elif x - radius <= 1 : # hit left boundary
                dx = -dx
            y += dy
            if y + radius > my_height: # hit bottom
                dy = -dy
            elif y - radius <= 0: # hit top
                dy = -dy
        ''' elif x - radius <= 0 :
                self.my_canvas.delete("disk", "line", "slot", "paddle")
                self.my_canvas.create_text(250, 70, text = "You won!", \
                                   font = "Courier 10", tags = "string")
        ''' 
           
        
        my_window.focus_set()
        my_window.mainloop()
    def up(self, event):
        x = 0
        y = -45
        self.my_canvas.move(self.my_paddle, x , y)
    def down(self, event):
        x = 0
        y = 45
        self.my_canvas.move(self.my_paddle, x , y)   

Pong()
