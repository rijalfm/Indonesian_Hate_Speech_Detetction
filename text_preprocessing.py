from nltk import word_tokenize
import re, string
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
factory = StemmerFactory()
stemmer = factory.create_stemmer()

# clean = clean.translate(str.maketrans("","",string.punctuation)).strip()

DICTIONARY_PATH = 'data/salng_dict.csv'
STOPWORD_PATH = 'data/stopword.txt'
ROOT_WORDS_PATH = 'data/kamus-kata-dasar.csv'

with open(STOPWORD_PATH, 'r') as f:
	stop_word = f.read().split('\n')
	stop_word = set([x.lower().strip() for x in stop_word])

with open(ROOT_WORDS_PATH, 'r') as f:
	root_words = f.read().split('\n')
	root_words = set([x.lower().strip() for x in root_words])

with open(DICTIONARY_PATH, 'r') as f:
	data_kamus = f.read().split('\n')
	data_kamus = data_kamus[1:-1]

# Unecessary word can be replaced OR optional stopword that will remove
noise = set(['user','hm','aa','se','a','sih','b','c','vid','uffff','per','us','apa-apa','hmm','hmmm','lah','fb','ig',
						'nah','lho','btw','ahayyyy','ww','tuh','nic','meter','ugh','covid','ac','via','gapapa','corona',
						'korona','guisss','hyung','masama','mah','h','dll','wfh','lockdown','new','eh','deh','ala','ah','bucin',
						'ehmm','ngemall','gaes','ukt','uwu','uwuwu','mall','bioskop','yt','an',
						'dong','fbn','nih','dkk','pdip','pks','gerindra','psi','demokrat','partai','d','e','f','g','h','i','j',
						'k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','ha','wk','he','wak','kok','guyss','ahy',
						'hu','iya'])

stop_word.update(noise)
kamus = {}
for data in data_kamus:
	data = data.split(',')
	kamus[data[0]] = data[1]

DictKeys = set(kamus.keys())

class Text():

	
	def __init__(self,text):
		self.text = str(text)
		self.text_lower = self.text.lower() #
		self.cleaned_text = self.clean_text(self.text_lower)
		self.first_tokenized = word_tokenize(self.text_lower) #
		self.new_text = self.formalisasi()
		self.stemmed_text = stemmer.stem(self.clean_text(self.new_text)) #
		self.second_tokenized = word_tokenize(self.stemmed_text) #
		self.final_tokenized = self.root_checker(self.second_tokenized) #
		self.final_text = ' '.join(self.final_tokenized) #

	
	def formalisasi(self):
		newText = self.text_lower
		
		for word in self.first_tokenized:
			if word in DictKeys:
				newText = newText.replace(word, kamus[word])
		
		return newText

	
	def clean_text(self,text):
		clean = re.sub(r'http([a-z0-9\/\?\&\%\:\.\=]+)',' ',text)		# URL remover
		clean = re.sub(r'pic\.([a-z0-9\/\?\&\%\:\.\=]+)',' ',clean)					# Picture URL remover
		clean = re.sub(r'#([a-z0-9_-]+)',' ',clean)													# Hashtag remover
		clean = re.sub(r'@([a-z0-9_-]+)',' ',clean)													# Mention remover
		clean = re.sub(r'[^\x00-\x7F]+',' ',clean)													# Clear not ascii character
		# Specific text remover
		clean = re.sub(r'hehe',' ',clean)
		clean = re.sub(r'hehe([a-z]+)',' ',clean)
		clean = re.sub(r'wkwk','',clean)
		clean = re.sub(r'wkwk([a-z]+)',' ',clean)
		clean = re.sub(r'haha','',clean)
		clean = re.sub(r'haha([a-z]+)',' ',clean)
		clean = re.sub(r'huhu','',clean)
		clean = re.sub(r'huhu([a-z]+)',' ',clean)
		clean = re.sub(r'wakwak',' ',clean)
		clean = re.sub(r'wakwak([a-z]+)',' ',clean)
		# Bracket remover
		clean = re.sub(r'\.',' ',clean)
		clean = re.sub(r'\[',' ',clean)
		clean = re.sub(r'\]',' ',clean)
		clean = re.sub(r'\/',' ',clean)
		clean = re.sub(r'\(',' ',clean)
		clean = re.sub(r'(\w)\1{2,}', r'\1', clean)
		clean = re.sub(r'\d+',' ',clean)

		return clean

	def root_checker(self,tokenized):
		new_tokenized = []

		for word in tokenized:
			if word in root_words and word not in stop_word:
				new_tokenized.append(word)

		return new_tokenized