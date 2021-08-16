# -*- coding: utf-8 -*-
"""
Created on Mon Apr 12 19:11:45 2021

@author: moonl
"""

from tkinter import *
    
class RestruantTipCalculator:
    def __init__(self):
        my_window = Tk()
        self.bill_obj = StringVar()
        self.tips_obj = StringVar()
       
        my_window.title = "Tip Calculator"
        
        Label(my_window, text = "Bill").grid( row = 1, column = 1, sticky = W)
        self.bill_entry = Entry(my_window, textvariable = self.bill_obj,\
                                justify = RIGHT)
        self.bill_entry.grid(row = 1, column = 2)
        self.bill_entry.focus()
        
        Label(my_window, text = "Tip Amount").grid( row = 4, column = 1, \
                                                       sticky = W)
        Label(my_window, text = "Tottal Amount").grid( row = 5, column = 1, \
                                                       sticky = W)
             
        Label(my_window, text = "Tip Amount" , textvariable = self.tips_obj) \
            .grid( row = 4, column = 2,sticky = E)
            
        self.t_amount_obj = StringVar()  
        Label(my_window, text ="Tottal Amount", textvariable=self.t_amount_obj) \
        .grid( row = 5, column = 2,sticky = E)
            
        self.tip_button = IntVar()    
        t_button = Radiobutton(my_window , text = "10%" ,\
                                 variable = self.tip_button , value = 1 ,\
                                     command = self.tip_value ) 
        f_button = Radiobutton(my_window , text = "15%" ,\
                                 variable = self.tip_button , value = 2 ,\
                                     command = self.tip_value )
        e_button = Radiobutton(my_window , text = "18%" ,\
                                 variable = self.tip_button , value = 3 ,\
                                     command = self.tip_value )
        tw_button = Radiobutton(my_window , text = "20%",\
                                 variable = self.tip_button , value = 4 ,\
                                     command = self.tip_value )
            
        t_button.grid( row = 2 , column = 1 )
        f_button.grid( row = 2 , column = 2 )
        e_button.grid( row = 3 , column = 1 )
        tw_button.grid( row = 3 , column = 2 )
        
        my_window.mainloop()
    def tip_value(self):
        button_value = self.tip_button.get()
       
        if button_value == 1 :
            tips_obj = float(self.bill_entry.get()) * 0.1
        elif button_value == 2 :
            tips_obj = float(self.bill_entry.get()) * 0.15
        elif button_value == 3 :
            tips_obj = float(self.bill_entry.get()) * 0.18
        elif button_value == 4: 
            tips_obj = float(self.bill_entry.get()) * 0.2
            
        get_bill = float(self.bill_entry.get())
        totall_tip = tips_obj
        totall_bill = get_bill + totall_tip
        
        #putting results back to tip value and totall amount value
        self.tips_obj.set(totall_tip)   
        self.t_amount_obj.set(totall_bill)
        
    
    


RestruantTipCalculator() 