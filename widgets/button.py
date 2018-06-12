from kivy.lang import Builder
from kivy.clock import Clock

from kivy.properties import (ListProperty, 
	ObjectProperty, StringProperty, 
	BooleanProperty, NumericProperty)

from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.anchorlayout import AnchorLayout


Builder.load_string("""
<BaseButton>:
	size_hint: None, None
	size: self.size

	anchor_x: "center"
	anchor_y: "center"

	canvas:
		Color:
			rgb: self._current_background_color
		RoundedRectangle:
			pos: self.pos
			size: self.size
			radius: self._current_border_radius

	Label:
		text: root.text
		bold: root.text_bold
		color: root._current_text_color
		italic: root.text_italic
		markup: True
		halign: root.text_halign
		valign: root.text_valign
		padding: root.text_padding
		font_size: root.text_font_size
""")


class BaseButton(ButtonBehavior, AnchorLayout):
	text = StringProperty("Hello World!")
	text_bold = BooleanProperty(False)
	text_color = ListProperty([0, 0, 0, 1])
	text_italic = BooleanProperty(False)
	text_halign = StringProperty("center")
	text_valign = StringProperty("middle")
	text_padding = ListProperty([15, 15])
	text_font_size = NumericProperty(18)

	border_radius = ListProperty([15, 15, 15, 15])
	background_color = ListProperty([0.6941176470588235,
		0.15294117647058825, 0.8470588235294118, 1])

	pressed = BooleanProperty(False)
	pressed_text_color = ListProperty([.5, .5, .5, 1])
	pressed_border_radius = ListProperty([15, 15, 15, 15])
	pressed_background_color = ListProperty([0.5725490196078432,
		0.16078431372549018, 0.6980392156862745, 1])

	disabled = BooleanProperty(False)
	disabled_text_color = ListProperty([.5, .5, .5, .5])
	disabled_border_radius = ListProperty([15, 15, 15, 15])
	disabled_background_color = ListProperty([0.5725490196078432,
		0.16078431372549018, 0.6980392156862745, .5])

	_current_text_color = ListProperty([0, 0, 0, 0])
	_current_border_radius = ListProperty([0, 0, 0, 0])
	_current_background_color = ListProperty([0, 0, 0, 0])

	def __init__(self, **kwargs):
		super(BaseButton, self).__init__(**kwargs)
		Clock.schedule_once(self.initialize_color_palette)

	def initialize_color_palette(self, *args):
		self.change_styles("pressed", self.pressed)
		self.change_styles("disabled", self.disabled)

	def on_pressed(self, instance, value):
		self.change_styles("pressed", value)

	def on_disabled(self, instance, value):
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

	def on_touch_down(self, touch):
		if touch.is_mouse_scrolling or\
		not self.collide_point(*touch.pos) or\
		self in touch.ud or self.disabled:
			return False
		else:
			self.pressed = True
			if callable(self.on_press_callback):
				self.on_press_callback()
		return super(BasePressedButton, self).on_touch_down(touch)

	def on_touch_up(self, touch):
		if touch.grab_current is self:
			self.pressed = False
			if callable(self.on_release_callback):
				self.on_release_callback()
		return super(BasePressedButton, self).on_touch_up(touch)


class CMButton(BasePressedButton):
	pass