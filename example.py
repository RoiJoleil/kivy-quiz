"""
KIVY BASICS TUTORIAL
A comprehensive guide to Kivy's core widgets and features

Installation: pip install kivy
"""

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.slider import Slider
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.graphics import Color, Rectangle


# ====================
# SCREEN 1: Basic Widgets
# ====================
class BasicWidgetsScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        # Main layout (vertical)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        # === LABELS ===
        title = Label(
            text='Kivy Basics Tutorial',
            size_hint=(1, 0.1),
            font_size='24sp',
            bold=True,
            color=(0.2, 0.6, 1, 1)  # RGBA: Blue
        )
        layout.add_widget(title)
        
        # === TEXT INPUT ===
        self.text_input = TextInput(
            hint_text='Type something here...',
            size_hint=(1, 0.1),
            multiline=False,
            background_color=(0.95, 0.95, 0.95, 1)
        )
        layout.add_widget(self.text_input)
        
        # === SLIDER ===
        slider_container = BoxLayout(orientation='horizontal', size_hint=(1, 0.1), spacing=10)
        slider_container.add_widget(Label(text='Slider:', size_hint=(0.2, 1)))
        
        self.slider = Slider(
            min=0, 
            max=100, 
            value=50,
            size_hint=(0.6, 1)
        )
        self.slider.bind(value=self.on_slider_change)
        slider_container.add_widget(self.slider)
        
        self.slider_label = Label(text='50', size_hint=(0.2, 1))
        slider_container.add_widget(self.slider_label)
        layout.add_widget(slider_container)
        
        # === BUTTONS ===
        button_layout = GridLayout(cols=2, size_hint=(1, 0.2), spacing=10)
        
        # Button 1: Simple action
        btn1 = Button(
            text='Show Input',
            background_color=(0.2, 0.8, 0.2, 1),  # Green
            background_normal=''
        )
        btn1.bind(on_press=self.show_input)
        button_layout.add_widget(btn1)
        
        # Button 2: Open popup
        btn2 = Button(
            text='Open Popup',
            background_color=(0.8, 0.2, 0.2, 1),  # Red
            background_normal=''
        )
        btn2.bind(on_press=self.open_popup)
        button_layout.add_widget(btn2)
        
        # Button 3: Go to next screen
        btn3 = Button(
            text='Next Screen →',
            background_color=(0.6, 0.2, 0.8, 1),  # Purple
            background_normal=''
        )
        btn3.bind(on_press=self.go_to_screen2)
        button_layout.add_widget(btn3)
        
        # Button 4: Colored layout example
        btn4 = Button(
            text='Colored Layouts',
            background_color=(1, 0.6, 0.2, 1),  # Orange
            background_normal=''
        )
        btn4.bind(on_press=self.go_to_screen3)
        button_layout.add_widget(btn4)
        
        layout.add_widget(button_layout)
        
        # === OUTPUT LABEL ===
        self.output_label = Label(
            text='Output appears here...',
            size_hint=(1, 0.3),
            color=(0.3, 0.3, 0.3, 1)
        )
        layout.add_widget(self.output_label)
        
        self.add_widget(layout)
    
    def on_slider_change(self, instance, value):
        self.slider_label.text = str(int(value))
    
    def show_input(self, instance):
        text = self.text_input.text
        if text:
            self.output_label.text = f'You typed: "{text}"'
        else:
            self.output_label.text = 'Please type something first!'
    
    def open_popup(self, instance):
        popup = Popup(
            title='This is a Popup!',
            content=Label(text='Popups are floating windows'),
            size_hint=(0.7, 0.4)
        )
        popup.open()
    
    def go_to_screen2(self, instance):
        self.manager.current = 'screen2'
    
    def go_to_screen3(self, instance):
        self.manager.current = 'screen3'


# ====================
# SCREEN 2: Layouts Demo
# ====================
class LayoutsScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        main = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Title
        main.add_widget(Label(
            text='Different Layouts',
            size_hint=(1, 0.1),
            font_size='20sp',
            bold=True
        ))
        
        # GridLayout example (3x3 grid)
        grid = GridLayout(cols=3, rows=3, size_hint=(1, 0.5), spacing=5)
        for i in range(9):
            btn = Button(text=f'Grid {i+1}')
            grid.add_widget(btn)
        main.add_widget(grid)
        
        # Back button
        back_btn = Button(
            text='← Back',
            size_hint=(1, 0.1),
            background_color=(0.2, 0.6, 1, 1),
            background_normal=''
        )
        back_btn.bind(on_press=lambda x: setattr(self.manager, 'current', 'screen1'))
        main.add_widget(back_btn)
        
        self.add_widget(main)


# ====================
# SCREEN 3: Custom Colors with Canvas
# ====================
class ColoredLayoutScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        # Using FloatLayout for absolute positioning
        layout = FloatLayout()
        
        # Add colored background using canvas
        with layout.canvas.before:
            Color(0.95, 0.95, 0.98, 1)  # Light blue-gray background
            self.rect = Rectangle(pos=layout.pos, size=layout.size)
        layout.bind(pos=self.update_rect, size=self.update_rect)
        
        # Create a colored box manually
        colored_box = BoxLayout(
            orientation='vertical',
            size_hint=(0.6, 0.5),
            pos_hint={'center_x': 0.5, 'center_y': 0.6},
            padding=20,
            spacing=10
        )
        
        # Add colored background to box
        with colored_box.canvas.before:
            Color(0.3, 0.5, 0.7, 1)  # Blue background
            self.box_rect = Rectangle(pos=colored_box.pos, size=colored_box.size)
        colored_box.bind(pos=self.update_box_rect, size=self.update_box_rect)
        
        colored_box.add_widget(Label(
            text='Custom Colored Section',
            font_size='18sp',
            bold=True,
            color=(1, 1, 1, 1)  # White text
        ))
        
        colored_box.add_widget(Label(
            text='You can color layouts using canvas!',
            color=(1, 1, 1, 1)
        ))
        
        layout.add_widget(colored_box)
        
        # Back button with absolute positioning
        back_btn = Button(
            text='← Back to Main',
            size_hint=(0.3, 0.1),
            pos_hint={'x': 0.35, 'y': 0.1},
            background_color=(0.2, 0.6, 1, 1),
            background_normal=''
        )
        back_btn.bind(on_press=lambda x: setattr(self.manager, 'current', 'screen1'))
        layout.add_widget(back_btn)
        
        self.add_widget(layout)
    
    def update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size
    
    def update_box_rect(self, instance, value):
        self.box_rect.pos = instance.pos
        self.box_rect.size = instance.size


# ====================
# MAIN APP
# ====================
class KivyTutorialApp(App):
    def build(self):
        # ScreenManager handles multiple screens (like pages/windows)
        sm = ScreenManager()
        sm.add_widget(BasicWidgetsScreen(name='screen1'))
        sm.add_widget(LayoutsScreen(name='screen2'))
        sm.add_widget(ColoredLayoutScreen(name='screen3'))
        return sm


if __name__ == '__main__':
    KivyTutorialApp().run()