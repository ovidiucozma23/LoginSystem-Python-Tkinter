#################################################
#	Filename: login.py
#	Author: Ovidiu
#	Date: 2023-10-19
#################################################
# Include Libs
import tkinter as tk 
from tkinter import ttk
import os
from tkinter import messagebox as mbox
import sqlite3
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
from classes.login import *
from database.database_connect import *
from main_window import *

class LoginScreen(tk.Tk):
	WIN_WIDTH = 250
	WIN_HEIGHT = 210

	def __init__(self):
		super().__init__()
		self.title(APP_NAME)
		center_win = window_center(self, self.WIN_WIDTH, self.WIN_HEIGHT, TSKB_HEIGHT)
		self.geometry(f'{self.WIN_WIDTH}x{self.WIN_HEIGHT}+{center_win[0]}+{center_win[1]}')
		self.resizable(False, False)
		self.config(bg = '#222222')
		self.update_idletasks() 
		dir = os.path.dirname(__file__)
		#To change the application icon, use another image with the same name 'app_icon.png' or change icons name from code
		self.tk.call('wm', 'iconphoto', self._w, tk.PhotoImage(file = os.path.join(dir, 'assets\\app_icon.png')))
		self.iconphoto(True, tk.PhotoImage(file = os.path.join(dir, 'assets\\app_icon.png')))
		# ===============================
		# Create Widgets
		container = tk.Frame(self, bd = 0, background = '#222222', relief = 'flat')

		username_label = InputLabel(container, 'Username')
		self.username = tk.StringVar()
		self.username_input = InputEntry(container, self.username, '')

		password_label = InputLabel(container, 'Password')
		self.password = tk.StringVar()
		self.password_input = InputEntry(container, self.password, '*')

		reset_button = Btn(container, 'Reset form', self.reset_form)
		login_button = Btn(container, 'Login', self.submit_form)

		# Show Widgets
		container.place(x = 20, y = 20, width = 210, height = 160)

		username_label.place(x = 0, y = 0, width = 210, height = 20)
		self.username_input.place(x = 0, y = 20, width = 210, height = 25)

		password_label.place(x = 0, y = 60, width = 210, height = 20)
		self.password_input.place(x = 0, y= 80, width = 210, height = 25)

		reset_button.place(x = 0, y = 130, width = 80, height = 30)
		login_button.place(x = 130, y = 130, width = 80, height = 30)

	def reset_form(self):
		self.username.set('')
		self.password.set('')
		self.username_input.focus()

	def submit_form(self):
		username = self.username.get()
		password = self.password.get()

		if len(username.strip()) > 0 and len(password.strip()) > 0:
			con = db_con()
			crs = con.cursor()
			querry = """SELECT * FROM users WHERE username = ? AND password = ?"""
			crs.execute(querry, (username, password,))
			con.commit()
			result = crs.fetchone()

			if result:
				Main(result[0])
				self.destroy()
			else:
				mbox.showerror(APP_NAME, 'The username or password is incorrect!', parent = self)
				self.reset_form()
			crs.close()
			con.close()

		else:
			mbox.showinfo(APP_NAME, 'All fields are required!', parent = self)
			self.reset_form()