# import different modules
from kivymd.uix.screen import MDScreen
from docx2pdf import convert
from kivymd.app import MDApp
from kivy.uix.image import Image
from kivymd.uix.button import MDFillRoundFlatIconButton, MDFillRoundFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDToolbar
from kivymd.uix.button import MDFlatButton
from kivymd.uix.filemanager import MDFileManager


# Main Class

class MyApp(MDApp):

    # function to refresh page
    def fresh(self):
        if self.state == 0:
            self.label.text = "Convert another word file"
            self.input.text = ""
            self.state = 1

        elif self.state == 1:
            self.label.text = "Convert another word file"
            self.input.text = ""

    # function for conversion of word file to pdf file

    def convertion(self, args):
        if self.input.text == "":
            self.label.text = "Please give path"
        else:
            list = [""]
            list.append(self.input.text)
            l = ''.join(map(str, list))

            convert(f"{l}")
            if True:
                self.label.text = 'Converted successfully'
                self.state = 1

    # init() function
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.file_manager_obj = MDFileManager(
            select_path=self.select_path,
            exit_manager=self.close_file_manager,
            preview=False
        )

    # function for selecting path of a file
    def select_path(self, path):
        self.input.text = path
        if True:
            self.close_file_manager(self)

    # function for opening file manager
    def open_file_manager(self, args):
        self.file_manager_obj.show('/')

    # function for closing file manager
    def close_file_manager(self, args):
        self.file_manager_obj.close()

    # build function

    def build(self):
        self.state = 0

        # defining screen
        screen = MDScreen()

        # changing the color of the theme-
        self.theme_cls.primary_palette = "Purple"

        # toolbar
        self.toolbar = MDToolbar(title="Word to Pdf Converter")
        self.toolbar.pos_hint = {'top': 1}
        self.toolbar.right_action_items = [
            ["refresh", lambda x:self.fresh()]]

        screen.add_widget(self.toolbar)

        # image
        self.image = Image(source="1_5PYkSnlRCKJvuI8aDdlB0Q.jpg", size_hint_x=0.4, pos_hint={
                           "center_x": 0.5, "center_y": 0.68})

        screen.add_widget(self.image)

        # label
        self.label = MDLabel(
            text="", font_size=19, halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.5},
            theme_text_color="Primary")

        # buttons
        self.button = MDFillRoundFlatButton(text="Choose File",
                                            font_size=16,
                                            pos_hint={"center_x": 0.5,
                                                      "center_y": 0.4},
                                            on_press=self.open_file_manager)

        self.label1 = MDLabel(
            text="Or", font_size=16, halign="center",
            pos_hint={"center_x": 0.5, "center_y": 0.35},
            theme_text_color="Primary")

        self.input = MDTextField(hint_text="Enter the path",
                                 helper_text="Fill details",
                                 helper_text_mode="on_focus", pos_hint={"center_x": 0.5, "center_y": 0.3}, size_hint_x=0.8)

        self.button1 = MDFillRoundFlatButton(text="Convert",
                                             font_size=18,
                                             pos_hint={"center_x": 0.5,
                                                       "center_y": 0.2},
                                             on_press=self.convertion)

        # adding widgets
        screen.add_widget(self.input)
        screen.add_widget(self.button)
        screen.add_widget(self.button1)
        screen.add_widget(self.label)
        screen.add_widget(self.label1)

        return screen


# main function to run the MyApp()
if __name__ == "__main__":
    MyApp().run()
