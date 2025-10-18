from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image as KivyImage
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.clock import Clock
import random

class FoodAnalyzerApp(App):
    def build(self):
        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        title_label = Label(
            text='🍎 Анализатор пищевых продуктов',
            size_hint=(1, 0.1),
            font_size='20sp',
            bold=True
        )
        
        content_layout = BoxLayout(orientation='horizontal', spacing=10)
        
        left_panel = BoxLayout(orientation='vertical', size_hint=(0.5, 1))
        self.image_widget = KivyImage(size_hint=(1, 0.7), allow_stretch=True)
        self.image_status = Label(text='Нажмите "Анализировать"', size_hint=(1, 0.1))
        
        self.analyze_btn = Button(
            text='🔍 Анализировать',
            size_hint=(1, 0.1),
            background_color=(0.2, 0.4, 0.8, 1)
        )
        self.analyze_btn.bind(on_press=self.analyze_image)
        
        left_panel.add_widget(self.image_widget)
        left_panel.add_widget(self.image_status)
        left_panel.add_widget(self.analyze_btn)
        
        right_panel = BoxLayout(orientation='vertical', size_hint=(0.5, 1))
        results_title = Label(text='📊 Результаты анализа', size_hint=(1, 0.1), bold=True)
        
        scroll_view = ScrollView(size_hint=(1, 0.7))
        self.results_text = TextInput(
            text='Загрузите изображение пищевого продукта для анализа.',
            size_hint=(None, None),
            size=(400, 400),
            readonly=True
        )
        scroll_view.add_widget(self.results_text)
        
        right_panel.add_widget(results_title)
        right_panel.add_widget(scroll_view)
        
        content_layout.add_widget(left_panel)
        content_layout.add_widget(right_panel)
        main_layout.add_widget(title_label)
        main_layout.add_widget(content_layout)
        
        return main_layout
    
    def analyze_image(self, instance):
        self.results_text.text = "🔍 Анализируем изображение...\n\nПожалуйста, подождите..."
        Clock.schedule_once(self.finish_analysis, 2)
    
    def finish_analysis(self, dt):
        analysis_type = random.choice(['fruit', 'vegetable', 'bread', 'meat'])
        results_data = {
            'fruit': {'icon': '🍎', 'name': 'Фрукт', 'calories': f"{random.randint(40, 80)} ккал/100г"},
            'vegetable': {'icon': '🥦', 'name': 'Овощ', 'calories': f"{random.randint(20, 50)} ккал/100г"},
            'bread': {'icon': '🍞', 'name': 'Хлеб/Выпечка', 'calories': f"{random.randint(200, 300)} ккал/100г"},
            'meat': {'icon': '🍖', 'name': 'Белковый продукт', 'calories': f"{random.randint(150, 250)} ккал/100г"}
        }
        
        data = results_data[analysis_type]
        self.results_text.text = f"""📊 РЕЗУЛЬТАТЫ АНАЛИЗА:

{data['icon']} {data['name']}
🔥 Калорийность: {data['calories']}

🥗 Пищевая ценность:
• Белки: {random.randint(5, 25)}г
• Жиры: {random.randint(1, 15)}г  
• Углеводы: {random.randint(10, 50)}г

💡 Результаты приблизительные"""

if __name__ == '__main__':
    FoodAnalyzerApp().run()
