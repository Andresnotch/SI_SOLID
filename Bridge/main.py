from pynput import keyboard
from spiderverse import SpiderMan, Earth616, Earth1610

game = {
	'chars': [SpiderMan(Earth616()), SpiderMan(Earth1610())],
	'selected': 0
}


def on_press(key):
	if hasattr(key, 'char'):
		print(key.char)
		if key.char == 'c':
			if game['selected']:
				game['selected'] = 0
			else:
				game['selected'] = 1
			print(f'Changed to {game["chars"][game["selected"]].supername} ({game["chars"][game["selected"]].name})')
		elif key.char == 'j':
			game["chars"][game["selected"]].attack()
		elif key.char == 'k':
			game["chars"][game["selected"]].special()
		elif key.char == 'l':
			game["chars"][game["selected"]].gadget()
		else:
			print('input c to change characters, j for attack, k for special, l for gadget')
	else:
		print('input c to change characters, j for attack, k for special, l for gadget')


def on_release(key):
	if key == keyboard.Key.esc:
		# Stop listener
		return False


if __name__ == '__main__':
	listener = keyboard.Listener(
		on_press=on_press,
		on_release=on_release)
	listener.start()
	while True:
		pass
