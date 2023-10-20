#################################################
#	Filename: main_window.py
#	Author: Ovidiu
#	Date: 2023-10-19
#################################################
# Include Libs
import tkinter as tk 
from tkinter import ttk
from tkinter import messagebox as mbox
import os
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
from classes.credentials import *
from database.database_connect import *

class Credentials(tk.Toplevel):
	WIN_WIDTH = 470
	WIN_HEIGHT = 270
	CONTAINER_WIDTH = 430
	CONTAINER_HEIGHT = 250
	def __init__(self, parent, username_id):
		super().__init__(parent)
		self.username_id = username_id
		self.title('Change credentials')
		center_win = window_center(self, self.WIN_WIDTH, self.WIN_HEIGHT, TSKB_HEIGHT)
		self.geometry(f'{self.WIN_WIDTH}x{self.WIN_HEIGHT}+{center_win[0]}+{center_win[1]}')
		self.resizable(False, False)
		self.wm_attributes('-toolwindow', True)
		self.focus()
		self.update_idletasks()
		# ===============================
		# Create Widgets	
		window_container = tk.Frame(self, bd = 0, relief = 'flat')
		# Title Input Top
		title_input_top = TitleInputCredentials(window_container, 'Insert current credentials')
		labelinput_usr = LabelInputCredentials(title_input_top, 'Username')
		labelinput_pws = LabelInputCredentials(title_input_top, 'Password')

		#self.usr_value = tk.StringVar()
		self.inputentry_usr = InputEntryCredentials(title_input_top, 'normal')
		#self.psw_value = tk.StringVar()
		self.inputentry_psw = InputEntryCredentials(title_input_top, 'normal')

		self.reset_btn = BtnCredentials(window_container, 'Reset form', self.reset_form_current, 'normal')
		self.check_btn = BtnCredentials(window_container, 'Check credentials', self.check_data, 'normal')
		
		# Title Input Bottom
		title_input_bottom = TitleInputCredentials(window_container, 'Insert new credentials')
		labelinput_usr_new = LabelInputCredentials(title_input_bottom, 'Username')
		labelinput_pws_new = LabelInputCredentials(title_input_bottom, 'Password')

		#self.usr_value_new = tk.StringVar()
		self.inputentry_usr_new = InputEntryCredentials(title_input_bottom, 'disabled')

		#self.psw_value_new = tk.StringVar()
		self.inputentry_psw_new = InputEntryCredentials(title_input_bottom, 'disabled')

		self.reset_btn_new = BtnCredentials(title_input_bottom, 'Reset form', self.reset_form_new, 'disabled')
		self.submit_btn = BtnCredentials(title_input_bottom, 'Update credentials', self.update_form, 'disabled')

		# Show Widgets
		window_container.place(x = 20, y = 10, width = self.CONTAINER_WIDTH, height = self.CONTAINER_HEIGHT)
		title_input_top.place(x = 0, y = 0, width = self.CONTAINER_WIDTH, height = 110)
		labelinput_usr.place(x = 5, y = 5, width = 200, height = 15)
		labelinput_pws.place(x = 220, y = 5, width = 200, height = 15)

		self.inputentry_usr.place(x = 8, y = 20, width = 195, height = 25)
		self.inputentry_psw.place(x = 223, y = 20, width = 195, height = 25)
		self.reset_btn.place(x = self.CONTAINER_WIDTH - 120 - 20 - 80, y = 70, width = 80, height = 30)
		self.check_btn.place(x = self.CONTAINER_WIDTH - 120 - 10, y = 70, width = 120, height = 30)

		title_input_bottom.place(x = 0, y = 130, width = self.CONTAINER_WIDTH, height = 115)
		labelinput_usr_new.place(x = 5, y = 5, width = 200, height = 15)
		labelinput_pws_new.place(x = 220, y = 5, width = 200, height = 15)
		self.inputentry_usr_new.place(x = 8, y = 20, width = 200, height = 25)
		self.inputentry_psw_new.place(x = 223, y = 20, width = 195, height = 25)

		self.reset_btn_new.place(x = self.CONTAINER_WIDTH - 120 - 20 - 80, y = 55, width = 80, height = 30)
		self.submit_btn.place(x = self.CONTAINER_WIDTH - 120 - 10, y = 55, width = 120, height = 30)

	def reset_form_current(self):
		self.inputentry_usr.delete(0, tk.END)
		self.inputentry_psw.delete(0, tk.END)
		self.inputentry_usr.focus()

	def reset_form_new(self):
		self.inputentry_usr_new.delete(0, tk.END)
		self.inputentry_psw_new.delete(0, tk.END)
		self.inputentry_usr_new.focus()

	def check_data(self):
		current_username = self.inputentry_usr.get()
		current_password = self.inputentry_psw.get()

		if len(current_username.strip()) > 0 and len(current_password.strip()) > 0:
			con = db_con()
			crs = con.cursor()
			querry = '''SELECT * FROM users WHERE id = ?'''
			crs.execute(querry, (self.username_id,))
			con.commit()
			result = crs.fetchone()
			db_username = result[1]
			db_password = result[2]
			crs.close()
			con.close()

			if (current_username == db_username and current_password == db_password):
				self.inputentry_usr.config(state = 'disabled')
				self.inputentry_psw.config(state = 'disabled')
				self.reset_btn.config(state = 'disabled')
				self.check_btn.config(state = 'disabled')

				self.inputentry_usr_new.config(state = 'normal')
				self.inputentry_psw_new.config(state = 'normal')
				self.reset_btn_new.config(state = 'normal')
				self.submit_btn.config(state = 'normal')

				self.reset_form_new() 
			else:
				mbox.showerror(APP_NAME, 'The data entered does not match!', parent = self)
				self.reset_form_current()
		else:
			mbox.showinfo(APP_NAME, 'All fields are required!', parent = self)
			self.reset_form_current()

	def update_form(self):
		new_username = self.inputentry_usr_new.get()
		new_password = self.inputentry_psw_new.get()

		if len(new_username.strip()) > 0 and len(new_password.strip()) > 0:
			con = db_con()
			crs = con.cursor()
			querry = '''UPDATE users SET username = ?, password = ? WHERE id = ?'''
			crs.execute(querry, (new_username, new_password, self.username_id))
			con.commit()
			crs.close()
			con.close()
			self.destroy()
		else:
			mbox.showinfo(APP_NAME, 'All fields are required!', parent = self)
			self.reset_form_current()