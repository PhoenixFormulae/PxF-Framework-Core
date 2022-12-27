## framework imports
import tkinter


## Application imports
from Content.Interface.Frames.Types.Tkinter.View.Control import Control


## Library imports


class Button(Control, tkinter.Button):
	
	Type = 'button'
	
	def __init__(self, parent):
		super(tkinter.Button, self).__init__(parent, self.Type)
		super(Control).__init__()
	
	def __del__(self):
		super(tkinter.Button, self).destroy()
