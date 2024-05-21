from servicio_correo import ServicioCorreo
from servicio_correo_reintentos import ServicioCorreoConReintentos
from servicio_correo_thread_safe import ServicioCorreoThreadSafe
from servicio_correo_logging import ServicioCorreoConLogging
from servicio_correo_caching import ServicioCorreoConCache

# Creamos una instancia del servicio de correo original
class ServicioCorreoOriginal(ServicioCorreo):
    def enviar_correo(self, correo):
        print("Enviando correo:", correo)

    def listar_correos(self, inicio, fin):
        print("Listando correos desde", inicio, "hasta", fin)

    def descargar_correo(self, info_correo):
        print("Descargando correo:", info_correo)

servicio_correo_original = ServicioCorreoOriginal()

# Creamos las instancias de las clases extendidas
servicio_con_reintentos = ServicioCorreoConReintentos(servicio_correo_original)
servicio_thread_safe = ServicioCorreoThreadSafe(servicio_correo_original)
servicio_con_logging = ServicioCorreoConLogging(servicio_correo_original)
servicio_con_cache = ServicioCorreoConCache(servicio_correo_original)

# Probamos cada instancia llamando a los métodos correspondientes
print("Probando Servicio con Reintentos:")
servicio_con_reintentos.enviar_correo("Correo de prueba")

print("\nProbando Servicio Thread-Safe:")
servicio_thread_safe.listar_correos(1, 10)

print("\nProbando Servicio con Logging:")
servicio_con_logging.descargar_correo("Correo importante")

print("\nProbando Servicio con Cache:")
servicio_con_cache.enviar_correo("Correo con cache")
