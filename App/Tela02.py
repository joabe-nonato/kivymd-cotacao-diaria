from kivymd.uix.list import OneLineAvatarIconListItem
from kivymd.uix.label import MDIcon
from kivymd.uix.selectioncontrol import MDCheckbox

def AdicionarRemover(chckbox):
    Selecionados.append(chckbox)

    for p in Selecionados:
        print(p)

# Listar registros de ambas as telas
def listarRegistros(lista, box, editar):
    box.clear_widgets()
    
    global Selecionados 
    Selecionados = []

    for registro in lista:       
            r = registro["codigo"]
        # try:
            item = OneLineAvatarIconListItem(            
                text = registro["codigo"],               
                pos_hint= {'center_y': 0.5},
                on_release= lambda x: AdicionarRemover(r)
            )
            # icone esquerdo
            item.add_widget(MDIcon(
                icon = "cash-multiple",
                size_hint= (None, None),
                size= (25,25),
                pos_hint= {'center_x': 0.1, 'center_y': 0.5},                
            ))    
            # item.add_widget(MDIcon(
            #     icon = "heart-outline",
            #     size_hint = (None, None),
            #     size = (25,25),
            #     pos_hint = {'center_x': 0.9,'center_y': 0.5},
            #     theme_text_color = "Custom",
            #     # text_color = (0.7, 0.7, 0.7, 1),            
            # ))
            item.add_widget(
                MDCheckbox(
                size_hint = (None, None),
                size = (25,25),
                pos_hint = {'center_x': 0.9,'center_y': 0.5},
                # on_active = on_checkbox_active(registro)
            ))

            box.add_widget(item)
        # except:
        #     print("Erro ao executar - listarRegistros() = código: {0}".format(registro["codigo"]))

# Pesquisar (Atualmente usado somente o configurar)
def Pesquisar(texto, box, editar, Registros):
    listaConsulta = []
    if len(box.children) > 0:
        resultado = filter(lambda x: texto in x["codigo"] 
                            or texto in x["descricao"] 
                            , Registros)
        # for item in Registros:
        #     if texto.upper() in item["text"].upper():
        #         listaConsulta.append(item)
        listarRegistros(resultado, box, editar)
    else:
        listarRegistros(Registros, box, editar)
