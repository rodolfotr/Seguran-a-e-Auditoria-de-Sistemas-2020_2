"""
#DESCRIÇÃO DO SISTEMA
O sistema é capaz de:
	A: Assinar documentos digitalmente, a partir de uma chave privada.
	B: Gerar certificados de dois tipos:
		1: Certificados Autoassinados;
	C: De posse de um conjunto de certificados, verificar se um documento assinado digitalmente, é válido.

#NECESSARIO INSTALAR
pip3 install pycryptodome

#COMANDOS DE ENTRADA
-ger <certificate file> - Para gerar uma assinatura digital.
-ass <normal doc file> <assigned text file> <PrivateKey file> - Para assinar um documento
-ver <normal doc file> <public key file> <PublicKey file>- Para verificar assinatura de um documento

#EXEMPLO DE USO
Gerar Certificado Autoassinado>> python3 trab01_CertDig.py -ger teste.txt
Assinar Certificado Específico>> python3 trab01_CertDig.py -ass doc.txt docsigned.txt prv_RodolfoTrevisol.pem
Verificar Documento Assinado>> python3 trab01_CertDig.py -ver doc.txt docsigned.txt pbl_RodolfoTrevisol.pem
"""

from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Signature import pkcs1_15

import sys
import ast
import random
import time

arg1 = None
arg2 = None
arg3 = None

try:
	command = sys.argv[1]
	arg1 = sys.argv[2]

	if len(sys.argv) == 5:
		arg2 = sys.argv[3]
		arg3 = sys.argv[4]
except:
	print("Comandos de entrada:")
	print("-ass <normal text file> <assigned text file> - Para assinar um documento")
	print("-ver <assigned text file> - Para verificar assinatura de um documento")
	sys.exit()

#Geração de Certificados Autoassinados
if  command == "-ger":
	#Nome do certificado.
	file_e = arg1
	
	#Credenciais do usuário.
	name = input("Digite seu nome!\n")
	born_dt = input("Digite sua data de nascimento (apenas números, formato DDMMAAAA)\n")
	num_id = input("Digite um número de identificação (CPF)\n")

	#Credenciais randomizadas.
	certif_text = born_dt + name + str(int(time.time())) + num_id
	certif_text = ''.join(random.sample(certif_text, len(certif_text)))

	#Geração das chaves Privada e Publica.
	key = RSA.generate(2048)
	private_key = key.export_key()
	file_out = open("prv_"+name.replace(" ","")+".pem", "wb")
	file_out.write(private_key)

	public_key = key.publickey().export_key()
	file_out = open("pbl_"+name.replace(" ","")+".pem", "wb")
	file_out.write(public_key)
	
	#Hash das credenciais.
	hash_txt = SHA256.new(certif_text.encode('utf-8'))
	
	#Assinatura (Cifra) das credenciais usando as chaves geradas.
	digitalSign = pkcs1_15.new(key).sign(hash_txt)
	
	file_e = open(file_e, 'w')
	file_e.write(certif_text)
	file_e.write('Hash: ')
	file_e.write(hash_txt.hexdigest())
	file_e.write('\r\n')
	file_e.write(public_key.decode('utf-8'))
	file_e.write('\r\n')
	file_e.write(str(digitalSign))
	print('Certificado gerado com sucesso!!\n')

#Assinar
elif  command == "-ass":
	#Nome dos arquivos utilizados.
	file_n = arg1	#Documento Original.
	file_e = arg2	#Documento Assinado.
	file_c = arg3	#PrivateKey para Assinatura.

	#Leitura do documento.
	with open(file_n,'r') as doc: out = doc.read()
	
	#Assinatura do documento usando Chave Privada.
	with open(file_c,'r') as file_c: key = file_c.read()

	key = RSA.import_key(key)
	public_key = key.publickey().export_key()
	
	#Hash do Documento Original.
	hash_doc = SHA256.new(out.encode('utf-8'))
	
	#Assinatura com a chave.
	digitalSign = pkcs1_15.new(key).sign(hash_doc)
	
	if file_e:
		file_e = open(file_e, 'w')
		file_e.write(str(digitalSign))
		print('Documento assinado com sucesso!!\n')
	else:
		print(out,'\n')
		print('Hash: ')
		print(hash_doc.hexdigest())
		print('\n')
		print(public_key)
		print('\n')
		print(digitalSign)

#Verificar
elif  command == "-ver":
	#Nome dos arquivos utilizados.
	file_n = arg1	#Documento Original.
	file_e = arg2	#Documento Assinado.
	file_c = arg3	#PublicKey para Verificação.

	#Leitura do Documento Original.
	with open(file_n,'r') as doc: out = doc.read()

	#Leitura do Documento Assinado.
	with open(file_e,'r') as doc: signed = doc.read()
	
	#Leitura da Chave Publica.
	with open(file_c,'r') as file_c: key = file_c.read()
	
	#Hash do Documento Original.
	hash_doc = SHA256.new(out.encode('utf-8'))
	
	#Assinatura com a chave.
	key = RSA.import_key(key.encode('utf-8'))
	h = SHA256.new(out.encode('utf-8'))
	signature = ast.literal_eval(signed)
	
	#Verificação da Assinatura.
	try:
		pkcs1_15.new(key).verify(h, signature)
		print("Assinatura OK.")
	except (ValueError, TypeError) as e:
		print("Falha.",e)
