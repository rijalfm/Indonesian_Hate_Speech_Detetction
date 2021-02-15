import pickle
from flask import Flask, jsonify
from abusive import Abusive
from text_preprocessing import Text

class Model:

	def __init__(self):
		self.Model = pickle.load(open('log_model.sav','rb'))

	def hate_speech(self):
		text_processed = Text(self.text).final_text
		result = self.Model.predict([text_processed])[0]

		return result

	def abusive(self):
		result = Abusive(self.text)

		return result.results

	def result_json(self,text=None):
		if text:
			self.text = text
			HS = self.hate_speech()
			ABUSIVE = self.abusive()

			json_data = {'hate_speech':str(HS),
										'abusive':ABUSIVE}

			return jsonify(json_data), 200

		return jsonify({'error':'No text submited!'}), 404
