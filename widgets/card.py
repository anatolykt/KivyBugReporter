from kivy.lang import Builder
from kivy.properties import ListProperty, StringProperty
from kivy.uix.floatlayout import FloatLayout


Builder.load_string("""
<Card>:
	canvas.before:
		Color:
			rgb: self.card_background_color
		RoundedRectangle:
			pos: self.pos
			size: self.size
			radius: self.card_border_radius

	BoxLayout:
		orientation: "vertical"
		padding: 10, 10
		pos_hint: {"center_x": .5, "center_y": .5}

		Label:
			text: root.header_text
			color: root.header_text_color
			padding: root.header_padding
			size_hint_y: None
			height: self.texture_size[1]
			halign: "center"

		Label:
			text: root.subheader_text
			color: root.subheader_text_color
			padding: root.subheader_padding
			size_hint_y: None
			height: self.texture_size[1]
			halign: "center"

		BoxLayout:
			canvas.before:
				Color:
					rgb: root.textinput_background_color
				RoundedRectangle:
					pos: self.pos
					size: self.size
					radius: root.textinput_border_radius

			orientation: "horizontal"
			padding: 10, 10

			TextInput:
				text: root.textinput_text
				color: root.textinput_text_color
				background_color: root.textinput_background_color
""")


class Card(FloatLayout):
	card_border_radius = ListProperty([15, 15])
	card_background_color = ListProperty([.937, .945, .949, 1])

	header_text = StringProperty("Card Header")
	header_padding = ListProperty([0, 5])
	header_text_color = ListProperty([0, 0, 0, 1])

	subheader_text = StringProperty("Card Subheader")
	subheader_padding = ListProperty([0, 15])
	subheader_text_color = ListProperty([0, 0, 0, .5])

	textinput_text = StringProperty(" Error Traceback... " * 50)
	textinput_text_color = ListProperty([0, 0, 0, 1])
	textinput_border_radius = ListProperty([15, 15])
	textinput_background_color = ListProperty([255, 255, 255, 1])

	def __init__(self, **kwargs):
		super(Card, self).__init__(**kwargs)