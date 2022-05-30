####################################################################################################################
#                     Algoritmo para criar uma senha com 16 caracteres que permite apenas 3 números                #
####################################################################################################################

import string
import random

qtd_caracteres_totais = 16
qtd_numeros_permitidos = 3
senha = ''

for i in range(qtd_caracteres_totais):
    caractere = random.choice(string.ascii_letters + string.digits)
    
    # verifica se é um número
    if(caractere in string.digits):
        # print(f'É um número: {caractere}')

        # se ainda for permitido número a senha recebe
        if(qtd_numeros_permitidos > 0):
            senha += caractere
        else: 
            # sorteia uma letra caso não mais permitido número
            senha += random.choice(string.ascii_letters)
        
        # diminui a quantiade de números permitidos
        qtd_numeros_permitidos -= 1
    else:
        # se não for número recebe a letra
        senha += caractere

print(f'Senha: {senha}')