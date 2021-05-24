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
