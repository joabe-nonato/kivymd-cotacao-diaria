###############################################################
# Criar splash screen
# Recursos: Python, Kivy, kivyMD
# IDE: Visual Core
# Autor: Joabe Nonato
# 02/06/2022
###############################################################
## IMPORTS
###############################################################
import os
from kivy.lang import Builder
from kivy.clock import Clock
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivymd.uix.list import MDList
from kivy.core.window import Window
from App.recursos.dados.data import data as Registros, favoritos

from App.biblioteca import *
from App.Tela01 import *
from App.Tela02 import *

###############################################################
## SET WINDOW SIZE
###############################################################
Window.size = (350, 600)

###############################################################
## MAIN screens
###############################################################

# lista_geral = []
# lista_ativos = []
def TrocarTela(tela):    
    if tela == "Tela01":
        screen_manager.transition.direction = 'right'
    else:
        screen_manager.transition.direction = 'left'
    screen_manager.current = str(tela)

################################################################
class Consulta(Screen):

    def proximaTela(self, tela):
        TrocarTela(str(tela))

    def on_enter(self, *args):        
        # Carregando(3)        
        #listar apenas registros ativos        
        ativos = filter(lambda x: x["ativo"] == "1", favoritos)
        PesquisarRegistros(ativos, self.ids.box, False)

    def pesquisar(self, texto):
         if len(self.ids.box.children) > 0:
            ativos_filtrados = filter(lambda x: x["ativo"] == "1" 
                            and (texto.upper() in x["codigo"].upper() 
                            or texto.upper() in x["descricao"].upper() ) 
                            , favoritos)
            PesquisarRegistros(ativos_filtrados, self.ids.box, False)
        
class Configura(Screen):
    def on_enter(self, *args):
        # Carregando(5)        
        listarRegistros(lista_geral, self.ids.box, True)
        
    # def on_pre_leave(self, *args):
    #     tst = []
    #     tst = self.ids.box.children
    #     for t in tst:
    #         print(t)
    
    def proximaTela(self, tela):
        TrocarTela(str(tela))

    def pesquisar(self, texto):
        Pesquisar(texto, self.ids.box, True, lista_geral)
   

KVC = """
<ConteudoCarregando>
    orientation: "vertical"
    spacing: "12dp"
    size_hint_y: None
    height: "30dp"

    MDSpinner:
        size_hint: None, None
        size: "23dp", "23dp"
        pos_hint: {'center_x': 0.5, 'center_y': 0.5}
        active: True
"""   
###############################################################
## MAIN CLASS
###############################################################
class MainApp(MDApp):
    # Global screemanager variable
    global screen_manager
    screen_manager = ScreenManager()
    
    global dialog
    dialog = None
    ###############################################################
    ## BUILD FUNCTION
    ###############################################################
    def build(self):
        Builder.load_string(KVC)
        # Set App Title
        self.title = "Cotaçã Diaria"
        
        # Set App Theme
        self.theme_cls.primary_palette = "Orange"
        
        # Load kv screen files to builder
        screen_manager.add_widget(Builder.load_file(os.path.join(os.getcwd(), "App\Tela00.kv")), name = "Tela00")        
        screen_manager.add_widget(Builder.load_file(os.path.join(os.getcwd(), "App\Tela01.kv")), name = "Tela01")
        screen_manager.add_widget(Builder.load_file(os.path.join(os.getcwd(), "App\Tela02.kv")), name = "Tela02")
                
        # Return Screen Manager
        return screen_manager

    ###############################################################
    ## TIMER TO CHANGE SCREEN
    ###############################################################
    def on_start(self):        
        Clock.schedule_once(self.change_screen, 5)        
        
        #CARREGAR BASE OU API
        global lista_geral        
        lista_geral = RecuperarListaJSON("base")
        # global lista_ativos
        # lista_ativos = filter(lambda x: x["ativo"] == "1", lista_geral)
        # print(len(lista_geral))        
        
    ###############################################################
    ## CHANGE SCREEN
    ###############################################################        
    def change_screen(self, dt):
        TrocarTela("Tela01")        
        # print(screen_manager.ids)

###############################################################
## RUM APP
###############################################################
MainApp().run()