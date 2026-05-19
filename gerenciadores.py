from Domínios import Notificacao

class GerenciadorNotificacoes:
    def __init__(self):
        #sem banco de dados ainda
        self._notificacoes_por_usuario = {}

    def adicionar_notificacao(self, usuario_destino, remetente, tipo): 
        nova_notif = Notificacao(remetente, tipo) 

        #sem banco de dados ainda
        if usuario_destino not in self._notificacoes_por_usuario:
            self._notificacoes_por_usuario[usuario_destino] = []
        
        self._notificacoes_por_usuario[usuario_destino].append(nova_notif)
        print(f"[central notif] Alerta de {tipo} para {usuario_destino}")
    
    def buscar_pendentes(self, usuario):
        #mostra as notificaçoes nao lidas
        #sem banco 
        if usuario not in self._notificacoes_por_usuario:
            return []
        return[n for n in self._notificacoes_por_usuario[usuario] if not n.lida]
    
    def marcar_todas_como_lidas(self, usuario):
        #muda o status de notificaçoes para lidas
        #sem banco
        if usuario in self._notificacoes_por_usuario:
            for notif in self._notificacoes_por_usuario[usuario]:
                notif.lida = True
            print(f"[central notif] alertas de {usuario} marcados como lidos")