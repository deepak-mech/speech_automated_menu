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
	print(" \t\t\t\t\t***** Web Server ***** ")
	os.system(" espeak-ng -a 170 -s 150 ' Web Server on Docker' ")
	os.system(" tput setaf 2 ")
	print(" \t\t\t\t_________________________________\n")
	os.system(" tput setaf 4 ")

def docker():
	print("""
	Services:
	\t--------> Restart Docker Services
	\t--------> Install HTTPD
	\t--------> Create Web Page
	\t--------> Start Web Services
	\t--------> Show Web Page
	\t--------> Python Set up Menu
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
	ip = input("\t\t\tEnter the IP of your remote host :  ")
	print()
	k_name = input("\t\t\tEnter the name of private key:  ")
	print()
	cont_name = input(' \t\t\tEnter the name of container:  ')

while True:
	os.system(" clear ")
	docker()
	query = takeCommand().lower()
	os.system(" tput  setaf 17 ")

	if r == 'local':
		if "restart" in query:
			cont_name = input(' \t\t\tEnter the name of container:  ')
			os.system( " systemctl stop firewalld ")
			os.system( " systemctl restart docker ")
			os.system( " systemctl status docker ")
			os.system(" docker start {} ".format(cont_name))
			print()

		elif "install" in query:
			os.system(" docker exec -it  {} yum install httpd -y ".format(cont_name))
			print()

		
		elif "create" in query:
			wp_name = input(' Enter the name of web page:  ')
			os.system(" docker exec -it  {} vi {} ".format(cont_name, wp_name))
			print()

		elif "start web services" in query:
			os.system(" docker exec -it  {} /usr/sbin/httpd ".format(cont_name))
			os.system(" docker exec -it  {} mv {} /var/www/html ".format(cont_name, wp_name))
			os.system(" docker exec -it  {} rm -rf {} ".format(cont_name, wp_name))
			os.system(' netstat -tnlp ')
			print()

		elif "open web page" in query:
			ip = input(' Enter the IP of your local host:  ')
			os.system(" gio open http://{}:8080/{} ".format(ip, wp_name))
			print()

		elif "menu" in query:
			break

		os.system(" tput  setaf 23 ")
		input(" Press Enter to Continue......")

	elif r == 'remote':
		if "restart" in query:
			cont_name = input(' \t\t\tEnter the name of container:  ')
			os.system( " ssh -i {}.pem root@{} setenforce 0 ".format(k_name, ip))
			os.system( " ssh -i {}.pem root@{} systemctl restart docker ".format(k_name, ip))
			os.system( " ssh -i {}.pem root@{} systemctl status docker ".format(k_name, ip))
			os.system(" ssh -i {}.pem root@{} docker start {} ".format(k_name, ip, cont_name))
			print()

		elif "install" in query:
			os.system(" ssh -i {}.pem root@{} docker exec {} yum install httpd -y ".format(k_name, ip, cont_name))
			print()

		
		elif "create" in query:
			wp_name = input(' Enter the name of web page:  ')
			os.system(' vi {} '.format(wp_name))
			os.system(" scp -i {}.pem {} root@{}:/root ".format(k_name, wp_name, ip))
			os.system(' rm -rf {} '.format(wp_name))
			os.system(" ssh -i {}.pem root@{} docker cp {} {}:/var/www/html ".format(k_name, ip, wp_name, cont_name))
			os.system(" ssh -i {}.pem root@{} rm -rf {} ".format(k_name, ip, wp_name))
			print()

		elif "start web services" in query:
			os.system(" ssh -i {}.pem root@{} docker exec {} /usr/sbin/httpd ".format(k_name, ip, cont_name))
			os.system(' ssh -i {}.pem root@{} docker exec {} yum install net-tools -y'.format(k_name, ip, cont_name))
			os.system(' ssh -i {}.pem root@{} docker exec {} netstat -tnlp '.format(k_name, ip, cont_name))
			print()

		elif "open web page" in query:
			remote_ip = input(' Enter the IP of your remote host:  ')
			wp_name = input(' Enter the name of web page:  ')
			os.system(" gio open http://{}:8080/{} ".format(remote_ip, wp_name))
			print()

		elif  "menu" in query:
			break

		os.system(" tput  setaf 23 ")
		input(" Press Enter to Continue......")


	else:
		break
