import logging
import os

DIR_LOG = os.path.join(".", "log")

def configurar_logger():
    os.makedirs(DIR_LOG, exist_ok=True) # Crea el directorio de registro si no existe.
    log_programa = "paraules"
    # Formato del registro que incluye la fecha, nombre del logger, nivel de registro y mensaje.
    log_formato = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    log_nivel = logging.DEBUG
    log_modo = 'a'
    log_archivo = os.path.join(DIR_LOG, 'paraules.log') # Configura el sistema de registro básico.
    logging.basicConfig(level=log_nivel, format=log_formato, filename=log_archivo, filemode=log_modo)
    return logging.getLogger(log_programa)

def info_log():
    logger = configurar_logger()
    logger.info("Programa iniciado")

def error_log(e, archivo):
    logger = configurar_logger()
    logger.error("Archivo: " + archivo + str(e))

def final_log(duracion):
    logger = configurar_logger()
    duracion_str = "{:.2f}".format(duracion) # Formatea la duración a dos decimales.
    # Registra un mensaje de información sobre la finalización del programa junto con la duración.
    logger.info("Programa finalizado, tardó " + str(duracion_str) + " segundos")
