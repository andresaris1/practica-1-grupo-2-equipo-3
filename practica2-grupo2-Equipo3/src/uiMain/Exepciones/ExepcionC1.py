from ErrorAplicacion import ErrorAplicacion
class ExepcionC1(ErrorAplicacion):
    def __init__(self,mensaje):
        super().__init__("Error C1 ->  "+mensaje)

