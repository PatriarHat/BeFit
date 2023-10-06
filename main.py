from kivymd.app import MDApp

from kivy.properties import ObjectProperty
from kivy.uix.videoplayer import VideoPlayer
from kivy.metrics import dp

from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.button import MDFlatButton
from kivymd.uix.navigationdrawer import (MDNavigationLayout,
    MDNavigationDrawer,
    MDNavigationDrawerMenu,
    MDNavigationDrawerLabel,
    MDNavigationDrawerDivider,
    MDNavigationDrawerItem,
)
from kivymd.uix.button import MDIconButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.screen import MDScreen
from kivymd.uix.list import MDList,OneLineListItem
from kivymd.uix.dialog import MDDialog
from kivymd.uix.screenmanager import MDScreenManager, ScreenManager
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.label import MDLabel


import requests
from fatsecret import Fatsecret
response = requests.get("https://platform.fatsecret.com/rest/server.api")


class ContentNavigationDrawer(MDScrollView):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()

class BeFit(MDApp):
    dialog = None

    def build(self):
        self.theme_cls.primary_palette = "Orange"
        self.theme_cls.theme_style = "Dark"


        return (
            MDScreen(
                MDTopAppBar(
                    pos_hint={"top": 1},
                    elevation=0,
                    title = "BeFit",
                    left_action_items=[["menu", lambda x: self.nav_drawer_open()]],
                    ),
                MDNavigationLayout(
                    MDScreenManager(
                        MDScreen(
                            MDGridLayout(
                                MDLabel(
                                    text = 'Головним  скарбом  життя  є  не  землі,  що  ти  їх  завоював,  не  багатства,  що  їх маєш  у  скринях...  Головним  скарбом  життя  є  здоров’я,  і,  щоб  його  зберегти, потрібно багато що знати.  (Авіцена)',
                                    font_style = "Button",
                                ),
                                MDLabel(
                                    text='Поведінка  є  таким  самим  джерелом  патології,  як  гени  й середовище... Неправильна  поведінка  людей  є  більш  частою  причиною  їхніх захворювань, аніж зовнішні дії чи слабкість природи людини. (М. Амосов)',
                                    font_style="Button",
                                ),
                                MDLabel(
                                    text='Життя — цікаве, і мотивація то є сильна: філософія, психологія. саме головне — залишайтеся людьми і кричіть, що ви живі Я ЖИВИИИИИЙ! Я СИЛЬНИЙ! (П.Моставчук)',
                                    font_style="Button",
                                ),
                                MDLabel(
                                    text='Здоров’я - такий  же  унікум,  як  картина  Рафаеля.  Знищити  його  легко, відновити неможливо. (І. Бородін)',
                                    font_style="Button",
                                ),
                                MDLabel(
                                    text="Сучасна  молодь  не  розуміє  сенсу  життя  і  його  справжню  цінність.  Своїми проявами  девіантної  поведінки  вони  не  лише  руйнують  своє  здоров’я,  а  й здоров'я  майбутнього  покоління,  своїх  дітей  та  внуків –  майбутнього  нашої нації. (М. Горький)",
                                    font_style="Button",
                                ),
                                MDLabel(
                                    text="Жити  нерозумно,  нестримано –  значить  непогано  жити,  але повільно помирати.  (Демокріт)",
                                    font_style="Button",
                                ),
                                MDLabel(
                                    text="Здорова людина – найдорогоцінніший здобуток природи. (Т. Карлейль)",
                                    font_style="Button",
                                ),
                                MDLabel(
                                    text="Людина  може  жити  до 100  років.  Ми  самі  своєю  безладністю,  своїм жахливим  ставленням  до  власного  організму  зменшуємо  цей  нормальний термін до значно меншої цифри. (І. Павлов)",
                                    font_style="Button",
                                ),
                            padding = [10,60,10,10],
                            rows = 8,
                            ),
                            name = "scr 1",
                        ),
                        MDScreen(
                            VideoPlayer(
                                source = 'video/fe.mp4',
                                options = {'eos': 'stop', 'allow_stretch': False},
                            ),
                            name = "scr 2",
                        ),
                        MDScreen(
                            VideoPlayer(
                                source='video/se.mp4',
                                options={'eos': 'stop', 'allow_stretch': False},
                            ),
                            name="scr 3",
                        ),
                        MDScreen(
                            VideoPlayer(
                                source='video/te.mp4',
                                options={'eos': 'stop', 'allow_stretch': False},
                            ),
                            name="scr 4",
                        ),
                        MDScreen(
                            MDBoxLayout(
                                MDBoxLayout(
                                    MDTextField(
                                        id='search_field',
                                        hint_text='Пошук їжі',
                                        size_hint_x = 0.8,
                                        pos_hint = {'center_y': 0.5}
                                    ),
                                    MDIconButton(
                                        icon='magnify',
                                        pos_hint = {'center_y': 0.5},
                                        on_release=self.food_search
                                    ),

                                    size_hint_y = None,
                                    height = dp(50),
                                    pos_hint = {'top': 0.8},
                                    id="searchbox",
                                ),
                                MDList(
                                    id="container",
                                    adaptive_height = True,
                                    spacing = dp(10)
                                ),
                                id='box',
                                orientation='vertical',
                                padding=20,
                            ),
                            name="scr 5",
                        ),
                        id="screen_manager",
                    ),
                    MDNavigationDrawer(
                        MDNavigationDrawerMenu(
                                MDNavigationDrawerLabel(
                                    text='Головна'
                                ),
                                MDNavigationDrawerItem(
                                    icon="babel",
                                    text="Мотиваційний Пролог",
                                    text_color="#7d7878",
                                    on_press=self.switch_screen,
                                ),

                                MDNavigationDrawerDivider(),

                                MDNavigationDrawerLabel(
                                    text='Вправи'
                                ),
                                MDNavigationDrawerItem(
                                    icon="walk",
                                    text="Легко",
                                    text_color="#7d7878",
                                    on_press=self.switch_screen,
                                ),
                                MDNavigationDrawerItem(
                                    icon="walk",
                                    text="Середньо",
                                    text_color="#7d7878",
                                    on_press=self.switch_screen,
                                ),
                                MDNavigationDrawerItem(
                                    icon="walk",
                                    text="Складно",
                                    text_color="#7d7878",
                                    on_press=self.switch_screen,
                                ),

                                MDNavigationDrawerDivider(),

                                MDNavigationDrawerLabel(
                                    text='FatSecret'
                                ),
                                MDNavigationDrawerItem(
                                    icon="egg-fried",
                                    text="Їжа",
                                    text_color="#7d7878",
                                    on_press=self.switch_screen,
                                ),
                        ),
                        id="nav_drawer",
                        radius=(0, 16, 16, 0),
                    ),
                    id="navigation_layout",
                )
            )
        )

    def food_search(self, *args):
        fs = Fatsecret("b5e9a2a7783a4b76b4f224ceeae4223f", "b0da5f6fa2254beeadad5b3c25ad75f4")
        foods = fs.foods_search(self.root.ids.navigation_layout.ids.screen_manager.get_screen("scr 5").ids.box.ids.searchbox.ids.search_field.text, 1, 1)
        name = foods['food_name']
        self.nutr = foods['food_description']
        md_list = self.root.ids.navigation_layout.ids.screen_manager.get_screen("scr 5").ids.box.ids.container
        md_list.clear_widgets()
        md_list.add_widget(
                OneLineListItem(text=name, on_press=self.food_dialog)
        )
    def food_dialog(self, *args):
        if not self.dialog:
            self.dialog = MDDialog(
                text = self.nutr,
                buttons = [
                    MDFlatButton(
                        text="OK",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_press = self.close_but
                    )
                ],
            )
        else:
            self.dialog.text = self.nutr
        self.dialog.open()

    def close_but(self, *args):
        self.dialog.dismiss()


    def switch_screen(self, instance_list_item: MDNavigationDrawerItem):
        self.root.ids.navigation_layout.ids.screen_manager.current = {
            "Мотиваційний Пролог": "scr 1", "Легко": "scr 2", "Середньо": "scr 3", "Складно": "scr 4", "Їжа": "scr 5"
        }[instance_list_item.text]
        self.root.children[0].ids.nav_drawer.set_state("close")

    def nav_drawer_open(self):
        nav_drawer = self.root.children[0].ids.nav_drawer
        nav_drawer.set_state("open")

if __name__ == "__main__":
    BeFit().run()