from text_preprocessing import Text

with open('data/abusive.csv','r') as f:
	abusive = f.read().split('\n')
	abusive = {x.split(',')[0]:x.split(',')[1] for x in abusive}
	AbusiveWord = set(abusive.keys())

class Abusive():

	def __init__(self,text):
		self.first_words = Text(text).first_tokenized
		self.second_words = Text(text).second_tokenized
		self.abusive_word = self.abusiveCheck()
		self.results = self.abusiveCategory()

	def abusiveCheck(self):
		ls = []
		for word in self.first_words:
			if word in AbusiveWord and word not in ls:
				ls.append(word)

		for word in self.second_words:
			if word in AbusiveWord and word not in ls:
				ls.append(word)

		return ls

	def abusiveCategory(self):
		ls = []
		for word in self.abusive_word:
			data_json = {'abusive_word':word,'category':abusive[word]}
			ls.append(data_json)

		return ls