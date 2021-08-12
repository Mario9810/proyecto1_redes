
"""
References:https://sleekxmpp.readthedocs.io/en/latest/getting_started/sendlogout.html
	https://sleekxmpp.readthedocs.io/en/latest/getting_started/echobot.html
	https://python.hotexamples.com/examples/sleekxmpp/ClientXMPP/get_roster/python-clientxmpp-get_roster-method-examples.html
	https://sleekxmpp.readthedocs.io/en/latest/getting_started/muc.html
	Examples in: https://github.com/fritzy/SleekXMPP/tree/develop/examples
"""
import time
import Client as client
import UI
from inputimeout import inputimeout, TimeoutOccurred
import sys



moveUp=lambda n:u"\u001b["+str(n)+"A"

cleanLine=lambda :u"\u001b["+str(2)+"K"

"""
Function that takes care of the user session 
"""
def Ccontrol(event):
	xmpp.start()
	while 1:
		

		try:
			if(len(xmpp.notifications)>0):
				#notifications if someone is online 
				UI.menuprincipal(xmpp.notifications.pop(0))
			else:
				#load user's main menu
				UI.menuprincipal()
			userInput = inputimeout(prompt='> ', timeout=5)
			
			if(UI.homeio(userInput)):
				time.sleep(1)
				if(userInput=='1'):
					
					#this displays all the users in the server 
					UI.mostrartodos()
					xmpp.getAllUsers()
					input('\npresiona una tecla para continuar...')
					"""
					this attempts to show all contacts to which the user 
					is subscribed
					"""
					UI.contactos()
					xmpp.getMyContacts()
					input('\npresiona una tecla para continuar...')
				elif(userInput=='2'):
					
					"""
					attemps to add an user to contacts 
					"""
					user=UI.agregar()
					xmpp.addSubscription(user)
				elif(userInput=='3'):
					
					"""
					attemps to search for an especified user
					"""
					user=UI.busqueda()
					xmpp.getContact(user)
					input('\npresiona una tecla para continuar...')
				elif(userInput=='4'):
					
					"""
					Displays the options for private messaging 
					"""
					userInput,control=UI.buzon(xmpp.getListOfContact())
					if(userInput!=-100):
						print(userInput)
						if(control):
							xmpp.updateInbox(userInput)
						
						xmpp.updateInboxContacts()
						"""
						Displays priavte messaging CLI
						"""
						UI.chatprivado(userInput)
						client.inbox[userInput].DesplegarMensajes()
						while 1:
							try:
								chatInput=inputimeout(prompt='> ', timeout=10)
							except TimeoutOccurred:
								chatInput=""

							sys.stdout.write(moveUp(1))
							sys.stdout.write(cleanLine())
							sys.stdout.flush()
							if(chatInput=='exit()'):
								break
							if(chatInput!=''):
								xmpp.enviarMensaje(userInput,chatInput)
								client.inbox[userInput].Mensajen('Me',chatInput)
							

							client.inbox[userInput].nods()
				elif(userInput=='5'):
					
					"""
					changes status and presence message
					"""
					status,presence=UI.estado()
					xmpp.SendPresenceMessage(status,presence)
				elif(userInput=='6'):
					"""
					Option to delete current account 
					"""
					xmpp.deleteAccount()
					print('se ha borrado la cuenta')
					time.sleep(1)
					break
				elif(userInput=='7'):
					"""
					Exits the program
					"""
					print('-- cargando --')
					break
		except TimeoutOccurred:
			continue
		
	
	xmpp.desconectarse()
	
	
"""
   Main
"""

if __name__ == "__main__":

	
	while True:
		"""
		Displays main menu
		"""
		UI.lobby()
		userInput=input('> ')
		print(userInput)
		if(UI.lobbyio(userInput)):
			"""
			validates user input
			"""
			if(userInput=='1'):
				
				"""
				Displays log in CLI
				"""
				user,password=UI.iniciosesion()

				xmpp = client.Client(user,password)
				xmpp.add_event_handler("session_start",Ccontrol, threaded=True)
				if xmpp.connect(address=("localhost",5222)): #attemps to connect to espcecified server on PORT 5222, use 5223  for legacy connection
					xmpp.process(block=False)

					print('cargando')
					break
			elif(userInput=='2'):
				
				"""
				Displays register CLI
				"""
				user,password=UI.registro()
				xmpp = client.RegisterClient(user,password)
				xmpp.register_plugin('xep_0030')  # Service Discovery
				xmpp.register_plugin('xep_0004')  # Data forms
				xmpp.register_plugin('xep_0066')  # Out-of-band Data
				xmpp.register_plugin('xep_0077')  # In-band Registration
				xmpp['xep_0077'].force_registration = True
				if xmpp.connect(address=("127.0.0.1",5222)):
					xmpp.process(block=False)
				print('Cuenta registrada')
				time.sleep(2)
			elif(userInput=='3'):
				"""
				exits the program
				"""
				break
