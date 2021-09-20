from producto import Producto
class Menu():
    def __init__(self):
        nombreRestaurante: str
        listaProductos: list
    
    def agregarProducto(self,producto: Producto):
        print("producto"+str(producto)+"agregado")
    
    def quitarProducto(self,producto: Producto):
        print("producto "+str(producto)+" eliminado")
