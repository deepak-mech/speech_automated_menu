import os
import speech_recognition as sr

def design1():
	os.system(" clear ")
	os.system(" tput bold ")
	print(" \t\t\t@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ ")
	os.system(" tput  setaf 1 ")
	print("      \t\t!!------->> Welcome to this Automation World <<--------!!\t\t")
	os.system(" tput  setaf 2 ")
	print(" \t\t\t@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ ")
	os.system(" espeak-ng -a 170 -s 150 'Welcome to this Automation World' ")
	os.system(' espeak-ng -a 170 -s 150  "Services available with Automation are" sleep 2')
	print("\t\t 1). Hadoop Services \t\t\t 2). LVM Facility \n\n \t\t 3). Docker Services \t\t\t 4). AWS Cloud Services \n")
	print("\t\t\t\t 5). Basic Linux Commands \n")
	os.system(" espeak-ng -a 170 -s 150   'Hadoop' ")
	os.system(" espeak-ng -a 170 -s 150  'LVM' ")
	os.system(" espeak-ng -a 170 -s 150  'Docker' ")
	os.system(" espeak-ng -a 170 -s 150   'A W S' ")
	os.system(" espeak-ng -a 170 -s 150   'Basic Linux Commands' ")
	os.system(" tput setaf 4 ")

def design2():
	print("--------------------------------------------------------")
	os.system(" tput setaf 25 ")
	print("\tLocal Host --------> Virtual Machines (RHEL8)")
	print("\tRemote Host --------> AWS EC2 Instances")
	os.system(" tput setaf 93 ")
	print("--------------------------------------------------------")

def takeCommand():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print()
		print("\t\t\t\tI am listening, tell me your requirements...!!!\n")
		os.system(" espeak-ng -a 170 -s 150 'Start Saying' ")
		r.pause_threshold = 3
		audio = r.listen(source)
      
	try:
		print('\t\t\t\t Just wait I am recognising...!!!\n')
		os.system(" espeak-ng -a 170 -s 150 ' I got it, please wait' ")
		query = r.recognize_google(audio, language='en-in')
		#print(query)

	except Exception as e:
		print(e)
		print('Say that again please...')

	return query

while True:
	os.system(' clear ')
	design1()
	design2()
	query = takeCommand().lower()

	if  'how are you'  in query:
		print(" I am good  & what's about you ? ")
		os.system(" espeak-ng -a 170 -s 150 ' I am good  & what's about you ' ")

	elif 'yourself' in query:
		print(" I am your voice assistant Ziara Sir  & today I wil operate all the services automatically ")
		os.system(" espeak-ng -a 170 -s 150 ' I am your voice assistant Ziara Sir  & today I wil operate all the services automatically ' ")

	elif "show docker menu" or " so doker menu" in query:
		os.system(" clear ")
		os.system(" python3 docker_install.py ")
		os.system(" clear ")
		os.system(" python3 docker_basic.py ")
		os.system(" clear ")
		os.system(" python3 docker_web_server.py ")
		os.system(" clear ")
		os.system(" python3 docker_python.py ")
		os.system(" clear ")
	
	else:
		break


		


