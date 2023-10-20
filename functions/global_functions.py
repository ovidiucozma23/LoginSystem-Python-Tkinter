#################################################
#	Filename: global_functions.py
#	Author: Ovidiu
#	Date: 2023-10-19
#################################################

def window_center(self, window_width, window_height, taskbar):
	screen_width = self.winfo_screenwidth()
	screen_height = self.winfo_screenheight()
	center_x = int((screen_width - window_width) // 2)
	center_y = int(((screen_height - window_height) // 2) - taskbar)

	return center_x, center_y