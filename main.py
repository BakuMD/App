# main.py
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup

class CompanyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical')
        companies = {
            "Компания A": "Описание компании A.",
            "Компания B": "Описание компании B.",
            "Компания C": "Описание компании C.",
            "Компания D": "Описание компании D.",
            "Компания E": "Описание компании E.",
            "Компания F": "Описание компании F.",
            "Компания G": "Описание компании G.",
            "Компания H": "Описание компании H.",
            "Компания I": "Описание компании I.",
            "Компания J": "Описание компании J.",
        }

        for name, description in companies.items():
            btn = Button(text=name)
            btn.bind(on_press=lambda instance, desc=description: self.show_description(desc))
            layout.add_widget(btn)

        return layout

    def show_description(self, description):
        popup = Popup(title='Описание компании', content=Label(text=description), size_hint=(0.8, 0.4))
        popup.open()

if __name__ == '__main__':
    CompanyApp().run()

