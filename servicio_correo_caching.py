from functools import lru_cache
from servicio_correo import ServicioCorreo

class ServicioCorreoConCache(ServicioCorreo):
    def __init__(self, servicio_correo):
        self.servicio_correo = servicio_correo

    @lru_cache(maxsize=None)
    def enviar_correo(self, correo):
        return self.servicio_correo.enviar_correo(correo)

    @lru_cache(maxsize=None)
    def listar_correos(self, inicio, fin):
        return self.servicio_correo.listar_correos(inicio, fin)

    @lru_cache(maxsize=None)
    def descargar_correo(self, info_correo):
        return self.servicio_correo.descargar_correo(info_correo)
