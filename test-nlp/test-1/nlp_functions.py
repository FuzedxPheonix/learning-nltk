import nltk, re, pprint
from nltk import word_tokenize

def test_connect():
	"""
	prints to make sure file is connect
	"""
	print("Connected")


class NLP_TEST_FILE:
	"""docstring for NLP_TEST_FILE"""
	def __init__(self, arg):
		self.text_file = arg
		self.tokens = None
		self.raw_string = open(self.text_file, 'rU', encoding="ISO-8859-1").read()

	def tokenize_raw_file(self):
		"""
		Follow URL : https://stackoverflow.com/questions/19699367/unicodedecodeerror-utf-8-codec-cant-decode-byte
		"""
		self.tokens = word_tokenize(self.raw_string)

	def print_type(self):
		print(type(self.tokens))

	def print_init(self):
		print("Text file: ", self.text_file)
		print("Tokens: ", self.tokens)

	def freq_words(self, min=1, num=10):
		freqdist = nltk.FreqDist(t for t in self.tokens if len(t) >= min)
		return freqdist.most_common(num)
