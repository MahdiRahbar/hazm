
import re
from .utils import u
from nltk.tokenize.api import TokenizerI


class SentenceTokenizer(TokenizerI):
	def __init__(self):
		self.pattern = re.compile(u(r'([!\.\?⸮؟]+)[ \n]+'))

	def tokenize(self, text):
		"""
		>>> tokenizer.tokenize('جدا کردن ساده است. تقریبا البته!')
		['جدا کردن ساده است.', 'تقریبا البته!']
		"""

		text = text.replace('\n', ' ')
		text = self.pattern.sub(r'\1\n', text)
		return [sentence.strip() for sentence in text.split('\n') if sentence]


if __name__ == '__main__':
	import doctest
	doctest.testmod(extraglobs={'tokenizer': SentenceTokenizer()})
