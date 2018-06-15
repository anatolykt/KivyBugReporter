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

	Card:
		size_hint: .9, .5
		pos_hint: {"center_x": .5, "center_y": .5}
""")


class BugReporter(FloatLayout):
	pass