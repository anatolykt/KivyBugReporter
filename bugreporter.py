from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout

from widgets.card import Card
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

	# Eye:
	# 	size_hint: None, None
	# 	pos_hint: {"center_x": .5, "top": .1}
	# 	pressing_area: 1
	# 	on_press: root.eye_press()
	# 	on_release: root.eye_release()

	Card:
		size_hint: .9, .5
		pos_hint: {"center_x": .5, "center_y": .5}
""")


class BugReporter(FloatLayout):
	def eye_press(self):
		print("Eye pressed!")
	def eye_release(self):
		print("Eye released!")