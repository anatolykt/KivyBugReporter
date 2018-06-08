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
			rgb: self.screen_border_color
		Ellipse:
			pos: self.pos
			size: self.size
		Color:
			rgb: self.screen_color
		Ellipse:
			pos: self._screen_pos
			size: self._screen_size
		Color:
			rgb: self.sclera_color
		Ellipse:
			pos: self._sclera_pos
			size: self._sclera_size
		Color:
			rgb: self.iris_color
		Ellipse:
			pos: self._iris_pos
			size: self._iris_size
		Color:
			rgb: self.pupil_color
		Ellipse:
			pos: self._pupil_pos
			size: self._pupil_size

<Head>:
	canvas:
		Color:
			rgb: self.color
		Ellipse:
			pos: self.pos
			size: self.size
	Eye:
		pos_hint: {"center_x": .5, "center_y": .5}
		size_hint: .23, .5

<Shoulder>:
	canvas:
		Color:
			rgb: self.color
		Ellipse:
			pos: self.pos
			size: self.size
	canvas.before:
		PushMatrix
		Rotate:
			angle: self.angle
			origin: self.center
	canvas.after:
		PopMatrix

<Hand>:
	canvas:
		Color:
			rgb: self.color
		Rectangle:
			pos: self.pos
			size: self.width, self.height * .4
	canvas.before:
		PushMatrix
		Rotate:
			angle: 45
			origin: self.center
	canvas.after:
		PopMatrix

<Arm>:
	canvas:
		Color:
			rgb: self.color
		Rectangle:
			pos: self.pos
			size: self.size

<Body>:
	canvas:
		Color:
			rgb: self.color
		Ellipse:
			pos: self.pos
			size: self.size
	Shoulder:
		angle: 30
		pos_hint: {"right": .25, "top": .9}
		size_hint: .2, .15
	Arm:
		pos_hint: {"right": .19, "top": .8}
		size_hint: .08, .8
	Shoulder:
		angle: 150
		pos_hint: {"right": .95, "top": .9}
		size_hint: .2, .15
	Arm:
		pos_hint: {"right": .89, "top": .8}
		size_hint: .08, .8

<Robot>:
	size_hint: None, None
	size: self.size

	# Body:
	# 	pos_hint: {"center_x": .5, "top": .75}
	# 	size_hint: 1, .7
	# Head:
	# 	pos_hint: {"center_x": .5, "top": 1}
	# 	size_hint: .8, .3

	# Hand:
	# 	pos_hint: {"center_x": .5, "center_y": .5}
	# 	size_hint: .5, .5

	Eye:
		pos_hint: {"center_x": .5, "center_y": .5}
		size_hint: 1, .4
""")


class Eye(FloatLayout):
	pupil_color = ListProperty([1.0, 
		0.6039215686274509, 0.0, 1])
	pupil_hint = NumericProperty(.1)

	_pupil_pos = ListProperty([0, 0])
	_pupil_size = ListProperty([0, 0])

	iris_color = ListProperty([
		0.9803921568627452, 0.0, 0.0, 1])
	iris_hint = NumericProperty(.4)

	_iris_pos = ListProperty([0, 0])
	_iris_size = ListProperty([0, 0])

	sclera_color = ListProperty([
		0.8745098039215686, 0.0, 0.0, 1])
	sclera_hint = NumericProperty(.7)

	_sclera_pos = ListProperty([0, 0])
	_sclera_size = ListProperty([0, 0])

	screen_color = ListProperty([0.00392156862745098, 
		0.00392156862745098, 0.00392156862745098, 1])
	screen_hint = NumericProperty(.9)

	_screen_pos = ListProperty([0, 0])
	_screen_size = ListProperty([0, 0])

	screen_border_color = ListProperty([0.776470588235294, 
		0.776470588235294, 0.776470588235294, 1])

	def __init__(self, **kwargs):
		super(Eye, self).__init__(**kwargs)
		Clock.schedule_once(self.initialize_sizes_and_positions, 1)

	def initialize_sizes_and_positions(self, *args):
		for elem in ("pupil", "iris", "sclera", "screen"):
			params = self.calculate_pos(getattr(self, elem + "_hint"))
			setattr(self, "_" + elem + "_pos", params[0])
			setattr(self, "_" + elem + "_size", params[1])

	def calculate_size(self, hint):
		width = self.width * hint
		height = self.height * hint
		return (width, height)

	def calculate_pos(self, hint):
		size = self.calculate_size(hint)
		x = self.x + (self.width - size[0]) / 2
		y = self.y + (self.height - size[1]) / 2
		return ((x, y), size)


class Head(FloatLayout):
	color = ListProperty([0.37254901960784315,
		0.776470588235294, 0.6705882352941177, 1])

	def __init__(self, **kwargs):
		super(Head, self).__init__(**kwargs)


class Shoulder(FloatLayout):
	angle = NumericProperty(0)
	color = ListProperty([0.9921568627450981,
		0.8431372549019608, 0.3764705882352941, 1])

	def __init__(self, **kwargs):
		super(Shoulder, self).__init__(**kwargs)


class Arm(FloatLayout):
	color = ListProperty([0.9921568627450981,
		0.8431372549019608, 0.3764705882352941, 1])

	def __init__(self, **kwargs):
		super(Arm, self).__init__(**kwargs)


class Hand(FloatLayout):
	color = ListProperty([0.9921568627450981,
		0.8431372549019608, 0.3764705882352941, 1])

	def __init__(self, **kwargs):
		super(Hand, self).__init__(**kwargs)


class Body(FloatLayout):
	color = ListProperty([0.37254901960784315,
		0.776470588235294, 0.6705882352941177, 1])

	def __init__(self, **kwargs):
		super(Body, self).__init__(**kwargs)


class Robot(FloatLayout):
	pass