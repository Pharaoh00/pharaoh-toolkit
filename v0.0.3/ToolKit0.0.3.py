# ToolKit criado por Pharaoh
# Versão 0.0.3 (2017) [Seg, 3 Jul 08:40:59]
# Linguagem = PT-BR

# Novo na versão 0.0.3:
# Adicionado modulo Calculadora no menu ~~2.Calculadora~~
# Importado modulo math. (python)
#
# -----------------------------------------------------------------------------------------------------------------------------------#
# Modulo Calculadora:
# Adicionado Sandbox.
# Sandbox é o modo eval() do proprio python. Possibilidando o usuario fazer qualquer operação por si só.
# Aceita opções como 10+10 ou 25*2. Aceitando todos os operadores comuns do python.
# Modo sqr. Raiz Quadrada, math.sqrt().
# Modo MDC. math.gcd().
# Modo MMC. Algoritmo inspirado (https://gist.github.com/endolith/114336).
# -----------------------------------------------------------------------------------------------------------------------------------#
#
#
import random, time, math
import string, sys

def main():
# -----------------------------------------------------------------------------------------------------------------------------------#
	# Modulo Gerador de Senha.
	def PasswordGenerator():
		# Titulo
		print("\nGerador de Senhas\n")
		# Titulo
		# INICIO FUNÇÕES DAS OPÇOES DO MENU
		#
		# Gerador para a senha "Fraca".
		def PassFraca(x):
			while(True):
				# LEMBRETE - TROCAR OS IF'S "-v" e "exit" E COLOCALOS EM CIMA, PARA SEREM AS PRIMEIRAS OPÇÕS A SEREM CHECADAS
				#
				#
				if not x.isdigit() and str(x) != "exit":
					print("Somente numeros")
					break
				elif int(x) > 72:
					print("Não tente quebrar o programa!")
				elif int(x) == 0:
					print("Não se pode ter uma senha com zero caracteres, não é mesmo?")
				elif str(x) == "-v":
					break
				elif str(x) == "exit":
					print("Saindo do programa")
					sys.exit()
				else:
					letterStore = string.ascii_lowercase # Letras de A a Z minusculas.
					print("") # Espaço.
					finalPass = "".join(random.sample(letterStore, int(x))) # Junção e Randomização.
					print("Essa senha está boa?: ", finalPass,"\n")
					return True # Failsafe?.
		# Gerador para a senha "Media".
		def PassMedia(x):
			while(True):
				if not x.isdigit() and str(x) != "exit":
					print("Somente numeros")
					break
				elif int(x) > 72:
					print("Não tente quebrar o programa!")
				elif int(x) == 0:
					print("Não se pode ter uma senha com zero caracteres, não é mesmo?")
				elif str(x) == "-v":
					break
				elif str(x) == "exit":
					print("Saindo do programa")
					sys.exit()
				else:
					letterStore = string.ascii_letters # Letras de A a Z minusculas e Maiusculas.
					print("") # Espaço
					finalPass = "".join(random.sample(letterStore, int(x)))
					print("Essa senha está boa?: ", finalPass,"\n")
					return True
		# Gerador para a senha "Forte".
		def PassForte(x):
			while(True):
				if not x.isdigit() and str(x) != "exit":
					print("Somente numeros")
					break
				elif int(x) > 72:
					print("Não tente quebrar o programa!")
				elif int(x) == 0:
					print("Não se pode ter uma senha com zero caracteres, não é mesmo?")
				elif str(x) == "-v":
					break
				elif str(x) == "exit":
					print("Saindo do programa")
					sys.exit()
				else:
					letterStore = string.ascii_letters + string.digits # Letrasde A a Z minusculas, Maiusculas e os numeros de 0 a 9.
					print("") # Espaço
					finalPass = "".join(random.sample(letterStore, int(x)))
					print("Essa senha está boa?: ", finalPass,"\n")
					return True
		# Gerador para a senha "Insana".
		def PassInsana(x):
			while(True):
				if not x.isdigit() and str(x) != "exit":
					print("Somente numeros")
					break
				elif int(x) > 72:
					print("Não tente quebrar o programa!")
				elif int(x) == 0:
					print("Não se pode ter uma senha com zero caracteres, não é mesmo?")
				elif str(x) == "-v":
					break
				elif str(x) == "exit":
					print("Saindo do programa")
					sys.exit()
				else:
					letterStore = string.ascii_letters + string.digits + string.punctuation # Letrasde A a Z minusculas, Maiusculas, os numeros de 0 a 9 e os caracteres especiais como "%" ou "$"
					print("") # Espaço
					finalPass = "".join(random.sample(letterStore, int(x)))
					print("Essa senha está boa?: ", finalPass,"\n")
					return True
		# Gerador para "Custom".
		def PassCustom(a,b,c,d):
			try:
				enter = ""
				# Começo Bloco parametro A.
				if a != enter and b == enter and c == enter and d == enter: # Caso o slot 1 for diferente que "" Lettersore é igual "a", caso for numero, upper, lower ou espec "a" acaba se tornando umas das strings.
					if a == "numero":
						a = string.digits
					if a == "upper":
						a = string.ascii_uppercase
					if a == "lower":
						a = string.ascii_lowercase
					if a == "espec":
						a = string.punctuation
					letterStore = a # Somente se A for diferent.
				elif a != enter and b != enter and c == enter and d == enter:
					if a == "numero":
						a = string.digits
					if a == "upper":
						a = string.ascii_uppercase
					if a == "lower":
						a = string.ascii_lowercase
					if a == "espec":
						a = string.punctuation
					#
					if b == "numero":
						b = string.digits
					if b == "upper":
						b = string.ascii_uppercase
					if b == "lower":
						b = string.ascii_lowercase
					if b == "espec":
						b = string.punctuation
					letterStore = a + b
					#
				elif a != enter and b == enter and c != enter and d == enter:
					if a == "numero":
						a = string.digits
					if a == "upper":
						a = string.ascii_uppercase
					if a == "lower":
						a = string.ascii_lowercase
					if a == "espec":
						a = string.punctuation
					#
					if c == "numero":
						c = string.digits
					if c == "upper":
						c = string.ascii_uppercase
					if c == "lower":
						c = string.ascii_lowercase
					if c == "espec":
						c = string.punctuation
					letterStore = a + c
					#
				elif a != enter and b == enter and c == enter and d != enter:
					if a == "numero":
						a = string.digits
					if a == "upper":
						a = string.ascii_uppercase
					if a == "lower":
						a = string.ascii_lowercase
					if a == "espec":
						a = string.punctuation
					#
					if d == "numero":
						d = string.digits
					if d == "upper":
						d = string.ascii_uppercase
					if d == "lower":
						d = string.ascii_lowercase
					if d == "espec":
						d = string.punctuation
					letterStore = a + d
					#
				elif a != enter and b != enter and c != enter and d == enter:
					if a == "numero":
						a = string.digits
					if a == "upper":
						a = string.ascii_uppercase
					if a == "lower":
						a = string.ascii_lowercase
					if a == "espec":
						a = string.punctuation
					#
					if b == "numero":
						b = string.digits
					if b == "upper":
						b = string.ascii_uppercase
					if b == "lower":
						b = string.ascii_lowercase
					if b == "espec":
						b = string.punctuation
					#
					if c == "numero":
						c = string.digits
					if c == "upper":
						c = string.ascii_uppercase
					if c == "lower":
						c = string.ascii_lowercase
					if c == "espec":
						c = string.punctuation
					letterStore = a + b + c
					#
				elif a != enter and b == enter and c != enter and d != enter:
					if a == "numero":
						a = string.digits
					if a == "upper":
						a = string.ascii_uppercase
					if a == "lower":
						a = string.ascii_lowercase
					if a == "espec":
						a = string.punctuation
					#
					if c == "numero":
						c = string.digits
					if c == "upper":
						c = string.ascii_uppercase
					if c == "lower":
						c = string.ascii_lowercase
					if c == "espec":
						c = string.punctuation
					#
					if d == "numero":
						d = string.digits
					if d == "upper":
						d = string.ascii_uppercase
					if d == "lower":
						d = string.ascii_lowercase
					if d == "espec":
						d = string.punctuation
					letterStore = a + c + d
					#
				elif a != enter and b != enter and c != enter and d != enter:
					if a == "numero":
						a = string.digits
					if a == "upper":
						a = string.ascii_uppercase
					if a == "lower":
						a = string.ascii_lowercase
					if a == "espec":
						a = string.punctuation
					#
					if b == "numero":
						b = string.digits
					if b == "upper":
						b = string.ascii_uppercase
					if b == "lower":
						b = string.ascii_lowercase
					if b == "espec":
						b = string.punctuation
					#
					if c == "numero":
						c = string.digits
					if c == "upper":
						c = string.ascii_uppercase
					if c == "lower":
						c = string.ascii_lowercase
					if c == "espec":
						c = string.punctuation
					#
					if d == "numero":
						d = string.digits
					if d == "upper":
						d = string.ascii_uppercase
					if d == "lower":
						d = string.ascii_lowercase
					if d == "espec":
						d = string.punctuation
					letterStore = a + b + c + d
				# Fim Bloco parametro A.
				# Começo Bloco parametro B.
				elif a == enter and b != enter and c == enter and d == enter:
					if b == "numero":
						b = string.digits
					if b == "upper":
						b = string.ascii_uppercase
					if b == "lower":
						b = string.ascii_lowercase
					if b == "espec":
						b = string.punctuation
					letterStore = b  # Somente se B for diferente.
					#
				elif a == enter and b != enter and c != enter and d == enter:
					if b == "numero":
						b = string.digits
					if b == "upper":
						b = string.ascii_uppercase
					if b == "lower":
						b = string.ascii_lowercase
					if b == "espec":
						b = string.punctuation
					#
					if c == "numero":
						c = string.digits
					if c == "upper":
						c = string.ascii_uppercase
					if c == "lower":
						c = string.ascii_lowercase
					if c == "espec":
						c = string.punctuation
					letterStore = b + c
					#
				elif a == enter and b != enter and c == enter and d != enter:
					if b == "numero":
						b = string.digits
					if b == "upper":
						b = string.ascii_uppercase
					if b == "lower":
						b = string.ascii_lowercase
					if b == "espec":
						b = string.punctuation
					#
					if d == "numero":
						d = string.digits
					if d == "upper":
						d = string.ascii_uppercase
					if d == "lower":
						d = string.ascii_lowercase
					if d == "espec":
						d = string.punctuation
					letterStore = b + d
					#
				elif a == enter and b != enter and c != enter and d != enter:
					if b == "numero":
						b = string.digits
					if b == "upper":
						b = string.ascii_uppercase
					if b == "lower":
						b = string.ascii_lowercase
					if b == "espec":
						b = string.punctuation
					#
					if c == "numero":
						c = string.digits
					if c == "upper":
						c = string.ascii_uppercase
					if c == "lower":
						c = string.ascii_lowercase
					if c == "espec":
						c = string.punctuation
					#
					if d == "numero":
						d = string.digits
					if d == "upper":
						d = string.ascii_uppercase
					if d == "lower":
						d = string.ascii_lowercase
					if d == "espec":
						d = string.punctuation
					letterStore = b + c + d
				# Fim Bloco parametro B.
				# Começo Bloco parametro C.
				elif a == enter and b == enter and c != enter and d == enter:
					if c == "numero":
						c = string.digits
					if c == "upper":
						c = string.ascii_uppercase
					if c == "lower":
						c = string.ascii_lowercase
					if c == "espec":
						c = string.punctuation
					letterStore = c  # Somente se C for diferente.
					#
				elif a == enter and b == enter and c != enter and d != enter:
					if c == "numero":
						c = string.digits
					if c == "upper":
						c = string.ascii_uppercase
					if c == "lower":
						c = string.ascii_lowercase
					if c == "espec":
						c = string.punctuation
					#
					if d == "numero":
						d = string.digits
					if d == "upper":
						d = string.ascii_uppercase
					if d == "lower":
						d = string.ascii_lowercase
					if d == "espec":
						d = string.punctuation
					letterStore = c + d
				# Fim Bloco parametro C.
				# Começo Bloco parametro D.
				elif a == enter and b == enter and c == enter and d != enter:
					if d == "numero":
						d = string.digits
					if d == "upper":
						d = string.ascii_uppercase
					if d == "lower":
						d = string.ascii_lowercase
					if d == "espec":
						d = string.punctuation
					letterStore = d  # Somente se D for diferente.
				# Fim Bloco parametro D.
				print("") # Espaço
				finalPass = "".join(random.sample(letterStore, int(passGen)))
				print("Essa sequencia está boa?: ", finalPass,"\n")
				return True
			except ValueError:
				print("Provavelmente não tem tantos characteres quanto o tamanho final do valor.\nPor favor, adicione mais characteres ou tente um valor menor!")
			except TypeError:
				print("Você tem que passar algum argumento")
######################### FIM FUNÇÕES
		# Inicio comparações
		while(True):
			askOpt = str(input("Você quer uma senha fraca, media, forte, insana ou custom?: "))
			# Caso fraca
			if askOpt == "fraca":
				passGen = input("Quantos caracteres você deseja ter?(entre 1 a 72): ")
				PassFraca(passGen) # Chamando a funão PassFraca(), que está la em cima.
			# Caso media
			elif askOpt == "media":
				passGen = input("Quantos caracteres você deseja ter?(entre 1 a 72): ")
				PassMedia(passGen) # Chamando a funão PassMedia(), que está la em cima.
			# Caso forte
			elif askOpt == "forte":
				passGen = input("Quantos caracteres você deseja ter?(entre 1 a 72): ")
				PassForte(passGen) # Chamando a funão PassForte(), que está la em cima.
			# Caso insana
			elif askOpt == "insana":
				passGen = input("Quantos caracteres você deseja ter?(entre 1 a 72): ")
				PassInsana(passGen) # Chamando a funão PassInsana(), que está la em cima.
			# Caso custom
			elif askOpt == "custom":
				while(True):
					passGen = input("Quantos caracteres você deseja ter?(entre 1 a 72): ")
					if str(passGen) == "-v":
						break
					elif str(passGen) == "exit":
						sys.exit()
					PassCustom(input("Slot 1: "),input("Slot 2: "),input("Slot 3: "),input("Slot 4: "))
			# Para sair do loop atual.
			elif askOpt == "-v":
				break
			# Para sair do programa.
			elif askOpt == "exit":
				print("\nSaindo do programa")
				sys.exit()
			elif askOpt.isdigit():
				print("\nSomente numeros\n")
			# Fim comparações
	# Fim modulo Geração de senha
# -----------------------------------------------------------------------------------------------------------------------------------#
# Inicio AJUDA
# -----------------------------------------------------------------------------------------------------------------------------------#
	def Ajuda():
		print("")
		print("")
		print("    ###          ## ##     ## ########     ###    ")
		time.sleep(0.1)
		print("   ## ##         ## ##     ## ##     ##   ## ##   ")
		time.sleep(0.1)
		print("  ##   ##        ## ##     ## ##     ##  ##   ##  ")
		time.sleep(0.1)
		print(" ##     ##       ## ##     ## ##     ## ##     ## ")
		time.sleep(0.1)
		print(" ######### ##    ## ##     ## ##     ## ######### ")
		time.sleep(0.1)
		print(" ##     ## ##    ## ##     ## ##     ## ##     ## ")
		time.sleep(0.1)
		print(" ##     ##  ######   #######  ########  ##     ## ")
		time.sleep(0.1)
		print("")
		print("")
		while(True):
			print("As opções disponiveis são:\n-help - Para obter mais informações.\nexit - Para sair do programa.(Sai completamente do programa)\n-v - Para voltar as opções anteriores.")
			askUser = input("O que desejar fazer?: ")
			if str(askUser) == "-v":
				break
			elif str(askUser) == "exit":
				sys.exit()
# -----------------------------------------------------------------------------------------------------------------------------------#
# Fim AJUDA
# -----------------------------------------------------------------------------------------------------------------------------------#
	# Modulo Calculadora
	def Calculadora():
		def SandBox():
			print("O valor de PI é:", math.pi)
			while(True):
				try:
					askUser = input("Quanto é: ")
					if str(askUser) == "-v":
						break
					elif str(askUser) == "exit":
						sys.exit()
					elif str(askUser) == "-help":
						print("\n-v para voltar.\nexit para sair.\nsqr para Raiz Quadrada.\nmdc ou mmc para Minimo Multiplo Comum ou Maximo Divisor Comum.\n(Qualquer uma das opções iram gerar tanto MMC quanto MDC)\n")
					elif str(askUser) == "sqr":
						askSqr = input("Raiz quadrada de: ")
						askSqr = math.sqrt(int(askSqr))
						print(askSqr)
					elif str(askUser) == "mdc" or str(askUser) == "mmc":
						slot1 = input("Numero: ")
						slot2 = input("Numero: ")
						mdc = math.gcd(int(slot1),int(slot2))
						mmc = int(slot1) * int(slot2) // math.gcd(int(slot1),int(slot2))
						print("O MDC entre", str(slot1),"e",str(slot2),"é:", mdc)
						print("O MMC entre", str(slot1),"e",str(slot2),"é:", mmc)
					else:
						askUser = eval(askUser)
						print(askUser)
				except ZeroDivisionError:
					print("Não se pode dividir por zero, lembra?")
				except SyntaxError:
					print("Invalido - SyntaxError")
				except ValueError:
					print("Invalido - ValueError")
				except NameError:
					print("Invalido - NameError")
		SandBox()
# -----------------------------------------------------------------------------------------------------------------------------------#
# Fim modulo Calculadora
	# ANIMÇÃO DO INICIO DO PROGRAMA
	print("")
	print("")
	time.sleep(0.1)
	print("   /$$$$$$$$                  /$$ /$$   /$$ /$$   /$$     ")
	time.sleep(0.1)
	print("  |__  $$__/                 | $$| $$  /$$/|__/  | $$     ")
	time.sleep(0.1)
	print("     | $$  /$$$$$$   /$$$$$$ | $$| $$ /$$/  /$$ /$$$$$$   ")
	time.sleep(0.1)
	print("     | $$ /$$__  $$ /$$__  $$| $$| $$$$$/  | $$|_  $$_/   ")
	time.sleep(0.1)
	print("     | $$| $$  \ $$| $$  \ $$| $$| $$  $$  | $$  | $$     ")
	time.sleep(0.1)
	print("     | $$| $$  | $$| $$  | $$| $$| $$\  $$ | $$  | $$ /$$ ")
	time.sleep(0.1)
	print("     | $$|  $$$$$$/|  $$$$$$/| $$| $$ \  $$| $$  |  $$$$/ ")
	time.sleep(0.1)
	print("     |__/ \______/  \______/ |__/|__/  \__/|__/   \___/   ")
	print("")
	time.sleep(0.1)
	print("")
	print("")
	time.sleep(0.1)
	print("  @@@@@@@   @@@  @@@   @@@@@@   @@@@@@@    @@@@@@    @@@@@@   @@@  @@@  ")
	time.sleep(0.1)
	print("  @@@@@@@@  @@@  @@@  @@@@@@@@  @@@@@@@@  @@@@@@@@  @@@@@@@@  @@@  @@@  ")
	time.sleep(0.1)
	print("  @@!  @@@  @@!  @@@  @@!  @@@  @@!  @@@  @@!  @@@  @@!  @@@  @@!  @@@  ")
	time.sleep(0.1)
	print("  !@!  @!@  !@!  @!@  !@!  @!@  !@!  @!@  !@!  @!@  !@!  @!@  !@!  @!@  ")
	time.sleep(0.1)
	print("  @!@@!@!   @!@!@!@!  @!@!@!@!  @!@!!@!   @!@!@!@!  @!@  !@!  @!@!@!@!  ")
	time.sleep(0.1)
	print("  !!@!!!    !!!@!!!!  !!!@!!!!  !!@!@!    !!!@!!!!  !@!  !!!  !!!@!!!!  ")
	time.sleep(0.1)
	print("  !!:       !!:  !!!  !!:  !!!  !!: :!!   !!:  !!!  !!:  !!!  !!:  !!!  ")
	time.sleep(0.1)
	print("  :!:       :!:  !:!  :!:  !:!  :!:  !:!  :!:  !:!  :!:  !:!  :!:  !:!  ")
	time.sleep(0.1)
	print("   ::       ::   :::  ::   :::  ::   :::  ::   :::  ::::: ::  ::   :::  ")
	time.sleep(0.1)
	print("   :         :   : :   :   : :   :   : :   :   : :   : :  :    :   : :  ")
	time.sleep(0.1)
	#
	# Para ajuda -help.
	print("\nPara mais informações -help")
	while(True):
		#FailSafe?.
		try:
			# MENU.
			print("___  ___ _____ _   _ _   _ ")
			print("|  \/  ||  ___| \ | | | | |")
			print("| .  . || |__ |  \| | | | |")
			print("| |\/| ||  __|| . ` | | | |")
			print("| |  | || |___| |\  | |_| |")
			print("\_|  |_/\____/\_| \_/\___/ ")
			print("")
			print("~~Ferramentas~~\n\n1. ~~Gerador de senha~\n2. ~~Calculadora~~\n")
			askUser = input("O que deseja fazer? ")
			# -help.
			if str(askUser) == "-help":
				Ajuda()
			# Para sair do programa.
			elif str(askUser) == "exit":
				print("\nSaindo do programa!")
				time.sleep(0.2)
				sys.exit()
			# Modulo Gerador de Senha.
			elif int(askUser) == 1:
				PasswordGenerator()
			# Modulo Calculadora.
			elif int(askUser) == 2:
				Calculadora()
		# Caso der algum erro.
		except ValueError:
			print("\n~~Somente as opções a cima.\nPara mais informações -help~~(teste)\n")
#                        #
# Chamando todo o programa.
main() #################
####
##
#
