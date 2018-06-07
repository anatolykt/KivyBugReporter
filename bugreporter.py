from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout

from widgets.button import CButton

Builder.load_string("""
<BugReporter>:
	canvas:
		Color:
			rgb: 255, 255, 255, 1
		Rectangle:
			pos: root.pos
			size: root.size
	CButton:
		size: dp(150), dp(50)
		pos_hint: {"center_x": .5, "center_y": .5}
""")


class BugReporter(FloatLayout):
	pass