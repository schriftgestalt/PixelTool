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
		# self.generalContextMenus = [
		# 	{'name': Glyphs.localize({'en': u'Layer info in Macro window', 'de': u'Ebenen-Infos in Makro-Fenster'}), 'action': self.printInfo},
		# ]
		self.keyboardShortcut = 'x'

	def start(self):
		pass

	def activate(self):
		pass

	def background(self, layer):
		pass
	
	def deactivate(self):
		pass
	
	def mouseDown1_(self, event):
		pass
	
	def mouseUp_(self, event):
		
		if not self.dragging():
			Loc = self.editViewController().graphicView().getActiveLocation_(event)
			print Loc
			layer = self.editViewController().graphicView().activeLayer()
			font = layer.font()
			pixel = font.glyphs["pixel"]
			if pixel is None:
				Message("Missing glyph", "Please add pixel glyph")
				return
			print font
			grid = font.grid
			origin = NSPoint(math.floor(Loc.x / grid) * grid, math.floor(Loc.y / grid) * grid)
			foundPixel = False
			for c in layer.components:
				if c.componentName == "pixel" and distance(c.position, origin) < 1:
					foundPixel = True
					layer.components.remove(c)
					break
			if not foundPixel:
				c = GSComponent("pixel")
				c.position = origin
				layer.components.append(c)
		else:
			objc.super(PixelTool, self).mouseUp_(event)
	
	def conditionalContextMenus(self):
		pass
		# # Empty list of context menu items
		# contextMenus = []
		#
		# # Execute only if layers are actually selected
		# if Glyphs.font.selectedLayers:
		# 	layer = Glyphs.font.selectedLayers[0]
		#
		# 	# Exactly one object is selected and it’s an anchor
		# 	if len(layer.selection) == 1 and type(layer.selection[0]) == GSAnchor:
		#
		# 		# Add context menu item
		# 		contextMenus.append({'name': Glyphs.localize({'en': u'Randomly move anchor', 'de': u'Anker zufällig verschieben'}), 'action': self.randomlyMoveAnchor})
		#
		# # Return list of context menu items
		# return contextMenus

	# def printInfo(self):
	# 	"""
	# 	Example for a method triggered by a context menu item.
	# 	Fill in your own method name and code.
	# 	Remove this method if you do not want any extra context menu items.
	# 	"""
	#
	# 	# Execute only if layers are actually selected
	# 	if Glyphs.font.selectedLayers:
	# 		layer = Glyphs.font.selectedLayers[0]
	#
	# 		# Do stuff:
	# 		print "Current layer:", layer.parent.name, layer.name
	# 		print "  Number of paths:", len(layer.paths)
	# 		print "  Number of components:", len(layer.components)
	# 		print "  Number of anchors:", len(layer.anchors)

		
		
	def __file__(self):
		"""Please leave this method unchanged"""
		return __file__