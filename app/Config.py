from os import path

class Config:

# colors
 MODE_COLOR = "dark"
 DEFAULT_THEME_COLOR = "dark-blue"

# strings
 TITLE = "Ticket an das DM & IIoT Team"
 TEST_BTN_TEXT = "Hilfe & Support"

 # images
 TEST_IMAGE = path.join(path.dirname(__file__), "test_image.jpg")
 ICON_IMAGE = path.join(path.dirname(__file__), "logo_image.png")