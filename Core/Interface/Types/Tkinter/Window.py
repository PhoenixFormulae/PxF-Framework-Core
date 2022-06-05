## System Imports
import tkinter
from typing import Optional


## Application Imports
from Core.Interface.Window import BaseWindow


## Library Imports


class TkinterWindow(BaseWindow):
	
	def __init__(self, frame, frame_configuration):
		super().__init__()
		
		self.__frame = frame
		
		self.__window_configuration = frame_configuration
		
		self.__window: Optional[tkinter.Tk] = self.Create()
	
	def __del__(self):
		pass
	
	def Create(self) -> tkinter.Tk:
		window = tkinter.Tk()
		window.title(self.__window_configuration.Title)
		
		window.geometry(f"{self.__window_configuration.Width}x{self.__window_configuration.Height}")
		
		window.attributes('-fullscreen', not self.__window_configuration.Windowed)
		
		return window
	
	def Loop(self):
		self.__window.mainloop()
