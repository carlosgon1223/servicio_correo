from abc import ABC, abstractmethod

class ServicioCorreo(ABC):
    @abstractmethod
    def enviar_correo(self, correo):
        pass

    @abstractmethod
    def listar_correos(self, inicio, fin):
        pass

    @abstractmethod
    def descargar_correo(self, info_correo):
        pass
