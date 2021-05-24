# DESCRIÇÃO DO SISTEMA
O sistema é capaz de: A: Assinar documentos digitalmente, a partir de uma chave privada. B: Gerar certificados de dois tipos: 1: Certificados Autoassinados; C: De posse de um conjunto de certificados, verificar se um documento assinado digitalmente, é válido.

# NECESSARIO INSTALAR
pip3 install pycryptodome

# COMANDOS DE ENTRADA
* -ger - Para gerar uma assinatura digital.
* -ass - Para assinar um documento.
* -ver - Para verificar assinatura de um documento.

# EXEMPLO DE USO
Gerar Certificado Autoassinado>> python3 DigitalSignature.py -ger teste.txt
Assinar Certificado Específico>> python3 DigitalSignature.py -ass doc.txt docsigned.txt prv_key.pem
Verificar Documento Assinado >> python3 DigitalSignature.py -ver doc.txt docsigned.txt pbl_key.pem
