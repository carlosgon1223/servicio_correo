import logging
from servicio_correo import ServicioCorreo

class ServicioCorreoConLogging(ServicioCorreo):
    def __init__(self, servicio_correo):
        self.servicio_correo = servicio_correo
        self.logger = logging.getLogger('ServicioCorreo')
        self.logger.setLevel(logging.INFO)

    def enviar_correo(self, correo):
        self.logger.info('Enviando correo...')
        self.servicio_correo.enviar_correo(correo)

    def listar_correos(self, inicio, fin):
        self.logger.info('Listando correos...')
        return self.servicio_correo.listar_correos(inicio, fin)

    def descargar_correo(self, info_correo):
        self.logger.info('Descargando correo...')
        return self.servicio_correo.descargar_correo(info_correo)
