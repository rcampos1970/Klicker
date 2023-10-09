import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.clock import Clock

kivy.require('2.0.0')


class ClickSpeedApp(App):
    def build(self):
        self.click_count = 0
        self.clicks_per_second = 0.0
        self.last_click_time = 0.0

        self.label = Label(text="Click Speed: 0.0 CPS", font_size=30)
        self.button = Button(text="Click Me!", on_press=self.on_button_click)
        self.reset_button = Button(text="Reset", on_press=self.reset)

        layout = self.setup_layout()
        Clock.schedule_interval(self.update_clicks_per_second, 0.1)  # Update CPS every 0.1 seconds

        return layout

    def setup_layout(self):
        layout = BoxLayout(orientation="vertical", spacing=10, padding=10)
        layout.add_widget(self.label)
        layout.add_widget(self.button)
        layout.add_widget(self.reset_button)
        return layout

    def on_button_click(self, instance):
        current_time = Clock.get_time()
        time_difference = current_time - self.last_click_time
        if time_difference <= 1.0:
            self.click_count += 1
        else:
            self.click_count = 1
        self.last_click_time = current_time

    def update_clicks_per_second(self, dt):
        self.clicks_per_second = self.click_count
        self.label.text = f"Click Speed: {self.clicks_per_second:.2f} CPS"

    def reset(self, instance):
        self.click_count = 0
        self.last_click_time = 0
        self.clicks_per_second = 0.0
        self.label.text = "Click Speed: 0.0 CPS"


if __name__ == '__main__':
    from kivy.uix.boxlayout import BoxLayout
    ClickSpeedApp().run()
