from kivymd.app import MDApp

from kivy.properties import ObjectProperty
from kivy.uix.videoplayer import VideoPlayer

from kivymd.uix.navigationdrawer import (MDNavigationLayout,
    MDNavigationDrawer,
    MDNavigationDrawerMenu,
    MDNavigationDrawerLabel,
    MDNavigationDrawerDivider,
    MDNavigationDrawerItem,
)
from kivymd.uix.screen import MDScreen
from kivymd.uix.screenmanager import MDScreenManager
from kivymd.uix.scrollview import MDScrollView
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.label import MDLabel

# import requests
# from fatsecret import Fatsecret
#
# response = requests.get("https://platform.fatsecret.com/rest/server.api")
# fs = Fatsecret("b5e9a2a7783a4b76b4f224ceeae4223f", "b0da5f6fa2254beeadad5b3c25ad75f4")
# foods = fs.foods_search("Spaghetti")
# print(foods)

class ContentNavigationDrawer(MDScrollView):
    screen_manager = ObjectProperty()
    nav_drawer = ObjectProperty()

class BeFit(MDApp):
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
                            MDLabel(
                                text = "Головна",
                                halign = "center",
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
                            MDLabel(
                                text="Їжа",
                                halign="center",
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