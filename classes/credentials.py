#################################################
#	Filename: main_window.py
#	Author: Ovidiu
#	Date: 2023-10-19
#################################################
# Include Libs
import tkinter as tk 
from tkinter import ttk
import os
# ========
# Set Paths
os.path.abspath('functions')
os.path.abspath('config')
# ========
# Include Other Files
from config.global_config import *
from functions.global_functions import *

class TitleInputCredentials(tk.LabelFrame):
	def __init__(self, parent, title_name):
		super().__init__(parent,
			text = '  ' + title_name + '  ')

class LabelInputCredentials(tk.Label):
	def __init__(self, parent, label_name):
		super().__init__(parent,
			text = label_name,
			font = ('Calibri', 10),
			anchor = 'w')

class InputEntryCredentials(tk.Entry):
	def __init__(self, parent, status):
		super().__init__(parent,
			state = status)

class BtnCredentials(tk.Button):
	def __init__(self, parent, button_name, commander, status):
		super().__init__(parent,
			text = button_name,
			cursor = 'hand2',
			bd = 1,
			background = '#bababa',
			relief = 'flat',
			command = commander,
			state = status)