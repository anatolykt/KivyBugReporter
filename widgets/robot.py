from math import sin, cos, atan, floor

from kivy.lang import Builder
from kivy.clock import Clock
from kivy.core.window import Window

from kivy.properties import (ListProperty, 
	NumericProperty, ObjectProperty, 
	BoundedNumericProperty, BooleanProperty)

from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.floatlayout import FloatLayout


Builder.load_string("""
<BaseEye>:
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
""")


class BaseEye(ButtonBehavior, FloatLayout):
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
		super(BaseEye, self).__init__(**kwargs)
		Clock.schedule_once(self.set_sizes_and_positions, 1)

	def on_pos(self, *args):
		self.set_sizes_and_positions()

	def on_size(self, *args):
		self.set_sizes_and_positions()

	def on_touch_move(self, touch):
		eye_center_x = self.x + self.width / 2
		eye_center_y = self.y + self.height / 2

		# width distribution from
		# the center of the eye.
		eye_width_on_left_side = eye_center_x
		eye_width_on_right_side = Window.width - eye_center_x

		# height distribution from
		# center of the eye.
		eye_height_on_top_side = eye_center_y
		eye_height_on_bottom_side = Window.height - eye_center_y

		# Offset of the touch pointer
		# relative to center of the eye.
		touch_x_offset = touch.x - eye_center_x
		touch_y_offset = touch.y - eye_center_y

		# Offset of the touch pointer
		# relative to width and height
		# distribution of the eye
		# mesured in percent.
		touch_x_offset_hint = ((touch_x_offset * 100) / \
			(eye_width_on_left_side if touch_x_offset < 0
				else eye_width_on_right_side)) / 100

		touch_y_offset_hint = ((touch_y_offset * 100) / \
			(eye_height_on_bottom_side if touch_y_offset < 0 
				else eye_height_on_top_side)) / 100
		
		# Ranges of vertical and 
		# horizontal shift of pupil
		range_of_vertical_shift = abs(
			self._sclera_size[1] - self._pupil_size[1]) / 6
		range_of_horizontal_shift = abs(
			self._sclera_size[0] - self._pupil_size[0]) / 6

		# Maximum and minimum vertical
		# and horizontal shift of pupil
		max_x, max_y = self._sclera_size
		min_x, min_y = (
			max_x + self._sclera_pos[0], 
			max_y + self._sclera_pos[1])

		# calculating coordinates of pupil
		pupil_x, pupil_y = self._pupil_pos
		pupil_x, pupil_y = (
			eye_center_x + (range_of_horizontal_shift * touch_x_offset_hint),
			eye_center_y + (range_of_vertical_shift * touch_y_offset_hint)
		)

		# and setting that coordinates to it
		self._pupil_pos = (pupil_x, pupil_y)

		return super(BaseEye, self).on_touch_move(touch)

	def on_touch_up(self, touch):
		# set pupil position to center of eye
		eye_center_x = self.x + self.width / 2
		eye_center_y = self.y + self.height / 2
		pupil_center_x = eye_center_x - self._pupil_size[0] / 2
		pupil_center_y = eye_center_y - self._pupil_size[1] / 2
		self._pupil_pos = (pupil_center_x, pupil_center_y)
		return super(BaseEye, self).on_touch_up(touch)

	def calculate_size(self, hint):
		width = self.width * hint
		height = self.height * hint
		return (width, height)

	def calculate_pos(self, size):
		x = self.x + (self.width - size[0]) / 2
		y = self.y + (self.height - size[1]) / 2
		return (x, y)

	def calculate_params(self, hint):
		size = self.calculate_size(hint)
		pos = self.calculate_pos(size)
		return (size, pos)

	def set_sizes_and_positions(self, *args):
		for eye_part in ("pupil", "iris", "sclera", "screen"):
			params = self.calculate_params(
				getattr(self, eye_part + "_hint"))
			setattr(self, "_" + eye_part + "_pos", params[1])
			setattr(self, "_" + eye_part + "_size", params[0])


class BaseEyePressed(BaseEye):
	# Number of eye parts clickin on which
	# be ragarded as pressing the button.
	# 1 - pupil
	# 2 - pupil + iris
	# 3 - pupil + iris + sclera
	# 4 - pupil + iris + sclera + screen
	# 5 - pupil + iris + sclera + screen + border
	pressing_area = BoundedNumericProperty(1, min=1, max=5)

	change_colors_on_press = BooleanProperty(False)
	pressed_pupil_color = ListProperty([0, 0, 0, 0])
	pressed_iris_color = ListProperty([0, 0, 0, 0])
	pressed_sclera_color = ListProperty([0, 0, 0, 0])
	pressed_screen_color = ListProperty([0, 0, 0, 0])
	pressed_border_color = ListProperty([0, 0, 0, 0])

	on_press_callback = ObjectProperty(None)
	on_release_callback = ObjectProperty(None)

	def __init__(self, **kwargs):
		super(BaseEyePressed, self).__init__(**kwargs)

	def on_touch_down(self, touch):
		if touch.is_mouse_scrolling or self in touch.ud or \
		   not self.collide_pressing_area(touch):
			return False
		else:
			if callable(self.on_press_callback):
				self.on_press_callback()
		return super(BaseEyePressed, self).on_touch_down(touch)

	def on_touch_up(self, touch):
		if touch.grab_current is self:
			if callable(self.on_release_callback):
				self.on_release_callback()
		return super(BaseEyePressed, self).on_touch_up(touch)

	def collide_pressing_area(self, touch):
		areas = ("pupil", "iris", "sclera", "screen", "border")
		eye_part = areas[self.pressing_area - 1]

		area_x, area_y = getattr(self, "_" + eye_part + "_pos")
		area_w, area_h = getattr(self, "_" + eye_part + "_size")

		if area_x <= touch.x <= (area_x + area_w) and \
		   area_y <= touch.y <= (area_y + area_h):
		    return True

class Eye(BaseEyePressed):
	pass