from kivy.lang import Builder
from kivy.clock import Clock
from kivy.animation import Animation

from kivy.properties import ListProperty

from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.floatlayout import FloatLayout


Builder.load_string("""
<Head>:
	canvas:
		Color:
			rgb: self.background_color
		Ellipse:
			pos: self.pos
			size: self.size

<Body>:
	canvas:
		Color:
			rgb: self.background_color
		Ellipse:
			pos: self.pos
			size: self.size

<Robot>:
	size_hint: None, None
	size: self.size

	Head:
		pos_hint: {"center_x": .5, "top": 0}
		size_hint: .8, .4

	Body:
		pos_hint: {"center_x": .5, "top": .5}
""")


class Head(FloatLayout):
	background_color = ListProperty([0.37254901960784315,
		0.776470588235294, 0.6705882352941177, 1])

	def __init__(self, **kwargs):
		super(Head, self).__init__(**kwargs)


class Body(FloatLayout):
	background_color = ListProperty([0.37254901960784315,
		0.776470588235294, 0.6705882352941177, 1])

	def __init__(self, **kwargs):
		super(Body, self).__init__(**kwargs)


class Robot(FloatLayout):
	pass