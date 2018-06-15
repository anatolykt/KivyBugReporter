from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout

from widgets.card import Card
from widgets.robot import Eye
from widgets.button import CMButton
from widgets.dialogue import Dialogue

Builder.load_string("""
<BugReporter>:
	canvas:
		Color:
			rgb: 255, 255, 255, 1
		Rectangle:
			pos: root.pos
			size: root.size

	Label:
		text: "Something is broken"
		color: 0, 0, 0, .8
		font_size: dp(32)
		size_hint_y: None
		height: self.texture_size[1]
		halign: "center"
		pos_hint: {"top": .95}

	Label:
		text: "To fix it shortly, please report us a bug!"
		color: 0, 0, 0, .5
		font_size: dp(28)
		size_hint_y: None
		height: self.texture_size[1]
		halign: "center"
		pos_hint: {"top": .87}

	Eye:
		size_hint: .5, .6
		pos_hint: {"center_x": .5, "center_y": .45}

	Dialogue:
		_width: 200
		_height: 100
		text: ["I am sorry, David", "I am afraid", "I can not do that"]
		border_width: 5
		text_font_size: 20
		pos_hint: {"center_x": .15, "center_y": .5}

	CMButton:
		text: "Exit"
		text_color: 255, 255, 255, 1
		pos_hint: {"right": .35, "center_y": .09}

	CMButton:
		text: "Report"
		pos_hint: {"right": .75, "center_y": .09}
""")


class BugReporter(FloatLayout):
	pass