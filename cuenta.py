class Cuenta():
    def __init__(self,productos: [],total:float):
        self.productos = productos
        self.total = total
    
    def dividirCuenta(personas:int):
        cuentaDividida = total/personas
        print("Cada persona pagará "+cuentaDividida+" pesos")
    
    def pagar():
        print("El total a pagar es: "+total)
    
    def agregarProducto(producto: Producto,cantidad:int):
        if(cantidad == 1):
            print("producto"+producto+"agregado")
        else:
            print(cantidad+" productos " + producto+" agregados")
    
    def quitarProducto(producto: Producto,cantidad:int):
        if(cantidad == 1):
            print("producto "+producto+" eliminado")
        else:
            print(cantidad+" productos " + producto+" eliminados")
