class ErrorAplicacion(Exception):
    def __init__(self,mensaje):
        super().__init__("Manejo de errores de la Aplicación: "+mensaje)