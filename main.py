from kivymd.app import MDApp


class MainApp(MDApp):
    def build(self):
        self.title="KivyMD Travel App"
        self.theme_cls.primary_palette='BlueGray'
MainApp().run()