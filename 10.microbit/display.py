from pixel import Pixel, PixelPower
from time import sleep_ms

PixelPower(True)

CharData = {
	'!': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	'"': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0],
	'#': [0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0],
	'$': [0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
	'%': [1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1],
	'&': [0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
	"'": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
	'(': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0],
	'@': [0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0],
	')': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
	'*': [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
	'+': [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
	',': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
	'-': [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
	'.': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
	'/': [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
	'0': [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0],
	'1': [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
	'2': [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1],
	'3': [0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0],
	'4': [0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0],
	'5': [1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1],
	'6': [0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0],
	'7': [1, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1],
	'8': [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0],
	'9': [0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0],
	':': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
	';': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
	'<': [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
	'=': [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0],
	'>': [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
	'?': [0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0],
	'A': [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1],
	'B': [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1],
	'C': [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0],
	'D': [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1],
	'E': [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1],
	'F': [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1],
	'G': [0, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0],
	'H': [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1],
	'I': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1],
	'J': [1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0],
	'K': [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1],
	'L': [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
	'M': [1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1],
	'N': [1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1],
	'O': [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0],
	'P': [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1],
	'Q': [0, 0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0],
	'R': [0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1],
	'S': [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
	'T': [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
	'U': [0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0],
	'V': [1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0],
	'W': [1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1],
	'X': [0, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1],
	'Y': [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
	'Z': [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1],
	'[': [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
	"\\": [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0],
	']': [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0],
	'^': [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
	'_': [0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
	'`': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	'a': [0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0],
	'b': [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1],
	'c': [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0],
	'd': [0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0],
	'e': [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0],
	'f': [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0],
	'g': [0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0],
	'h': [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1],
	'i': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0],
	'j': [0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
	'k': [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1],
	'l': [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
	'm': [0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1],
	'n': [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1],
	'o': [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0],
	'p': [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1],
	'q': [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0],
	'r': [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1],
	's': [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
	't': [0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
	'u': [0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0],
	'v': [0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0],
	'w': [0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1],
	'x': [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1],
	'y': [0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1],
	'z': [0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1],
	'{': [0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
	'|': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
	'}': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1],
	'~': [0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
	' ': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
}

black = [0, 0, 0]
Red = [2, 0, 0]
Orange = [2, 1, 0]
Yellow = [2, 2, 0]
Green = [0, 2, 0]
Blue = [0, 0, 2]
Indigo = [0, 2, 2]
Purple = [2, 0, 2]

Zero = [black]*5

class Image:
	def __init__(self, str):
		self.tem = [0]*25
		self.seq = [20, 15, 10, 5, 0, 21, 16, 11, 6, 1, 22, 17,
					12, 7, 2, 23, 18, 13, 8, 3, 24, 19, 14, 9, 4]
		self.num = 0
		it = iter(self.seq)
		for val in str:
			if val != ':':
				self.tem[next(it)] = int(val)

	def __iter__(self):
		self.num = 0
		return self  # 实例本身就是迭代对象，故返回自己

	def __next__(self):
		value = self.tem[self.num]
		self.num += 1
		return value  # 返回下一个值

	HEART = [0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1,
			 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0]
	HEART_SMALL = [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0,
				   0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0]
	HAPPY = [0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0,
			 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0]
	SMILE = [0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0,
			 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0]
	SAD = [0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0,
		   0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1]
	CONFUSED = [0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0,
				0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1]
	ANGRY = [1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 0,
			 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1]
	ASLEEP = [0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0,
			  0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0]
	SURPRISED = [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0,
				 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0]
	SILLY = [1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0,
			 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0]
	FABULOUS = [1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1,
				0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0]
	MEH = [0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0,
		   0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0]
	YES = [0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
		   0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0]
	NO = [1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0,
		  1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1]
	CLOCK12 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1,
			   1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
	CLOCK11 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
			   0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0]
	CLOCK10 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
			   0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0]
	CLOCK9 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
			  0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0]
	CLOCK8 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
			  0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0]
	CLOCK7 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
			  0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0]
	CLOCK6 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
			  0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
	CLOCK5 = [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0,
			  0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
	CLOCK4 = [0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0,
			  0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
	CLOCK3 = [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0,
			  0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
	CLOCK2 = [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0,
			  0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
	CLOCK1 = [0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0,
			  0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
	ARROW_N = [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1,
			   1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0]
	ARROW_NE = [1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1,
				0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1]
	ARROW_E = [0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1,
			   0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0]
	ARROW_SE = [0, 0, 1, 1, 1, 0, 0, 0, 1, 1, 0,
				0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0]
	ARROW_S = [0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1,
			   1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0]
	ARROW_SW = [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
				0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1]
	ARROW_W = [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1,
			   0, 1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0]
	ARROW_NW = [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1,
				0, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0]
	TRIANGLE = [0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0,
				1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0]
	TRIANGLE_LEFT = [0, 0, 0, 0, 1, 0, 0, 0, 1, 1,
					 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1]
	CHESSBOARD = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0,
				  1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]
	DIAMOND = [0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1,
			   0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0]
	DIAMOND_SMALL = [0, 0, 0, 0, 0, 0, 0, 1, 0, 0,
					 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
	SQUARE = [1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1,
			  0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1]
	SQUARE_SMALL = [0, 0, 0, 0, 0, 0, 1, 1, 1, 0,
					0, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0]
	RABBIT = [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1,
			  1, 1, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1]
	COW = [1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 0,
		   1, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 0]
	MUSIC_CROTCHET = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
					  1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1]
	MUSIC_QUAVER = [0, 0, 1, 0, 0, 0, 1, 0, 0, 0,
					1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1]
	MUSIC_QUAVERS = [1, 1, 1, 1, 1, 1, 0, 0, 1, 1,
					 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1]
	PITCHFORK = [1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 1,
				 1, 1, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0]
	XMAS = [0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1,
			1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1]
	PACMAN = [1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1,
			  0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0]
	TARGET = [0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1,
			  1, 0, 1, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0]
	TSHIRT = [1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0,
			  1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0]
	ROLLERSKATE = [1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0,
				   0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 1, 0]
	DUCK = [0, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1,
			1, 1, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0]
	HOUSE = [0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1,
			 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0]
	TORTOISE = [0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0,
				1, 1, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0]
	BUTTERFLY = [1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0,
				 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1]
	STICKFIGURE = [0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1,
				   1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1]
	GHOST = [1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1,
			 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1]
	SWORD = [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1,
			 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]
	GIRAFFE = [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0,
			   0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0]
	SKULL = [0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1,
			 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0]
	UMBRELLA = [0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1,
				1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0]
	SNAKE = [0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0,
			 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0]
	ALL_CLOCKS = [CLOCK12, CLOCK1, CLOCK2, CLOCK3, CLOCK4, CLOCK5,
				  CLOCK6, CLOCK7, CLOCK8, CLOCK9, CLOCK10, CLOCK11]
	ALL_ARROWS = [ARROW_N, ARROW_NE, ARROW_E,
				  ARROW_SE, ARROW_S, ARROW_SW, ARROW_W, ARROW_NW]


class Display:
	def __init__(self):
		self.Led = Pixel()
		self.tem = [[0, 0, 0]]*25  # 显示缓存区m=

	def Disrupt_Col(color):
		a = color[-1]
		while True:
			if color_num != 1:
				import random
				random.shuffle(color)
				if a != color[0]:
					break

	def scroll(self, val, color=Red, delay=150):
		pixel_col = [[0, 0, 0]]*25  # 显示缓存区m=
		val = str(val) + ' '
		color_num = 1
		if color != Red:
			if isinstance(color[0], list):
				color_num = len(color)
		# self.Disrupt_Col(color) #打乱颜色顺序
		col_cnt = 0
		it = iter(color)
		for val1 in val:
			val2 = CharData[val1]

			if color_num == 1:
				now_col = color
			else:
				if col_cnt < color_num:
					now_col = next(it)  # 确定当前字符的颜色
				else:
					col_cnt = 0
					it = iter(color)
					now_col = next(it)
				col_cnt += 1

			for i in range(25):  # 为字符的像素点添加颜色
				if val2[i] == 1:
					pixel_col[i] = now_col
				else:
					pixel_col[i] = [0, 0, 0]

			for i in range(6):  # 开始滚动显示
				for t in range(4):
					self.tem[20 - (t * 5):20 - (t * 5) + 5] = self.tem[20 -
																	   ((t + 1) * 5):20 - ((t + 1) * 5) + 5]
					# 数据向前移动5位
				if i == 5:
					self.tem[0:5] = Zero[0:5]  # 每个字符之间间隔一行
				else:
					self.tem[0:5] = pixel_col[20 - (i * 5):20 - (i * 5) + 5]
				for r in range(25):
					self.Led.LoadPos(r, self.tem[r])  # 亮度为0
				self.Led.Show()
				sleep_ms(delay)

	def clear(self):
		self.Led.fill((0, 0, 0))
		self.Led.Show()

	def __show(self, it, color):
		it = iter(it)
		for r in range(25):
			col=next(it)
			self.Led.LoadPos(r, color if col else black)
		self.Led.Show()

	def show(self, images, color=Red,*, loop=False, delay=500):
		if isinstance(images, str):
			images = CharData[images]
		if isinstance(images, list) and (isinstance(images[0], Image) or isinstance(images[0], list)):
			for i in images:
				self.__show( i, color)
				sleep_ms(delay)
			try:
				while loop:
					for i in images:
						self.__show( i, color)
						sleep_ms(delay)
			except Exception as e:
				self.Led.fill((0, 0, 0))
				self.Led.Show()

		else:
			it = iter(images)
			self.__show(it,color)
			try:
				while loop:
					self.__show(it, color)
			except Exception as e:
				self.Led.fill((0, 0, 0))
				self.Led.Show()

def unit_test():
	print('The unit test code is as follows')
	print('\n\
	display = Display()\n\
	boat1 = Image("05050:"\n\
				"05050:"\n\
				"05050:"\n\
				"99999:"\n\
				"09990")\n\
	boat2 = Image("00000:"\n\
				"05050:"\n\
				"05050:"\n\
				"05050:"\n\
				"99999")\n\
	boat3 = Image("00000:"\n\
				"00000:"\n\
				"05050:"\n\
				"05050:"\n\
				"05050")\n\
	boat4 = Image("00000:"\n\
				"00000:"\n\
				"00000:"\n\
				"05050:"\n\
				"05050")\n\
	boat5 = Image("00000:"\n\
				"00000:"\n\
				"00000:"\n\
				"00000:"\n\
				"05050")\n\
	boat6 = Image("00000:"\n\
				"00000:"\n\
				"00000:"\n\
				"00000:"\n\
				"00000")\n\
   all_boats = [boat1, boat2, boat3, boat4, boat5, boat6]\n\
	display.scroll(\'hello,world\', Yellow)\n\
	sleep_ms(1000)\n\
	display.scroll(454545)\n\
	sleep_ms(1000)\n\
	display.scroll(\'Goodbye-My-Loneliness\', [Purple, Yellow, Green, Blue])\n\
	sleep_ms(1000)\n\
	display.show(all_boats,Yellow)\n\
	sleep_ms(1000)\n\
	display.clear()\n\
	display.show(boat1,Purple)\n\
	sleep_ms(1000)\n\
	display.clear()\n\
	sleep_ms(1000)\n\
	display.show(\'9\',Green)\n\
	sleep_ms(1000)\n\
	display.show(Image.DUCK)\n\
	sleep_ms(1000)\n\
	display.show(Image.DIAMOND)\n\
	sleep_ms(1000)\n\
	display.show(Image.SILLY)\n\
	sleep_ms(1000)\n\
	display.show(Image.ALL_CLOCKS,Orange)\n\
	sleep_ms(1000)\n\
	display.show(Image.ALL_ARROWS,Blue)\n\
	sleep_ms(1000)\n\
	display.clear()\n\
	')
	display = Display()
	boat1 = Image("05050:"
				  "05050:"
				  "05050:"
				  "99999:"
				  "09990")

	boat2 = Image("00000:"
				  "05050:"
				  "05050:"
				  "05050:"
				  "99999")

	boat3 = Image("00000:"
				  "00000:"
				  "05050:"
				  "05050:"
				  "05050")

	boat4 = Image("00000:"
				  "00000:"
				  "00000:"
				  "05050:"
				  "05050")

	boat5 = Image("00000:"
				  "00000:"
				  "00000:"
				  "00000:"
				  "05050")

	boat6 = Image("00000:"
				  "00000:"
				  "00000:"
				  "00000:"
				  "00000")

	all_boats = [boat1, boat2, boat3, boat4, boat5, boat6]
	display.scroll('hello,world', Yellow)
	sleep_ms(1000)
	display.scroll(454545)
	sleep_ms(1000)
	display.scroll('Goodbye-My-Loneliness', [Purple, Yellow, Green, Blue])
	sleep_ms(1000)
	display.show(all_boats,Yellow)
	sleep_ms(1000)
	display.clear()
	display.show(boat1,Purple)
	sleep_ms(1000)
	display.clear()
	sleep_ms(1000)
	display.show('9',Green)
	sleep_ms(1000)
	display.show(Image.DUCK)
	sleep_ms(1000)
	display.show(Image.DIAMOND)
	sleep_ms(1000)
	display.show(Image.SILLY)
	sleep_ms(1000)
	display.show(Image.ALL_CLOCKS,Orange)
	sleep_ms(1000)
	display.show(Image.ALL_ARROWS,Blue)
	sleep_ms(1000)
	display.clear()


if __name__ == '__main__':
	unit_test()
