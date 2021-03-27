from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivymd.uix.button import MDFlatButton
from helpers import screen_helper
from kivy.core.window import Window
from kivymd.uix.dialog import MDDialog

Window.size = (350, 650)


class CaseInApp(MDApp):

    def build(self):
        self.theme_cls.primary_palette = "Indigo"
        self.theme_cls.primary_hue = "700"
        screen = Builder.load_string(screen_helper)
        return screen

    def login(self):
        logins = {'newcomer': '123', 'mentor': '456'}
        if self.root.ids.login.text in logins and self.root.ids.password.text == logins[self.root.ids.login.text]:
            self.root.ids.manager.current = 'home'
            self.root.ids.navigator.opacity = 1
            self.root.ids.atom.opacity = 1
            self.root.ids.top_bar.opacity = 1

        elif not self.root.ids.login.text:

            self.root.ids.login.hint_text = 'Введите логин'
            self.root.ids.login.line_color_focus = (1, 0, 0, 1)
        else:
            dialog = MDDialog(title='Неправильный логин или пароль',
                                   size_hint=(0.8, 1),
                                   buttons=[MDFlatButton(text='Close', on_release=lambda x: dialog.dismiss())]
                                   )
            dialog.open()

    def change_screen(self, screen, *args):
        self.root.current = screen


if __name__ == '__main__':
    CaseInApp().run()