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
	os.system(" tput  bold ")
	print(" \t\t\t\t\t***** Python Set up ***** ")
	os.system(" espeak-ng -a 170 -s 150 ' Docker Automation' ")
	os.system(" tput setaf 2 ")
	print(" \t\t\t\t______________________________________\n")
	os.system(" tput setaf 4 ")

def docker():
	print("""
	Services:
	\t-------> Install Python on Docker
	\t-------> Write Code in Python
	\t-------> Show Python Code
	\t-------> Run Python Code
	\t-------> Back to Main Menu
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

os.system(" tput setaf 2 ")
 
r = input("How do you want to run the program ? ( local or remote )  :    ")
print()

os.system(" tput setaf 4 ")

if r == 'remote':
	ip = input("\t\t\tEnter the IP of your remote host :  ")
	print()
	k_name = input("\t\t\tEnter the name of private key:  ")
	print()
	cont_name = input(' \t\t\tEnter the name of container:  ')

while True:
	os.system(" clear ")
	docker()
	query = takeCommand().lower()
	os.system(" tput  setaf 8 ")

	if r == 'local':
		if "install python" in query:
			cont_name = input(' \t\t\tEnter the name of container:  ')
			os.system(" docker exec -it  {} yum install python3 ".format(cont_name))
			os.system(" tput setaf 2 ")
			print(" \t\t\t\tPython Installed Successfully \n")
			os.system(" tput setaf 4 ")

		elif "write python code" in query:
			file_name = input(" \t\t\tGive the name of file:  ")
			os.system(" docker exec -it  {} vi {} ".format(cont_name, file_name))
			print()

		elif "show python code" in query:
			os.system(" docker exec -it  {} cat {} ".format(cont_name, file_name))
			print()

		elif "run python code" in query:
			os.system(" docker exec -it  {} python3 {} ".format(cont_name, file_name))
			os.system(" tput setaf 2 ")
			print(" \t\t\t\tPython Code is Working Good\n")
			os.system(" tput setaf 4 ")

		elif "menu" in query:
			break

		os.system(" tput  setaf 19 ")
		input(" \t\t\t\tPress Enter to Continue......")

	elif r == 'remote':
		if "install python" in query:
			os.system(" ssh -i {}.pem root@{} docker exec  {} yum install python3 -y ".format(k_name, ip, cont_name))
			os.system(" tput setaf 2 ")
			print(" \t\t\t\tPython Installed Successfully \n")
			os.system(" tput setaf 4 ")

		elif "write python code" in query:
			file_name = input(" Give the name of file:  ")
			os.system(' vi {} '.format(file_name))
			os.system(" scp -i {}.pem {} root@{}:/root ".format(k_name, file_name, ip))
			os.system(' rm -rf {} '.format(file_name))
			os.system(" ssh -i {}.pem root@{} docker cp {} {}:/root ".format(k_name, ip, file_name, cont_name))
			os.system(" ssh -i {}.pem root@{} rm -rf {} ".format(k_name, ip, file_name))
			print()

		elif "show python code" in query:
			read_file = input(' \t\t\tEnter the name of file to read:  ')
			os.system(" ssh -i {}.pem root@{} docker exec {} cat /root/{} ".format(k_name, ip, cont_name, read_file))
			print()

		elif "run python code" in query:
			os.system("ssh -i {}.pem root@{} docker exec {} python3 /root/{}".format(k_name, ip, cont_name, file_name))
			os.system(" tput setaf 2 ")
			print(" \t\t\t\tPython Code is Working Good\n")
			os.system(" tput setaf 4 ")

		elif "menu" in query:
			break

		os.system(" tput  setaf 23 ")
		input(" \t\t\t\tPress Enter to Continue......")


	else:
		break
