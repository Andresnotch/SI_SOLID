class Mesa:
    def __init__(self, numMesa:int, cantidadPersona:int, listaCliente:int) -> None:
        self.numMesa = numMesa
        self.cantidadPersona = cantidadPersona
        self.listaCliente = []

class Restaurante:
    def __init__(self, nombre:str, direccion:str, mesa:Mesa) -> None:
        self.nombre = nombre
        self.direccion = direccion
        self.mesa = mesa #ASOCIACION -> AGREGACION

    def abirir(self) -> bool:
        print('restaurante abierto')
        #pass

    def cerrar(self) -> bool:
        print('restaurante cerrado')
        #pass

###
mesa1 = Mesa(1, 2, 3)

soft = Restaurante('Soft', 'La Minerva #123', mesa1)
print('El nombre del restaurante es:', soft.nombre)
print('La direccion del restaurante es:', soft.direccion)
print('El numero de mesa atendida es:', mesa1.numMesa)
print('Cantidad de personas en la mesa atendida es:', mesa1.cantidadPersona)
#print('Lista de personas en la mesa atendida es:', mesa1.listaCliente)
soft.abirir()
soft.cerrar()