campo_enviar_mensagem = ft.TextField(label="Digite aqui sua mensagem", 
                                         on_submit=enviar_mensagem)
botao_enviar = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)
linha_enviar = ft.Row([campo_enviar_mensagem, botao_enviar])

chat = ft.Column()