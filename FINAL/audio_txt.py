from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.conversation import Statement
from chatterbot.comparisons import LevenshteinDistance
import speech_recognition as sr 
import pyttsx3
 
bot = pyttsx3.init() 
chat = ChatBot('Cortana')
trainer = ChatterBotCorpusTrainer(chat)
trainer.train("chatterbot.corpus.spanish.dinero")
trainer.train("chatterbot.corpus.spanish.emociones")
trainer.train("chatterbot.corpus.spanish.psicologia")
trainer.train("chatterbot.corpus.spanish.trivia")
trainer.train("chatterbot.corpus.spanish.perfilbot")
trainer.train("chatterbot.corpus.spanish.IA")
trainer.train("chatterbot.corpus.spanish.greetings")
trainer.train("chatterbot.corpus.spanish.a_mayores")
trainer.train("chatterbot.corpus.spanish.conversations")
#bot = 'Cortana'
listener = sr.Recognizer()

def talk(record):
#f
	message = Statement(record)
	reply = chat.get_response(message) 
	dist = LevenshteinDistance().compare(message,reply)
	print('Yo: ', message)
	print('Bot: ', reply)

	bot.say(reply)
	bot.runAndWait()


try:
	with sr.Microphone() as source:
		print("Habla")
		
		while True:
			voice = listener.listen(source)
			record = listener.recognize_google(voice, language='es-MX')
			record = record.lower()
			talk(record)
		
		
except: 
	print("Adios")
