from datetime import datetime

import mesa, restaurante
from producto import Bebida, Alimento
from persona import Mesero, Cliente
from menu import Menu

if __name__ == '__main__':
	mesa1 = mesa.Mesa(1, 2)
	mesa2 = mesa.Mesa(2, 4)
	mesa3 = mesa.Mesa(2, 4)
	mesa4 = mesa.Mesa(2, 6)
	alimento1 = Alimento('Chilaquiles', 100, 'Unos ricos chilaquiles', ['huevo', 'crema', 'leche'], 'Vegetariana', 500)
	menu1 = Menu('Desayunos', {alimento1.nombre: alimento1})
	res = restaurante.Restaurante('Soft', 'La Minerva #123', menu1, [mesa1, mesa2, mesa3, mesa4])
	print('El name del restaurante es:', res.nombre)
	print('La direccion del restaurante es:', res.direccion)
	print('El numero de mesa atendida es:', mesa1.numMesa)
	print('Cantidad de personas en la mesa atendida es:', mesa1.cantidadPersona)
	# print('Lista de personas en la mesa atendida es:', mesa1.listaCliente)
	res.abrir()
	cliente1 = Cliente('Marcos', 24, 'Local')
	mesero1 = Mesero('María', 29, 'ojfaoiefjoseif', 'El salto, Colima', datetime.now(), res)
	mesero1.abrirCuenta(mesa1, cliente1)
	mesero1.cobrarCuenta(mesa1)
	res.cerrar()
