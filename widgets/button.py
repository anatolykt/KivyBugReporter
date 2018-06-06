from kivy.lang import Builder
from kivy.animation import Animation
from kivy.properties import (ListProperty, 
	ObjectProperty, StringProperty, 
	BooleanProperty, NumericProperty)
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.anchorlayout import AnchorLayout


Builder.load_string("""
<BaseButton>:
	size_hint: None, None
	anchor_x: "center"
	anchor_y: "center"

	canvas:
		Clear
		Color:
			rgb: self._current_background_color
		RoundedRectangle:
			pos: self.pos
			size: self.size
			raduis: self._current_border_radius

	Label:
		text: self.text
		bold: self.bold
		color: self.__current_text_color
		italic: self.italic
		markup: True
		halign: "center"
		valign: "middle"
		padding: self.text_padding
		font_name: self.font_family
		font_size: self.font_size
""")


class BaseButton(ButtonBehavior, AnchorLayout):
	text = StringProperty("")
	bold = BooleanProperty(False)
	italic = BooleanProperty(False)
	font_size = NumericProperty(16)
	font_family = StringProperty("")
	text_padding = ListProperty([0, 0])

	text_color = ListProperty([0, 0, 0, 1])
	border_radius = ListProperty([0, 0, 0, 0])
	background_color = ListProperty([.5, .5, .5, 1])

	pressed = BooleanProperty(False)
	pressed_text_color = ListProperty([.3, .3, .3, 1])
	pressed_border_radius = ListProperty([0, 0, 0, 0])
	pressed_background_color = ListProperty([.7, .7, .7, 1])

	disabled = BooleanProperty(False)
	disabled_text_color = ListProperty([.7, .7, .7, 1])
	disabled_border_radius = ListProperty([0, 0, 0, 0])
	disabled_background_color = ListProperty([.9, .9, .9, 1])

	_current_text_color = ListProperty([0, 0, 0, 0])
	_current_border_radius = ListProperty([0, 0, 0, 0])
	_current_background_color = ListProperty([0, 0, 0, 0])

	def __init__(self, **kwargs):
		super(BaseButton, self).__init__(**kwargs)

	def on_pressed(self, value):
		self.change_styles("pressed", value)

	def on_disabled(self, value):
		self.change_styles("disabled", value)

	def change_styles(self, key, value):
		self.change_text_color(getattr(self, key + "_text_color")\
			if value is True else self.text_color)
		self.change_border_raduis(getattr(self, key + "_border_radius")\
			if value is True else self.border_radius)
		self.change_background_color(getattr(self, key + "_background_color")\
			if value is True else self.background_color)

	def change_text_color(self, value):
		self._current_text_color = value

	def change_border_raduis(self, value):
		self._current_border_radius = value

	def change_background_color(self, value):
		self._current_background_color = value


class BasePressedButton(BaseButton):
	on_press_callback = ObjectProperty(None)
	on_release_callback = ObjectProperty(None)

	def __init__(self, **kwargs):
		super(BasePressedButton, self).__init__(**kwargs)

	def on_press(self):
		if callable(self.on_press_callback):
			self.on_press_callback()

	def on_release(self):
		if callable(self.on_release_callback):
			self.on_release_callback()