#################################################
#	Filename: class_login.py
#	Author: Ovidiu
#	Date: 2023-10-19
#################################################
# Include Libs
import tkinter as tk 
from tkinter import ttk

class InputLabel(tk.Label):
	def __init__(self, parent, label_name):
		super().__init__(parent,
			text = label_name,
			bd = 0,
			font = ('Calibri', 11, 'bold'),
			background = '#222222',
			foreground = '#dbd9d9',
			anchor = 'w')

class InputEntry(tk.Entry):
	def __init__(self, parent, input_value, show_char):
		super().__init__(parent,
			font = ('Calibri', 11, 'bold'),
			justify = 'center',
			background = '#4a4949',
			bd = 0,
			foreground = '#dbd9d9',
			textvariable = input_value,
			show = show_char)

class Btn(tk.Button):
	def __init__(self, parent, button_name, commander):
		super().__init__(parent,
			text = button_name,
			cursor = 'hand2',
			font = ('Calibri', 10, 'bold'),
			bd = 0,
			background = '#4a4949',
			foreground = '#dbd9d9',
			activebackground = '#dbd9d9',
			activeforeground = '#4a4949',
			command = commander)
