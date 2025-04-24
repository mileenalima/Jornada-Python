# Tela inicial:
    #Título: Hashzap
    #Botão:Iniciar chat
        #quando clicar no botão:
        #abrir um popup/modal/alerta
          #título: bem vindo ao Hashzap
          #caixa de texto: Escreva seu nome no chat
          #Botão: entrar no chat
             #quando clicar no botão 
                  #fechar o popup 
                  #sumir com o título
                  #sumir com o botão iniciar chat
                      #carregar o chat 
                      #carregar o campo de enviar mensagem:"Digite sua mensagem"
                      #botão enviar
                         #quando clicar no botão enviar
                         #enviar a mensagem 
                         #limpar a caixa de mensagem 


#Flask -> criar site
#Django -> criar site 
#Kivy -> criar app
#Tkinter -> criar tela para seus programas 

#flet -> da pra construir tanto o front quanto o back end
#Importar o flat 
import flet as ft #dando apelido ao flet de ft

#Criar um função principal para rodar o seu aplicativo 
def main(pagina):
    #titulo
    titulo = ft.Text("Hashzap")
    #websocket - tunel de comunicação entre dois usuários 

    def enviar_mensagem_tunel(mensagem):
        #executar tudo o q eu quero que aconteça para todos 
        # os usuarios que receberem a mensagem 
        texto = ft.Text(mensagem)
        chat.controls.append(texto)
        pagina.update()

    pagina.pubsub.subscribe(enviar_mensagem_tunel)


    def enviar_mensagem(evento):
        nome_usuario = caixa_nome.value
        texto_campo_mensagem = campo_enviar_mensagem.value
        mensagem = f"{nome_usuario}: {texto_campo_mensagem}"
        pagina.pubsub.send_all(mensagem)
    
        #limpar a caixa de enviar mensagem 
        campo_enviar_mensagem.value = ""
        pagina.update()
    

    campo_enviar_mensagem = ft.TextField(label="Digite aqui sua mensagem", 
                                            on_submit=enviar_mensagem)
    botao_enviar = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)
    linha_enviar = ft.Row([campo_enviar_mensagem, botao_enviar])

    chat = ft.Column()

    


    def entrar_chat(evento):
        #fechar o popup
        popup.open = False
        #sumir com o título
        pagina.remove(titulo)
        #sumir com o botão Iniciar chat
        pagina.remove(botao)
        #carregar o chat
        pagina.add(chat)
        #carregar o campo de enviar mensagem
        #carregar botao enviar 
        pagina.add(linha_enviar)

        #adicionar no chat a mensagem "Fulano entrou no chat"
        nome_usuario = caixa_nome.value
        mensagem = f"{nome_usuario} entrou no chat"
        pagina.pubsub.send_all(mensagem)
        pagina.update()


     #criar o popup
    titulo_popup = ft.Text("Bem vindo ao Hashzap") 
    caixa_nome = ft.TextField(label="Digite seu nome")
    botao_popup = ft.ElevatedButton("Entrar no Chat", on_click=entrar_chat)
    popup = ft.AlertDialog(title=titulo_popup, content=caixa_nome, actions=[botao_popup])




    #botao inicial 
    def abrir_popup(evento):
        pagina.dialog = popup 
        popup.open = True
        pagina.update()
    
    botao = ft.ElevatedButton("Iniciar Chat", on_click=abrir_popup)

    #colocar os elementos na página
    pagina.add(titulo)
    pagina.add(botao)

#executar essa função com o flet 
ft.app(main, view=ft.AppView.WEB_BROWSER)





