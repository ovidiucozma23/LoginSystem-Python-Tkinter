#################################################
#	Filename: menu.py
#	Author: Ovidiu
#	Date: 2023-10-19
#################################################
# Include Libs
import tkinter as tk
from tkinter import ttk
import sys
# ========
# Include Other Files
from change_credentials import * 

class MenuBar(tk.Menu):
	def __init__(self, parent, username_id):
		super().__init__(parent)
		self.username_id = username_id

		actions = tk.Menu(self, tearoff = False)
		self.add_cascade(label = "Actions", menu = actions)
		actions.add_command(label = "Change credentials", command = self.change_credentials)
		actions.add_separator()
		actions.add_cascade(label = "Exit", command = self.quit)

	def quit(self):
		sys.exit(0)

	def change_credentials(self):
		app = Credentials(self, self.username_id)
		app.grab_set()