from cgitb import text
from distutils.command.build import build
from kivy.clock import Clock
from kivymd.uix.list import ThreeLineIconListItem
from kivymd.uix.label import MDIcon
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from http import client
import json
from datetime import datetime

# ###############################################################
# ## REQUEST API
# ###############################################################

def ValorAtivo(codigo, urlApi = 'economia.awesomeapi.com.br'):
    try:
        moeda = '/json/last/{0}'.format(codigo)
        global data_retorno        
        conn = client.HTTPSConnection(urlApi)
        conn.request('GET', moeda)        
        r = conn.getresponse()                
        data_retorno = r.read()
        conn.close()

        if r.status == 200:
            return data_retorno
        else:
            return ""
    except:
        print("Erro ao executar: ValorAtivo() ")

def RecuperarDicionario(codigo):
    try:
        existe = ValorAtivo(codigo)
        if len(existe) > 0:
            jsn = json.loads(existe)
            codigo_root = "{0}BRL".format(codigo)    
            valor_node = jsn.get(codigo_root)
            
            if len(valor_node) > 0:
                return valor_node
    except:
        print("Erro ao executar RecuperarDicionario()")
        return ""

# print(RecuperarDicionario("RSD"))

###############################################################

dialog = None
   
# Listar registros de ambas as telas
def PesquisarRegistros(lista, box, editar):
    box.clear_widgets()
    
    for registro in lista:        
        
        resultado = RecuperarDicionario(registro["codigo"])        
        # atualizado = datetime.strptime(resultado.get('create_date'), "%Y-%m-%d %H:%M")

        try:
            item = ThreeLineIconListItem(            
                text = "{0}: {1}".format(registro["codigo"], resultado.get('name')),
                secondary_text = "Max: {0} Min: {1}".format(resultado.get('high'), resultado.get('low')) ,
                tertiary_text = "{0}".format(resultado.get('create_date')) ,
                pos_hint= {'center_y': 0.5}
            )
            # icone esquerdo
            item.add_widget(MDIcon(
                icon = "cash-multiple",
                size_hint= (None, None),
                size= (25,25),
                pos_hint= {'center_x': 0.1, 'center_y': 0.5}
            ))        
            # imagem_botao = "trash-can-outline"
            # if editar:
            #     if registro["ativo"] == "1":            
            #         imagem_botao = "checkbox-marked"
            #     else:
            #         imagem_botao = "checkbox-blank-outline"                            
            #icone direito
            item.add_widget(MDIcon(
                icon = "heart",
                size_hint = (None, None),
                size = (25,25),
                pos_hint = {'center_x': 0.9,'center_y': 0.5},
                theme_text_color = "Custom",
                # text_color = (0.7, 0.7, 0.7, 1),            
            ))
            box.add_widget(item)
        except:
            print("Erro ao executar - listarRegistros() = código: {0}".format(registro["codigo"]))

# Pesquisar (Atualmente usado somente o configurar)
def Pesquisar(texto, box, editar, Registros):
    if len(box.children) > 0:
        resultado = filter(lambda x: texto in x["codigo"] 
                            or texto in x["descricao"] 
                            , Registros)
        
        PesquisarRegistros(resultado, box, editar)
    else:
        PesquisarRegistros(Registros, box, editar)
