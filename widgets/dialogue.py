from kivy.lang import Builder
from kivy.clock import Clock

from kivy.graphics import Color, Line
from kivy.properties import (ListProperty, 
	NumericProperty, OptionProperty)

from kivy.uix.floatlayout import FloatLayout


Builder.load_string("""
<Dialogue>:
	Label:
		id: dialogue_text
		text: root.text[0]
		color: root.text_color
		padding: 10, 10
		halign: "center"
		size_hint_y: None
		heigh: self.texture_size[1]
		pos_hint: {"center_x": .5, "center_y": .5}
""")


class Dialogue(FloatLayout):
	_width = NumericProperty(50)
	_height = NumericProperty(50)

	arrow_side = OptionProperty("right",
		options=["left", "right"])
	arrow_align = OptionProperty("middle", 
		options=["top", "middle", "bottom"])

	border_color = ListProperty([.5, 0, 0, 1])
	border_width = NumericProperty(1.5)

	text = ListProperty(["Hello World", 
		"Привет мир", "Saluton mondo", "Hallo Welt"])
	text_color = ListProperty([0, 0, 0, 1])
	text_change_interval = NumericProperty(5)

	def __init__(self, **kwargs):
		super(Dialogue, self).__init__(**kwargs)
		Clock.schedule_once(self.render_dialogue_window, 1)

	def change_text(self, *args):
		current_text = self.ids.dialogue_text.text
		index = self.text.index(current_text)
		if index == len(self.text) - 1:
			next_index = 0
		else:
			next_index = index + 1
		self.ids.dialogue_text.text = self.text[next_index]

	def render_dialogue_window(self, *args, clear=False):
		points = []
		x, y = self.center

		x -= self._width / 2
		y -= self._height / 2
		points += [x, y]

		if self.arrow_side == "left":
			if self.arrow_align == "bottom":
				x -= self._width / 4
				y += self._height / 10
				points += [x, y]

				x += self._width / 4
				y += self._height / 10
				points += [x, y]

				y += self._height - (self._height / 5)
				points += [x, y]
			if self.arrow_align == "middle":
				y += (self._height - (self._height / 5)) / 2
				points += [x, y]

				x -= self._width / 4
				y += self._height / 10
				points += [x, y]

				x += self._width / 4
				y += self._height / 10
				points += [x, y]

				y += (self._height - (self._height / 5)) / 2
				points += [x, y]
			if self.arrow_align == "top":
				y += self._height - (self._height / 5)
				points += [x, y]

				x -= self._width / 4
				y += self._height / 10
				points += [x, y]

				x += self._width / 4
				y += self._height / 10
				points += [x, y]
		else:
			y += self._height
			points += [x, y]		

		x += self._width
		points += [x, y]

		if self.arrow_side == "right":
			if self.arrow_align == "top":
				x += self._width / 4
				y -= self._height / 10
				points += [x, y]

				x -= self._width / 4
				y -= self._height / 10
				points += [x, y]

				y -= self._height - (self._height / 5)
				points += [x, y]
			if self.arrow_align == "middle":
				y -= (self._height - (self._height / 5)) / 2
				points += [x, y]

				x += self._width / 4
				y -= self._height / 10
				points += [x, y]

				x -= self._width / 4
				y -= self._height / 10
				points += [x, y]

				y -= (self._height - (self._height / 5)) / 2
				points += [x, y]
			if self.arrow_align == "bottom":
				y -= self._height - (self._height / 5)
				points += [x, y]

				x += self._width / 4
				y -= self._height / 10
				points += [x, y]

				x -= self._width / 4
				y -= self._height / 10
				points += [x, y]
		else:
			y -= self._height
			points += [x, y]

		x -= self._width
		points += [x, y]

		with self.canvas:
			Color(*self.border_color)
			Line(points=points, 
				width=self.border_width)

		self.text_change_event = Clock.schedule_interval(
			self.change_text, self.text_change_interval)