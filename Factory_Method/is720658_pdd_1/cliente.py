import random

from libreria_pruebas import Test, TestFactory


class IntelTest(Test):
	def __init__(self, is_threaded):
		if is_threaded:
			self.process = random.randint(1, 10000)


class DefaultIntelTestFactory(TestFactory):
	def create_test(self, *args, **kwargs) -> IntelTest:
		return IntelTest(False)


class ThreadedIntelTestFactory(TestFactory):
	def create_test(self, *args, **kwargs) -> IntelTest:
		self.create_thread()
		return IntelTest(True)

	def create_thread(self):
		print('Thread Created')

	def assert_true(self, *args, **kwargs) -> bool:
		self.reset_environment()
		return any(i is False for i in args)

	def assert_equal(self, *args, **kwargs) -> bool:
		self.reset_environment()
		return kwargs['a'] == kwargs['b']

	def reset_environment(self):
		print('Resetted environment')


if __name__ == '__main__':
	default_test = DefaultIntelTestFactory().create_test()
	threaded_test = ThreadedIntelTestFactory().create_test()
	default_test.assert_true(True, True, False)
	threaded_test.assert_true(True, True, True)