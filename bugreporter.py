from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout

from widgets.robot import Robot
from widgets.button import CMButton

Builder.load_string("""
<BugReporter>:
	canvas:
		Color:
			rgb: 255, 255, 255, 1
		Rectangle:
			pos: root.pos
			size: root.size
			
	Robot:
		size: root.width * .5, root.height * .5
		pos_hint: {"center_x": .5, "top": 1}
""")


class BugReporter(FloatLayout):
	pass