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
os.path.abspath('classes')
os.path.abspath('database')
# ========
# Include Other Files
from config.global_config import *
from functions.global_functions import *
from classes.menu import *

class Main(tk.Tk):
	def __init__(self, username_id):
		super().__init__()
		self.title(APP_NAME)
		self.minsize(1000, 700)
		self.state('zoomed')
		#self.config(bg = '#222222')
		self.update_idletasks()

		menubar = MenuBar(self, username_id)
		self.config(menu = menubar)

