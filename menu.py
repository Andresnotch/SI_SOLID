from producto import Producto
class Menu():
    def __init__(self):
        nombreRestaurante: str
        listaProductos: list
    
    def agregarProducto(self,producto: Producto):
        print("producto"+str(self.producto)+"agregado")
    
    def quitarProducto(self,producto: Producto):
        print("producto "+str(self.producto)+" eliminado")
