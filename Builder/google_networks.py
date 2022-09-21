from networks import *

if __name__ == '__main__':
	director = NetworkDesigner(SequentialNetworkBuilder())
	seq_network = director.make()
	director.changeBuilder(RecurrentNetworkBuilder())
	rec_network = director.make()
	print(seq_network.name)
	print(rec_network.name)