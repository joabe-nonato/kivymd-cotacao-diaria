from ast import Import
import json
from textwrap import indent
from kivy.clock import Clock
from kivymd.uix.list import OneLineIconListItem
from kivymd.uix.label import MDIcon
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivy.uix.boxlayout import BoxLayout
from typing import List

# ###############################################################
# ## MODAL DIALOGO
# ###############################################################

dialog = None
   
# Modal de mensagems
def Mensagem(self):
        if not dialog:
            dialog = MDDialog(
                text="Discard draft?",
                buttons=[
                    MDFlatButton(
                        text="CANCEL",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                    ),
                    MDFlatButton(
                        text="DISCARD",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                    ),
                ],
            )
        dialog.open()

###############################################################
## CARREGANDO
###############################################################

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

class ConteudoCarregando(BoxLayout):
    pass

# Fechar carregando
def carregando_fechar(self):
        carregando.dismiss()

def Carregando(tempo = 2):        
        
        # Builder.load_string(KVC)

        global carregando
        carregando = None
        if not carregando:
            carregando = MDDialog(
                title= "Carregando",
                type= "custom",                
                content_cls = ConteudoCarregando(),
                buttons=[],
            )
        carregando.open()        
        Clock.schedule_once(carregando_fechar, tempo) 

###############################################################
## DADOS JSON
###############################################################

def NomeArquivoJson(nomea):
    # implementar PATH
    return "{0}.json".format(nomea)

def RecuperarListaJSON(arquivo):
    try:
        listaJson = []
        leitura = open(NomeArquivoJson(arquivo), "r", encoding='utf8')    
        listaJson = json.load(leitura)   
        leitura.close()    
        return listaJson    
    except:
        print('erro em CarregarListaJSON()')
    
def GravarListaJson(lista, nome_arquivo):        
    try:        
        jsn = json.dumps(lista, indent = 4, ensure_ascii=False)    
        gravar = open(NomeArquivoJson(nome_arquivo) ,"w", encoding='utf8')
        gravar.write(jsn)
        gravar.close()
    except:
        print('erro em GravarListaJson()')
    
    
###############################################################
## CLASSES
###############################################################

# class Objeto:
#     id: int
#     codigo: str
#     descricao: str
#     ativo: int

#     def __init__(self, id: int, codigo: str, descricao: str, ativo: int) -> None:
#         self.id = id
#         self.codigo = codigo
#         self.descricao = descricao
#         self.ativo = ativo

class Objeto:
    id: int
    codigo: str
    descricao: str
    ativo: int

    def __init__(self, id: int, codigo: str, descricao: str, ativo: int) -> None:
        self.id = id
        self.codigo = codigo
        self.descricao = descricao
        self.ativo = ativo


class Objetos:
    objeto: List[Objeto]

    def __init__(self, objeto: List[Objeto]) -> None:
        self.objeto = objeto


class Welcome10:
    objetos: Objetos

    def __init__(self, objetos: Objetos) -> None:
        self.objetos = objetos


