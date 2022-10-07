###############################################################
# Criar recurso HOT RELOAD
# Recursos: Python, Kivy, kivyMD
# IDE: Visual Core
# Autor: Joabe Nonato
# 02/06/2022
# Descrição: Esse recurso permite a pré-visualização da tela
# e exibe os erros, durante a codificação.
###############################################################
## IMPORTS
###############################################################
import os
from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
###############################################################
class Consulta(Screen):
    ...

class Configura(Screen):
    ...
###############################################################
## SET WINDOW SIZE
###############################################################
Window.size = (350, 600)

KV = """
#:import HotReloadViewer kivymd.utils.hot_reload_viewer.HotReloadViewer

BoxLayout:

    HotReloadViewer:
        size_hint_x: 0.3
        path: app.path_to_kv_file
        errors: True
        errors_text_color: 1, 0, 0, 1
        errors_background_color: app.theme_cls.bg_light
"""

###############################################################
## MAIN CLASS
###############################################################
class HotReloadApp(MDApp):
    ###############################################################
    ## SET KV TO HOTRELOAD
    ###############################################################
    path_to_kv_file = os.path.join(os.getcwd(), "App\Carregando.kv")

    def build(self):
        self.title = "OrangeRed - IT (HOT RELOAD)"
        self.theme_cls.theme_style = "Light"
        return Builder.load_string(KV, name="MainScreen")

    def update_kv_file(self, text):
        with open(self.path_to_kv_file, "w") as kv_file:
            kv_file.write(text)

HotReloadApp().run()