from kivy.lang import Builder
from kivy.clock import Clock

from kivy.properties import (ListProperty, 
	StringProperty, BoundNumericPropery)

from kivy.uix.floatlayout import FloatLayout


Builder.load_string("""
<Dialogue>:
	canvas:
		Color:
			rgb: self.background_color
		RoundedRectangle:
			pos: self.pos
			size: self.size
			radius: 15, 15, 15, 15
""")


class Dialogue(FloatLayout):
	text = ListProperty(["One", "Two", "Three"])
	text_color = ListProperty([0, 0, 0, 1])
	padding = ListProperty([15, 15])
	frequency = BoundNumericPropery(1, min=1, max=5)
	background_color = ListProperty([0, 0, 0, 1])
	
	def __init__(self, **kwargs):
		super(Dialogue, self).__init__(**kwargs)