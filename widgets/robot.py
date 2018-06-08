from kivy.lang import Builder
from kivy.clock import Clock
from kivy.animation import Animation

from kivy.properties import ListProperty, NumericProperty

from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.floatlayout import FloatLayout


Builder.load_string("""
<Eye>:
	canvas:
		Color:
			rgb: self.pupil_color
		Ellipse:
			pos: self.pos
			size: self.size
		Color:
			rgb: self.iris_color
		Ellipse:
			pos: self.pos
			size: self.size
		Color:
			rgb: self.sclera_color
		Ellipse:
			pos: self.pos
			size: self.size
		Color:
			rgb: self.screen_color
		Ellipse:
			pos: self.pos
			size: self.size
		Color:
			rgb: self.screen_border_color
		Ellipse:
			pos: self.pos
			size: self.size

<Head>:
	canvas:
		Color:
			rgb: self.background_color
		Ellipse:
			pos: self.pos
			size: self.size
	Eye:
		pos_hint: {"center_x": .5, "center_y": .5}
		size_hint: .25, .5

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
		pos_hint: {"center_x": .5, "top": 1}
		size_hint: .8, .3

	Body:
		pos_hint: {"center_x": .5, "top": .75}
		size_hint: 1, .7
""")


class Eye(FloatLayout):
	pupil_color = ListProperty([1.0, 
		0.6039215686274509, 0.0, 1])
	pupil_radius_hint = NumericProperty(.1)

	iris_color = ListProperty([
		0.9803921568627452, 0.0, 0.0, 1])
	iris_radius_hint = NumericProperty(.28)

	sclera_color = ListProperty([
		0.8745098039215686, 0.0, 0.0, 1])
	sclera_radius_hint = NumericProperty(.32)

	screen_color = ListProperty([0.00392156862745098, 
		0.00392156862745098, 0.00392156862745098, 1])
	screen_radius_hint = NumericProperty(.2)

	screen_border_color = ListProperty([0.776470588235294, 
		0.776470588235294, 0.776470588235294, 1])
	screen_border_radius_hint = NumericProperty(.1)

	def __init__(self, **kwargs):
		super(Eye, self).__init__(**kwargs)


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