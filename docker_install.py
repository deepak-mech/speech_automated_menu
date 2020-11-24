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
	print(" \t\t\t\t***** Install/Launch Docker ***** ")
	os.system(" espeak-ng -a 170 -s 150 ' Installation and Launching of Docker ' ")
	os.system(" tput setaf 2 ")
	print(" \t\t\t\t___________________________________\n")
	os.system(" tput setaf 4 ")

def docker():
	print("""
	Services:
	\t---------> Configure Yum for Docker
	\t---------> Install Docker
	\t---------> Start Docker Services
	\t---------> Pull Docker Images 
	\t---------> Launch Docker OS
	\t---------> Stop & Start Container
	\t---------> Stop docker services
	\t---------> Docker Basic Commands Menu
	""")

def takeCommand():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print()
		print("\t\t\t\tI am listening, tell me your requirements...!!!\n")
		os.system(" espeak-ng -a 170 -s 150  'Start Saying' ")
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
	os.system(' clear ')
	docker()
	query = takeCommand().lower()

	if r == 'local':
		if "yum" in query:
			os.system(' echo "[docker2]" >> dock.repo ')
			os.system(' echo "baseurl = https://download.docker.com/linux/centos/7/x86_64/stable" >> docker.repo ')
			os.system(' echo "gpgcheck. = 0" >> docker.repo ')
			os.system(' mv dock.repo  /etc/yum.repos.d/ ')
			os.system(' yum list docker-ce ')
			print("\t\t\t____________________________________")
			os.system(" tput setaf 2 ")
			print(' \t\t\t\tYum Configured Successfully ')
			os.system(" tput setaf 19 ")
			print("\t\t\t_______________________________\n")
			os.system("  espeak-ng -a 170 -s 150 ' Yum Configured Successfully ' ")

		elif "install" in query:
			os.system( " yum install docker-ce --nobest ")
			os.system(" rpm -q docker-ce ")
			print("\t\t\t____________________________________")
			os.system(" tput setaf 2 ")
			print(' \t\t\t\tDocker Installed Successfully ')
			os.system(" tput setaf 23 ")		
			print("\t\t\t____________________________________\n")
			os.system("  espeak-ng -a 170 -s 150 ' Docker Installed Successfully  ' ")

		elif "start docker service" in query:
			os.system( " systemctl stop firewalld ")
			os.system( " systemctl start docker ")
			os.system( " systemctl status docker ")
			print("\t\t\t____________________________________")
			os.system(" tput setaf 2 ")
			print(' \t\t\t\tDocker Services Started ')
			os.system(" tput setaf 19 ")
			print("\t\t\t____________________________________\n")
			os.system("  espeak-ng -a 170 -s 150 ' Docker Services Started ' ")

		elif "pull" in query:
			img_name = input("Enter the name of image:  ")
			os.system(" docker pull {}  ".format(img_name))
			os.system(' docker images ')
			print("\t\t\t____________________________________")
			os.system(" tput setaf 2 ")
			print(' \t\t\t\tImages Pulled Successfully ')
			os.system(" tput setaf 23 ")
			print("\t\t\t____________________________________\n")
			os.system("  espeak-ng -a 170 -s 150 ' Images Pulled Successfully ' ")

		elif "launch" in query:
			cont_name = input('\t\t\tEnter the name of container:  ')
			img_name = input("\t\t\tEnter the name of image:  ")
			os.system(" docker run -dit --name {} -p 8080:80 {} ".format(cont_name, img_name))
			os.system(' docker ps ')
			print("\t\t\t____________________________________")
			os.system(" tput setaf 2 ")
			print(' \t\t\t\tDocker Launched Successfully ')
			os.system(" tput setaf 19 ")
			print("\t\t\t____________________________________\n")
			os.system("  espeak-ng -a 170 -s 150 ' Docker Launched Successfully ' ")

		elif ("start" in query) and ("stop" in query):
			cont_name = input(' Enter the name of container:  ')
			os.system(' docker stop {} '.format(cont_name))
			os.system(' docker ps ')
			input(" Press Enter to Continue......")
			os.system(' docker start {} '.format(cont_name))
			os.system(' docker ps ')
			input(" Press Enter to Continue......")
			os.system(' docker attach {} '.format(cont_name))
			print()

		elif "stop docker service" in query:
			os.system( " systemctl stop docker ")
			os.system( " systemctl status docker ")
			print("\t\t\t____________________________________")
			os.system(" tput setaf 23 ")
			print(' \t\t\t\tDocker Services Stopped ')
			os.system(" tput setaf 19 ")
			print("\t\t\t____________________________________\n")
			os.system("  espeak-ng -a 170 -s 150 ' Docker Services Stopped ' ")

		elif "basic" in query:
			break

		input(" Press Enter to Continue......")

	elif r == 'remote':
		if "yum" in query:
			os.system(' echo "[docker2]" >> docker.repo ')
			os.system(' echo "baseurl = https://download.docker.com/linux/centos/7/x86_64/stable" >> docker.repo ')
			os.system(' echo "gpgcheck = 0" >> docker.repo ')
			os.system(' scp -i {}.pem docker.repo root@{}:/etc/yum.repos.d/  '.format(k_name, ip))
			os.system('  ssh -i {}.pem root@{} yum list docker-ce '.format(k_name, ip))
			os.system(' rm -rf  docker.repo ' )
			print("\t\t\t____________________________________")
			os.system(" tput setaf 23 ")
			print(' \t\t\t\tYum Configured Successfully ')
			os.system(" tput setaf 18 ")
			print("\t\t\t____________________________________\n")
			os.system("  espeak-ng -a 170 -s 150 ' Yum Configured Successfully ' ")
	

		elif "install" in query:
			os.system( "  ssh -i {}.pem root@{} yum install docker-ce --nobest ".format(k_name, ip))
			os.system("  ssh -i {}.pem root@{} rpm -q docker-ce ".format(k_name, ip))
			print("\t\t\t____________________________________")
			os.system(" tput setaf 2 ")
			print(' \t\t\t\tDocker Installed Successfully ')
			os.system(" tput setaf 19 ")
			print("\t\t\t____________________________________\n")
			os.system("  espeak-ng -a 170 -s 150 ' Docker Installed Successfully  ' ")

		elif "start docker service" in query:
			os.system( " ssh -i {}.pem root@{} setenforce 0 ".format(k_name, ip))
			os.system( " ssh -i {}.pem root@{} systemctl start docker ".format(k_name, ip))
			os.system( " ssh -i {}.pem root@{} systemctl status docker ".format(k_name, ip))
			print("\t\t\t_______________________________")
			os.system(" tput setaf 2 ")
			print(' \t\t\t\tDocker Services Started ')
			os.system(" tput setaf 23 ")
			print("\t\t\t_______________________________\n")
			os.system("  espeak-ng -a 170 -s 150 ' Docker Services Started ' ")

		elif  "pull" in query:
			img_name = input("Enter the name of image:  ")
			os.system(" ssh -i {}.pem root@{} docker pull {}  ".format(k_name, ip, img_name))
			os.system(' ssh -i {}.pem root@{} docker images '.format(k_name, ip))
			print("\t\t\t____________________________________")
			os.system(" tput setaf 23 ")
			print(' \t\t\t\tImages Pulled Successfully ')
			os.system(" tput setaf 18 ")
			print("\t\t\t____________________________________\n")
			os.system("  espeak-ng -a 170 -s 150 ' Images Pulled Successfully ' ")

		elif "launch" in query:
			cont_name = input('Enter the name of container:  ')
			img_name = input("Enter the name of image:  ")
			os.system(" ssh -i {}.pem root@{} docker run -dit --name {} -p 8080:80 {} ".format(k_name, ip, cont_name, img_name))
			os.system(' ssh -i {}.pem root@{} docker ps '.format(k_name, ip))
			print("\t\t\t____________________________________")
			os.system(" tput setaf 2 ")
			print(' \t\t\t\tDocker Launched Successfully ')
			os.system(" tput setaf 19 ")
			print("\t\t\t____________________________________\n")
			os.system("  espeak-ng -a 170 -s 150 ' Docker Launched Successfully ' ")

		elif "start" and "stop" in query:
			cont_name = input(' Enter the name of container:  ')
			os.system(' ssh -i {}.pem root@{} docker stop {} '.format(k_name, ip, cont_name))
			os.system(' ssh -i {}.pem root@{} docker ps '.format(k_name, ip))
			input(" Press Enter to Continue......")
			os.system(' ssh -i {}.pem root@{} docker start {} '.format(k_name, ip, cont_name))
			os.system(' ssh -i {}.pem root@{} docker ps '.format(k_name, ip))
			print()

		elif "stop docker service" in query:
			os.system( " ssh -i {}.pem root@{} systemctl stop docker ".format(k_name, ip))
			os.system( " ssh -i {}.pem root@{} systemctl status docker ".format(k_name, ip))
			print("\t\t\t_______________________________")
			os.system(" tput setaf 2 ")
			print(' \t\t\t\tDocker Services Stopped ')
			os.system(" tput setaf 23 ")
			print("\t\t\t_______________________________\n")
			os.system("  espeak-ng -a 170 -s 150 ' Docker Services Stopped ' ")

		elif "basic" in query:
			break
		
		os.system(" tput setaf 4 ")
		input(" \t\t\t\tPress Enter to Continue......")


	else:
		break


