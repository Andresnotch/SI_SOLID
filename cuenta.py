from producto import Producto
class Cuenta():
    def __init__(self,productos: list,total:float):
        self.productos = productos
        self.total = total
    
    def dividirCuenta(self,personas:int) -> None:
        cuentaDividida = self.total/personas
        print("Cada persona pagará "+cuentaDividida+" pesos")
    
    def pagar(self) -> None:
        print("El total a pagar es: "+self.total)
    
    def agregarProducto(self,producto: Producto,cantidad:int):
        if(cantidad == 1):
            print("producto"+str(self.producto)+"agregado")
        else:
            print(cantidad+" productos " + producto+" agregados")
    
    def quitarProducto(self,producto: Producto,cantidad:int):
        if(cantidad == 1):
            print("producto "+str(self.producto)+" eliminado")
        else:
            print(cantidad+" productos " + producto+" eliminados")
