import random

from Abstract_Test import Test, TestFactory


class GPUTest(Test):
	def __init__(self, CUDA, vector):
		self.CUDA_OK = True
		if CUDA['parallel']:
			for i in CUDA:
				if i.TEST(vector):
					self.CUDA_OK = False

	def is_true(self, int1,int2) -> bool:
		if int1 == int2:
			return True


class NVIDIATestFactory(TestFactory):
	def add_test(self, microtype) -> GPUTest:
		return GPUTest({'parallel': 1}, (1, 1, 2))


