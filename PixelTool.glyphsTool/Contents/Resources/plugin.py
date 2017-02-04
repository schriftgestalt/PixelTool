# encoding: utf-8

###########################################################################################################
#
#
#	Select Tool Plugin
#
#	Read the docs:
#	https://github.com/schriftgestalt/GlyphsSDK/tree/master/Python%20Templates/SelectTool
#
#
###########################################################################################################


from GlyphsApp.plugins import *
import math

class PixelTool(SelectTool):
	
	def settings(self):
		self.name = "Pixel Tool"
		self.keyboardShortcut = 'x'
	
	def start(self):
		pass
	
	def activate(self):
		pass
	
	def background(self, layer):
		pass
	
	def deactivate(self):
		pass
	
	def setPixel(self, event, force = 0):
		Loc = self.editViewController().graphicView().getActiveLocation_(event)
		layer = self.editViewController().graphicView().activeLayer()
		font = layer.font()
		pixel = font.glyphs["pixel"]
		if pixel is None:
			Message("Missing glyph", "Please add pixel glyph")
			return
		grid = font.grid
		origin = NSPoint(math.floor(Loc.x / grid) * grid, math.floor(Loc.y / grid) * grid)
		
		for c in layer.components:
			if c.componentName == "pixel" and distance(c.position, origin) < 1:
				if force != 1:
					layer.components.remove(c)
				return -1
		
		if force != -1:
			c = GSComponent("pixel")
			c.position = origin
			layer.components.append(c)
		return 1
	
	def mouseDown_(self, event):
		if event.clickCount() == 3:
			self.mouseTripleDown_(event)
			return
		if event.clickCount() == 2:
			self.mouseDoubleDown_(event)
			return
		self.initialMode = self.setPixel(event)
	
	def mouseDragged_(self, event):
		self.setPixel(event, self.initialMode)
		
	def mouseUp_(self, event):
		pass
	
	def __file__(self):
		"""Please leave this method unchanged"""
		return __file__