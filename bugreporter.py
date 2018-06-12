from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout

from widgets.robot import Eye
from widgets.button import CMButton

Builder.load_string("""
<BugReporter>:
	canvas:
		Color:
			rgb: 255, 255, 255, 1
		Rectangle:
			pos: root.pos
			size: root.size

	Eye:
		size_hint: None, None
		pos_hint: {"center_x": .5, "center_y": .5}

		pressing_area: 1
		on_press: root.eye_press()
		on_release: root.eye_release()
""")


class BugReporter(FloatLayout):
	def eye_press(self):
		print("Eye pressed!")
	def eye_release(self):
		print("Eye released!")