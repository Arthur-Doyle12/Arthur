palavra = 'Arthur'
pergunta = 'Arthur' in palavra
print(pergunta)

frase= 'Minha casa está em chamas.'
print('minha' in frase.lower())

texto = 'Este computador é bastante bom.'
quantidade = len(texto)
print(f'O texto tem {quantidade} caracters.')

texto = 'Olá Mundo.'
print(texto[0:])
print(texto[1:4])
print(texto[:5])
print(texto[-5:])
print(texto[-5:-1])

texto = 'nesse mundo em que vivemos, Devemos buscar por  nós mesmos.'
print(texto.capitalize()) #Transforma a primeira letra de uma string em maiúscula e todas as ouras em minúsculas.

texto = 'arthur pereira de lima doyle'
print(texto.title())

texto = 'a viDA É BeLA.'
print(texto.upper())

texto = 'VivER é sONhar.'
print(texto.lower())

texto = 'Computadores são úteis e interessantes. A criação de computadores revolucionol a tecnologia do mundo. Computadores.'
print(texto.count('Computadores'))

texto = 'Muitas laranjas são necessárias para fazer suco de laranja o suficiente para toda uma festa.'
print(texto.split()) #Também se pode fazer como: palavra = texto.split() -> print(palavra)

texto = 'Com 5 maçãs, nós fazemos uma torta de maçã.'
print(texto.split(','))

texto = 'Vamos terminar isso.'
print(texto.endswith('isso.')) #Normalmente usa nomes de arquivos para indentificá-los, como: 2023_relatório_final.pdf

texto = 'Vamos começar isso.'
print(texto.startswith('Vamos')) #Normalmente usa nomes de arquivos para indentificá-los, como: 2023_relatório_final.pdf

texto = 'Vamos encontrar algo.'
print(texto.find('encontrar')) #A função encontra o indice da letra, logo, neste caso foi: V0 a1 m2 o3 s4 'espaço'5 e6, sendo o 'e' a primeira letra da palavra 'encontrar'.

texto = 'Vamos encontrar algo.'
print(texto.replace('encontrar','substituir')) #Nesse caso, substituiu 'encontrar' por 'substituir'.