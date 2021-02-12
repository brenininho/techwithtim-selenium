# divisão com casa decimal usa somente uma barra"/"
# sem casa decimal usa duas barras "/"
#
# While True: - executa tudo que está dentro do código para sempre.
#
# input - para o comando e pede para de digite na tela.
#
# eval - executa a variável como se fosse código.
#
# print - mostra o código na tela.
#
# ","(vírgula) - da um espaço.
#
# ""(aspas simples ou duplas) - indica que há um texto dentro da aspas.
#
# int - para escrever números inteiros.
#
# float - para escrever números com vírgula.
#
# repetição - escrever um texto e multiplica-lo por um número, irá exibi-lo pelo número de vezes do número.
# print("5"*2) exibe: 55
#
# Contatenar - número tratado como texto
# print("soma de 5+5 é: ", "5+5"
#
# Python diferencia letras maíusculas de minúsculas
# print( "minúsculo")
# Print(" maiúscula da erro") #erro
#
"""
operadores aritmeticos
+  Sinal de mais               Adição/Concatenação
-  Sinal de menos              Subtração
*  Asterístico                 Multiplicação/Repetição
/  barra                       Divisão
// duas barras                 Divisão com resultado inteiro
%  sinal de porcentagem        Módulo (resto de divisão)
**
"""
# print("Variáveis--------------------------------------")
#
# print("Variáveis tipos: ''(string), 0(int), <>=(booleano),")
#
# print("Variáveis tipos: ''(string), 0(int), <>=(booleano),")
# print("somente utilizar letras minúsculas nas variáveis, ")
# print("só consegue dar espaço na variável com _(underline)")
# nome_composto = "Breno Valle"
# print(nome_composto)
#
"""
.format------------------------------------------------------

.format serve para organizar as variáveis dentro da string
"""
#
# print("primeira forma de se escrever")
# nome = "Breno Valle"  #string
# idade = 16  #int
# altura = 1.70  # float
# peso = 63 # int
#
# print("{} tem {} mede {} e pesa {}" .format(nome, idade, altura, peso))
#
# print("segunda forma de escrever")
# dono = 'Breno'
# máscaras = 100
# asilos = 2
#
# print( '{d}, Dono de asilo, comprará {m} máscaras e distribuirá em seus {a} asilos'.format(a=asilos, m=máscaras, d=dono))
#
# print("melhor forma de escrever")
#
# print( f'{dono}, Dono de asilo, comprará {máscaras} e distribuirá em seus {asilos} asilos')
#
# print(" ''' '''     três parênteses     possibilita a quebra de linha em textos grandes")
#
# cliente = 'Roberto'
# idoso = 'José'
# preco = 'R$2000'
# texto = f'''{cliente} confiou no Asilo da Prata
# para deixar seu pai, {idoso}, conosco por {preco}, tamo rico.'''
# print(texto)
#
"""
Tipos de dados----------------------------------------------

int - números inteiros (positívos, negativos e zero)
float - números reais, com ponto (positivos ou negativos)
bool - valor lógico (booleana) - True = Verdadeiro, False = Falso)
str - String ou cadeia de caracteres (texto)
"""
#
# print('soma de int com float')
# inteiro = 10 # int
# real = 2.5
# booleano = True  #bool
# texto = "5.5" #str
#
# print(inteiro + real)
#
# print(inteiro + float(texto))
#
# clientes = 20
# fatura = 2000
# funcionarios = 20
# salário = 1100
# multiplicação = (clientes*fatura)
# divisor = (funcionarios*salário)
# total = (multiplicação-divisor)
#
# print(f"O lucro total é de {total}")
#
# lucro = (clientes*fatura) - (funcionarios*salário)
# print( (clientes*fatura) - (funcionarios*salário))
#
# nome = 'Roberto'
# sobrenome = 'Nobre'
# idade = 25
# altura = 1.70
# peso = 70
# ano_nascimento = 1996
# print(f'''Este é o {nome} {sobrenome}. Ele nasceu em {ano_nascimento} e tem
# {idade} anos. {nome} {sobrenome} tem {altura} de altura e pesa {peso} kilos.''')
#
#
"""
Entrada de Dados - Aula 3 ------------------------------------------------------
"""
#
# nome = input('Qual o seu nome? ')
# idade = input("QUal a sua idade? ")
# ano_nascimento = 2021-int(idade)
#
# print(f'{nome} tem {idade} e nasceu em {ano_nascimento}')
#
"""
Condições IF, ELIF E ELSE - Aula 4 ------------------------------------------------
"""
#
# if False:
#     print('verdadeiro.')
# elif True:
#     print('Sábado é final de semana')
# else:
#     print('não é verdadeiro.')
#
"""
OPeradores Relacionais - Aula 4 Parte 2 --------------------------------------------

== pergunta se é igual
>  maior que
>= mair que ou igual a
<  menor que
<= menor que ou igual a
!= dirente
"""
#
# nome = input('Qual o seu nome ? ')
# idade = input('Qual a sua idade ? ')
# idade = int(idade)
#
# idade_limite = 18
#
# if idade >= idade_limite:
#     print(f'{nome} pode financiar.')
# else:
#     print(f'{nome} não pode financiar')
#
"""
Operadores lógicos - Aula 4-----------------------------------------------
and, or, not
in e not in
"""
#
# nome = 'Breno Valle'
#
# if 'valle' in nome:
#     print('Existe no texto')
# else:
#     print('Não existe no texto')
#
# usuario = input('Digite o seu nome de usuario ')
# senha = input('Digite a sua senha ')
#
# login = 'Breno'
# senha_l = '123'
#
# if login == usuario and senha_l == senha:
#     print('Conectado com sucesso')
# else:
#     print('nome de usuario ou senha incorreta')
#
"""
Formatando valores com modificadores - Aula 5----------------------------
:s - Texto (strings)
:d - inteiros (int)
:f - números de ponto flutuante (float)
:.(número)f - quantidade de casas decimais (float)
:(caractere)(> ou < ^)(quantidade)(tipo) - s, d ou f)

> - Esquerda
< - Direita
^ - Centro
"""
#
# num_1 = 5
# num_2 = 3
# divisao = num_1 / num_2
#
# print(f'{num_2:d}')
#
"""
Manipulando strings - Aula 6 ----------------------------------------
*String indices
*Fatiamento de strings [inicio:fim:passo]
*funções built-in len, abs, type, print, etc...
Essas funções podem ser usadas diretamente em cada tipo.
"""
#
# # positivo   [01234]
# texto =      'Breno'
# # negativos  [54321]
# texto2 = texto[0:3]
# print(texto2)
#
"""
while em Python - Aula 7---------------------------------------
utilizando para realizar ações enquanto
uma condição for verdadeira
"""
#
# x = 0
# while x <= 4:
#     if x == 3:
#         x = x + 1
#         continue
#     print(x)
#     x = x + 1
# print('Fim')
#
"""
While / else - Aula 8----------------------------------------
contadores
acumuladores
"""
#
# contador = 1
# acumulador = 1
# while contador <= 10:
#     print(contador, acumulador)
#     acumulador = acumulador + contador
#     contador += 1
# else:
#     print('Cheguei no else.')
#
"""
Iterando strings com while em Python Aula 9 -----------------------------------------
"""
#
# minha_string = "leve já o seu velhinho ao Asilo da Prata"
# tamanho_string = len(minha_string)
#
# c = 0
# nova_string = ''
# while c < tamanho_string:
#
#     if minha_string[c] == 'r':
#         nova_string += minha_string[c].upper()
#     else:
#         nova_string += minha_string[c]
#     c += 1
# print(minha_string)
#
# minha_string = "leve já o seu velhinho ao Asilo da Prata"
# tamanho_string = len(minha_string)
#
# c = 0
# contagem_atual = 0
# letra = ''
# while c < tamanho_string:
#     qtd_vezes_letra = minha_string.count(minha_string[c])
#
#     if contagem_atual < qtd_vezes_letra and minha_string[c].strip():
#         letra = minha_string[c]
#         contagem_atual = qtd_vezes_letra
#
#     print(minha_string[c], qtd_vezes_letra)
#
#     c += 1
# print(letra, contagem_atual)
#
#
"""
For in em Python Aula 10 -----------------------------------------------------------
Iterando string com for
Função range(start=0, stop, step=1
"""
#
# string = 'Eu uso varinha'
#
# for letra in string:
#     print(letra)
#
# for c in range(0, 10, 1):
#     print(c)
#
#
# string = 'Eu como carne.'
# nova_string = ''
#
# for letra in string:
#     if letra == 'c':
#         nova_string += letra.upper()
#     elif letra == 'o':
#         nova_string += letra.upper()
#     else:
#         nova_string += letra
#
# print(nova_string)
#
#
#
"""
Listas em Python Aula 11 -------------------------------------------------------------
fatiamento
append, insert, pop, del, clear, extend, +
min, max
range
"""
# #         0    1    2    3    4    5    6
# lista = ['A', 'B', 'C', 'D', 'E', True, 10.5]
# #      -  7    6    5    4    3    2    1
# print(lista[::2])
#
#
# l1 = [1, 2, 3]
# l2 = [4, 5, 6]

# l2.pop() exclui o último valor da lista
# l1.extend(l2) adiciona os valores de outra variável na lista
# l2.append('b') adiciona um valor no final da lista
# l2.insert(0, 'pão') Adiciona um valor em uma posição X da lista e empurra os itens depois da posição X
# del(l2[0]) exclui determinado valor(es) da lista
# print(max(l2))
# print(min(l2))
#
# print(l2)
#
# l3 = list(range(0, 100, 7))
# print(l3)

# l4 = 'Breno', False, 5, 1.2
# for val in l4:
#     print(f'O tipo de elemento é {type(val)} e o seu valor é {val}')
#
# --------------------------------------------------------------------
# secreto = 'mochila'
# digitadas = []
# chances = 3
#
# while True:
#     if chances == 0:
#         print('Você perdeu.')
#         break
#
#     letra = input('Digite uma letra: ')
#
#     if len(letra) > 1:
#         print('Isso não vale, digite somente uma letra por vez. ')
#         continue
#
#     digitadas.append(letra)
#
#     if letra in secreto:
#         print(f'Bom palpite, a letra "{letra}" existe na palavra secreta.')
#     else:
#         print(f'Infelizmente a letra "{letra}" não existe na palavra secreta.')
#         digitadas.pop()
#     secreto_temporario = ''
#     for letra_secreta in secreto:
#         if letra_secreta in digitadas:
#             secreto_temporario += letra_secreta
#         else:
#             secreto_temporario += '*'
#
#         if secreto_temporario == secreto:
#             print(f'Você acertou! a palavra correta é {secreto}.')
#             break
#     print(f'A palavra secreta está assim: {secreto_temporario}')
#
#     if letra not in secreto:
#         chances -= 1
#
#     print(f'você tem {chances} chances.')
#     print()
#
#
"""
For / Else em Python
"""
# variavel = ['luiz Otávio', 'Joãozinho', 'Maria']
#
# for valor in variavel:
#     if valor.startswith('J'):
#         print(f'{valor} começa com J.')
#     else:
#         print(f'{valor} não começa com J.')
#
#
# variavel = ['luiz Otávio', 'Joãozinho', 'Maria']
#
# comeca_com_j = False
# for valor in variavel:
#     if valor.lower().startswith('j'):
#         comeca_com_j = True
#
# if comeca_com_j:
#     print('Existe uma palavra que começa com J.')
# else:
#     print('Não existe uma palavra que começa com J.')
#
#
# variavel = ['luiz Otávio', 'Joãozinho', 'Maria']
#
# for valor in variavel:
#     if valor.lower().startswith('j'):
#         continue
#     print(valor)
#
#
"""
Split, Join, Enumerate em Python Aula 13 --------------------------------------------------
* Split - Dividir uma string # str
* Join - Juntar uma lista # str
* Enumerate - Enumerar elementos da lista # iteráveis
"""
#
# string = "O Brasil é o país do futebol, o Brasil é penta."
# lista1 = string.split(' ')
#
# palavra = ''
# contagem = 0
# for valor in lista1:
#     qtd_vezes = lista1.count(valor)
#
#     if qtd_vezes > contagem:
#         contagem = qtd_vezes
#         palavra = valor
#
# print(f'A palavra que apareceu mais vezes é {palavra} ({contagem}x)')
#
#
# string = 'O Brasil é penta.'
# lista = string.split(' ')
# string2 = ' '.join(lista)
#
# print(string)
# print(lista)
# print(string2)
#
#
# lista = ['Luiz', 'João', 'Maria']
#
# for indice, nome in enumerate(lista):
#     print(indice, nome)
#
#
# lista = ['Luiz', 'João', 'Maria']
#
# n1, n2, n3 = lista
#
# print(n2)
#
#
"""
Desempacotamento de listas em Python Aula 14 ----------------------------------------------
"""
#
# lista = ['Luiz', 'João', 'Maria', 1, 2, 3, 4, 5]
#
# n1, n2, n3, *resto_da_lista = lista
#
# print(n1, n2, n3)
#
#
"""
Operador ternário em Python Aula 15 --------------------------------------------------------
"""

# logged_user = True
# msg = 'Usuário logado.' if logged_user else 'usuário precisa logar.'
#
# print(msg)
#
# idade = input('Ensira sua idade ')
#
# if not idade.isnumeric():
#     print('Você precisa digitar um número.')
# else:
#     de_maior = (int(idade) >= 18)
#     msg = 'Pode acessar.' if de_maior else 'Não pode acessar.'
#     print(msg)
#
#
"""
Funções - def em Python Aula 16 (Parte 01) ---------------------------------------------------
"""
#
# def saudacao():  # eu posso colocar qualquer nome para o "def" transformar em uma função
#     print('Asilo da Prata!')
#
# saudacao()
#
#
# def saudacao(msg='Olá',vocativo='clientela'):
#     vocativo = vocativo.replace('e', '3')
#     msg = msg.replace('O', '0')
#     print(msg, vocativo)
#
# saudacao()
#
#
"""
Funções (def) em Python - return - Aula 16 (Parte 2) --------------------------------
"""
# def divisao(n1, n2):
#     if n2 > 0:
#         return n1 / n2
#
# divide = divisao(8, 0)
# if divide:
#     print(divide)
# else:
#     print('Conta inválida.')
#
#
"""
Funções (def) em Python - *args **kwargs - Aula 16 (Parte 3)------------------------
"""
#
# def func(*args, **kwargs):
#     print(args)
#
#     idade = kwargs['idade']
#     print(idade)
#
# lista = [1,2,3,4,5]
# lista2 = [10,20,30,40,50]
# func(*lista, *lista2, nome='Luiz', sobrenome='Miranda', idade=30)
#
#
"""
Escopo de variáveis de funções em Python - Global e Local - Aula 16 (Parte 04) ---------------------

qualquer variável que estiver dentro de uma função não pode ser acessada por outra função, porém
se usar a função "return" é possível dar o valor da variavel(que não podia ser acessada) para uma nova
 variável e assim, acessa-la..
"""
#
# def func():
#     variavel = 'Breno Valle'
#     return variavel
#
#
# def func2(arg):
#     print(arg)
#
# var = func()
# func2(var)
#
#
"""
Expressões lambda(funções anônimas) em Python - Aula 17
"""
#
# a = lambda x, y: x * y
#
# print(a(2, 2))
#
#
# lista = [
#     ['P1', 13],
#     ['P2', 6],
#     ['P3', 15],
#     ['P4', 23],
#     ['P5', 39],
# ]
# # .sort - ordena os valores da lista do menor para o maior.
# lista.sort(key=lambda item: item[1])
# print(lista)
'''
------------OU------------
'''
# print(sorted(lista, key=lambda i: i[1], reverse=False))
#
#
"""
Tuplas em Python - Aula 18 --------------------------------------------------------------------
não pode adicionar nem remover elementos e não pode mudar o valor do índice da tupla, porém
eu posso transformar a tupla em lista, mudar/adicionar/remover o elemento e depois transformar
em uma tupla novamente.
"""
# t1 = (1, 2, 3, 4, 5)
# t1 = list(t1)
# t1[1] = 3000
# t1 = tuple(t1)
#
# print(t1)
#
#
"""
Trocando o valor entre variáveis em Python - Aula 19 ----------------------------------------------
"""
# x = 10 # Breno
# y = 'Breno' # 10
# x, y = y, x
#
# print(f'O valor de x é {x} e o valor de y é {y}.')
#
#
"""
Dicionário em Python - Aula 20 -------------------------------------------
"""

# d1 = {
#  #   chave        valor
#     'chave' : 'valor da chave',
#     'casa':'388',
# }
#
# for k, v in d1.items():
#     print(k, v)


# clientes = {
# #    usuário do cliente
#     'eoroico' : {
#         'nome' : 'Breno',
#         'sobrenome' : 'Valle'
#     },
#     'brenova' : {
#         'nome' : 'Marcio',
#         'sobrenome' : 'Valle'
#     },
# }
#
# for clientes_k, clientes_v in clientes.items():
#     print(f'Exibindo {clientes_k}')
#     for dados_k, dados_v in clientes_v.items():
#         print(f'    {dados_k} = {dados_v}')


"""
Sistema de perguntas e respostas com dicionários em Python - Aula 21 ----------------
"""

# perguntas ={
#     'pergunta1': {
#         'pergunta': 'Quanto é 4+4? ',
#         'respostas': {'a': '8', 'b': '10', 'c': '5', },
#         'resposta_certa': 'a',
#     },
#     'pergunta2': {
#         'pergunta': 'Quanto é 3*3? ',
#         'respostas': {'a': '8', 'b': '10', 'c': '9', },
#         'resposta_certa': 'c',
#     },
# }
#
# respostas_certas = 0
# for pk, pv in perguntas.items() :
#     print(f'{pk}: {pv["pergunta"]}')
#
#     print('Alternativas: ')
#     for rk, rv in pv['respostas'].items():
#         print(f'[{rk}]: {rv}')
#
#     resposta_usuario = input('Sua resposta: ')
#
#     if resposta_usuario == pv['resposta_certa']:
#         print('Isso mesmo, você acertou!!!')
#         respostas_certas += 1
#     else:
#         print('Nada disso, você errou!!!')
#
#     print()
#
# qtd_perguntas = len(perguntas)
# porcentagem_acerto = respostas_certas / qtd_perguntas * 100
#
# print(f'Você acertou {respostas_certas} respostas.')
# print(f'Sua porcentagem de acerto foi de {porcentagem_acerto}%.')


"""
Sistema de perguntas e respostas com dicionários em Python - Aula 21 ----------------
"""

# perguntas ={
#     'pergunta1': {
#         'pergunta': 'Quanto é 4+4? ',
#         'respostas': {'a': '8', 'b': '10', 'c': '5', },
#         'resposta_certa': 'a',
#     },
#     'pergunta2': {
#         'pergunta': 'Quanto é 3*3? ',
#         'respostas': {'a': '8', 'b': '10', 'c': '9', },
#         'resposta_certa': 'c',
#     },
# }
#
# respostas_certas = 0
# for pk, pv in perguntas.items() :
#     print(f'{pk}: {pv["pergunta"]}')
#
#     print('Alternativas: ')
#     for rk, rv in pv['respostas'].items():
#         print(f'[{rk}]: {rv}')
#
#     resposta_usuario = input('Sua resposta: ')
#
#     if resposta_usuario == pv['resposta_certa']:
#         print('Isso mesmo, você acertou!!!')
#         respostas_certas += 1
#     else:
#         print('Nada disso, você errou!!!')
#
#     print()
#
# qtd_perguntas = len(perguntas)
# porcentagem_acerto = respostas_certas / qtd_perguntas * 100
#
# print(f'Você acertou {respostas_certas} respostas.')
# print(f'Sua porcentagem de acerto foi de {porcentagem_acerto}%.')


"""
Sets em Python Aula 22 ------------------------------
add(adiciona), update (atualiza), clear, discard
union  (une)
intersection & (todos os elementos presentes nos dois sets)
difference - (elementos apenas no set da esquerda)
symmetricdifference ^ (elementos que estão nos dois sets, mas não em ambos)
"""
# remove os duplicados
# s1 = {1, 2, 3, 4, 5, 6, 6, 6, 6, 6, 7, 8, 9, 'Breno', 'Breno'}
#
# print(s1)

"""
List Comprehension em Python - (Compreensão de lista) - Aula 23 ----------------
"""

# l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# ex1 = [variavel for variavel in l1]
#
# ex2 = [v * 2 for v in l1]
# ex3 = [(v, v2) for v in l1 for v2 in range(3)]
#
# l2 = ['Breno', 'Mauro', 'Maria']
# ex4 = [v.replace('a', '@').upper() for v in l2]
#
# tupla = (
#     ('chave', 'valor'),
#     ('chave2', 'valor2'),
# )
#
# ex5 = [(y, x) for x, y in tupla]
# ex5 = dict(ex5)
#
# l3 = list(range(100))
# ex6 = [v for v in l3 if v % 3 == 0 if v % 8 == 0]
#
# ex7 = [v if v % 3 == 0  and v % 8 == 0 else 0 for v in l3]
# print(ex7)


"""
Dictionary Comprehension em Python - (Compreensão de dicionários) - Aula 24 --------
"""

# l1 = [1, 2, 3, 4, 5, 6]
# l2 = [v * 2 for v in l1]
# print(l2)


# lista = [
#     ('chave', 'valor'),
#     ('chave2', 'valor2'),
# ]
#
# d1 = {x.upper(): y.upper() for x, y in lista}
# print(d1)


# d1 = {f'chave{x}': x**2 for x in range(5)}
# print(d1, type(d1))


"""
List Comprehension em Python - (Compreensão de lista) - Aula 23 ----------------
"""

# l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# ex1 = [variavel for variavel in l1]
#
# ex2 = [v * 2 for v in l1]
# ex3 = [(v, v2) for v in l1 for v2 in range(3)]
#
# l2 = ['Breno', 'Mauro', 'Maria']
# ex4 = [v.replace('a', '@').upper() for v in l2]
#
# tupla = (
#     ('chave', 'valor'),
#     ('chave2', 'valor2'),
# )
#
# ex5 = [(y, x) for x, y in tupla]
# ex5 = dict(ex5)
#
# l3 = list(range(100))
# ex6 = [v for v in l3 if v % 3 == 0 if v % 8 == 0]
#
# ex7 = [v if v % 3 == 0  and v % 8 == 0 else 0 for v in l3]
# print(ex7)


"""
Dictionary Comprehension em Python - (Compreensão de dicionários) - Aula 24 --------
"""

# l1 = [1, 2, 3, 4, 5, 6]
# l2 = [v * 2 for v in l1]
# print(l2)


# lista = [
#     ('chave', 'valor'),
#     ('chave2', 'valor2'),
# ]
#
# d1 = {x.upper(): y.upper() for x, y in lista}
# print(d1)


# d1 = {f'chave{x}': x**2 for x in range(5)}
# print(d1, type(d1))


"""
Geradores, Iteradores e Iteráveis em Python - Aula 25 ---------------------
"""

# import sys
# import time
#
# def gera():
#     for n in range(100):
#         yield n
#         time.sleep(0.1)
#
# g = gera()
#
# print(g)

import time

# def gera():
#     variavel = 'valor 1'
#     yield variavel
#     variavel = 'valor 2'
#     yield variavel
#     variavel = 'valor 3'
#     yield variavel
#
# g = gera()
#
# for v in g:
#     print(v)
