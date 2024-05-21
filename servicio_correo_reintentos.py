from servicio_correo import ServicioCorreo

class ServicioCorreoConReintentos(ServicioCorreo):
    def __init__(self, servicio_correo):
        self.servicio_correo = servicio_correo
        self.intentos_maximos = 3

    def enviar_correo(self, correo):
        intentos = 0
        while intentos < self.intentos_maximos:
            try:
                self.servicio_correo.enviar_correo(correo)
                break
            except Exception as e:
                intentos += 1

    def listar_correos(self, inicio, fin):
        return self.servicio_correo.listar_correos(inicio, fin)

    def descargar_correo(self, info_correo):
        return self.servicio_correo.descargar_correo(info_correo)
