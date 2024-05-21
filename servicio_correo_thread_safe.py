from threading import Lock
from servicio_correo import ServicioCorreo

class ServicioCorreoThreadSafe(ServicioCorreo):
    def __init__(self, servicio_correo):
        self.servicio_correo = servicio_correo
        self.lock = Lock()

    def enviar_correo(self, correo):
        with self.lock:
            self.servicio_correo.enviar_correo(correo)

    def listar_correos(self, inicio, fin):
        with self.lock:
            return self.servicio_correo.listar_correos(inicio, fin)

    def descargar_correo(self, info_correo):
        with self.lock:
            return self.servicio_correo.descargar_correo(info_correo)
