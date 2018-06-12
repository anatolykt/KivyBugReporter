from kivy.lang import Builder
from kivy.properties import ListProperty, StringProperty
from kivy.uix.floatlayout import FloatLayout


Builder.load_string("""
<Card>:
	canvas:
		Color:
			rgb: self.card_color
		RoundedRectangle:
			pos: self.pos
			size: self.size
			radius: self.card_radius

	BoxLayout:
		orientation: "vertical"
		padding: 10, 10

		pos_hint: {"center_x": .5, "center_y": .5}

		Label:
			text: root.header_text
			color: root.header_color
			size_hint: 1, .15

		Label:
			text: root.subheader_text
			color: root.subheader_color
			size_hint: 1, .15

		TextInput:
			size_hint: 1, .7

			text: root.content_text
			color: root.content_color
			background_color: 
				root.content_background

			scroll_y: 0
			multiline: True
			allow_copy: True
			auto_indent: True
""")


class Card(FloatLayout):
	card_color = ListProperty([0.9372549019607843, 
		0.9450980392156862, 0.9490196078431372, 1])
	card_radius = ListProperty([15, 15, 15, 15])

	header_text = StringProperty("Header text")
	header_color = ListProperty([0, 0, 0, 1])

	subheader_text = StringProperty("Subheader text")
	subheader_color = ListProperty([0, 0, 0, .5])

	content_text = StringProperty("Hello World!!!\n" * 100)
	content_color = ListProperty([0, 0, 0, 1])
	content_background = ListProperty([255, 255, 255, 1])

	def __init__(self, **kwargs):
		super(Card, self).__init__(**kwargs)