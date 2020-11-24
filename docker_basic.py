import os
import speech_recognition as sr

def design_1():
	os.system(" tput  setaf 1 ")
	os.system(" tput bold ")
	print(" \t\t\t========================================================")
	os.system(" espeak-ng -a 170 -s 150 ' Docker Automation' ")
	print(" \t\t\t!!----------->> Docker Menu Automation <<-------------!!")
	os.system(" tput  setaf 2 ")
	print(" \t\t\t========================================================")
	os.system(" tput setaf 4 ")


def design_2():
	print(" \t\t/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/")
	os.system(" tput  setaf 1 ")
	print(" \t\t\t\t***** Basic Commands ***** ")
	os.system(" espeak-ng -a 170 -s 150 ' Docker Basic Commands ' ")
	os.system(" tput setaf 2 ")
	print(" \t\t\t\t____________________________\n")
	os.system(" tput setaf 4 ")

def docker():
	print("""
         Services:
	\t--------> Check Docker Version
	\t--------> Docker Info
	\t--------> Display Multiple Commands
	\t--------> Show all Docker Images
	\t--------> Check all Stopped/Running Containers
	\t--------> Show Container's ID
	\t--------> Remove all Containers
	\t--------> Remove all Images
	\t--------> Show Insights of Docker
	\t--------> Web Server Menu
	""")

def takeCommand():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print()
		print("\t\t\t\tI am listening, tell me your requirements...!!!\n")
		os.system(" espeak-ng -a 170 -s 150 'Start Saying' ")
		r.pause_threshold = 2
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

design_1()
design_2()
docker()

r = input("How do you want to run the program ? ( local or remote )  :    ")
print()

if r == 'remote':
	ip = input("Enter IP address where you want to remote login :  ")
	print()
	k_name = input("Enter the name of private key:  ")

while True:
	os.system(" clear ")
	docker()
	query = takeCommand().lower()
	os.system(" tput  setaf 18 ")

	if r == 'local':
		if "version" in query:
			os.system(' docker -v ')
			print()

		elif "info" in query:
			os.system( " docker info ")
			print()

		
		elif "multiple" in query:
			os.system(" docker help ")
			print()

		elif "all images" in query:
			os.system(" docker images ")
			print()

		elif "containers" in query:
			os.system(" docker ps -a ")
			print()

		elif "running" in query:
			os.system(" docker ps -a -q ")
			print()

		elif "remove all containers" in query:
			os.system(" docker rm `docker ps -a -q` ")
			print()

		elif "remove all images" in query:
			os.system(" docker rmi `docker ps -a -q`")
			print()

		elif "insights" in query:
			cont_name = input("Enter the name of container:  ")
			os.system(" docker logs {} ".format(cont_name))
			print()

		elif "menu" in query:
			break

		input(" Press Enter to Continue......")

	elif r == 'remote':
		if "version" in query:
			os.system(' ssh -i {}.pem root@{} docker -v '.format(k_name, ip))
			print()

		elif "info" in query:
			os.system( " ssh -i {}.pem root@{} docker info ".format(k_name, ip))
			print()

		elif "multiple" in query:
			os.system(" ssh -i {}.pem root@{} docker help ".format(k_name, ip))
			print()

		elif "all images" in query:
			os.system(" ssh -i {}.pem root@{} docker images ".format(k_name, ip))
			print()

		elif "containers" in query:
			os.system(" ssh -i {}.pem root@{} docker ps -a ".format(k_name, ip))
			print()

		elif "running" in query:
			os.system(" ssh -i {}.pem root@{} docker ps -a -q ".format(k_name, ip))
			print()

		elif  "remove all containers" in query:
			os.system(" ssh -i {}.pem root@{} docker rm `docker ps -a -q` ".format(k_name, ip))
			print()

		elif  "remove all images" in query:
			os.system(" ssh -i {}.pem root@{} docker rmi `docker ps -a -q`".format(k_name, ip))
			print()

		elif "insights" in query:
			cont_name = input(" Enter the name of container:  ")
			os.system(" ssh -i {}.pem root@{} docker logs {} ".format(k_name, ip, cont_name))
			print()

		elif "menu" in query:
			break

		os.system(" tput setaf 19 ")
		input(" \t\t\t\tPress Enter to Continue......")


	else:
		break


