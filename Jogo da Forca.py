# Exercicio Programa 2: João Pedro, Lucas Monteiro
#ADS 1°B 2016

# coding=<nome da codificação>
print('O jogo começara em breve, aguarde alguns instantes!')
def escolhe():
    import urllib.request
    page = urllib.request.urlopen ('http://www.ime.usp.br/~pf/dicios/br')
    palavra = page.read().decode ("iso8859").split()
    condição(palavra)

def condição(palavra):
    import random
    global letras
    global secreta
    secreta = random.choice(palavra)
    global corretas
    global erradas
    corretas = ''
    erradas = ''
    totalcorretas = ''
    letras = ''
    print('ESTE É O JOGO DA FORCA!')
    print('É bem fácil! Chute letras até acertar a palavra.\nAviso: Só poderá errar 6 vezes.')
    print('Lembre-se a palavra escolhida pode ter acento.\nCaso isso aconteça você deverá colocar a letra correta ACENTUADA.')
    if len(palavra) < 5:
        random.choice(palavra)
    else:
        desenha(secreta,corretas,erradas,totalcorretas,letras,palavra)


def desenha(secreta,corretas,erradas,totalcorretas,letras,palavra):
    global forca
    forca = [ '''

    +------------+
    |            |
                 |
                 |
                 |
                 |
                 |
   =============== ''', '''


    +------------+
    |            |
    O            |
                 |
                 |
                 |
                 |
   =============== ''', '''

   
    +------------+
    |            |
    O            |
    |            |
                 |
                 |
   =============== ''' , '''


    +------------+
    |            |
    O            |
   /|            |
                 |
                 |
   =============== ''' , '''

    +------------+
    |            |
    O            |
   /|\           |
                 |
                 |
                 |
   =============== ''' , '''

    +------------+
    |            |
    O            |
   /|\           |
   /             |
                 |
   =============== ''' , '''


    +------------+
    |            |
    O            |
   /|\           |
   / \           |
                 |
   =============== ''' ]
    
    print(forca[len(erradas)-1])
    for x in secreta:
        print('_', end = ' ')
    chute(secreta,corretas,erradas,totalcorretas,letras,palavra)


def chute (secreta,corretas,erradas,totalcorretas,letras,palavra):
    global letra
    letra = str(input('\nDigite a letra: '))
    letra = letra.upper().lower()
    if letra in letras:
        print('Você já digitou essa letra. Digite outra.')
        return chute(secreta,corretas,erradas,totalcorretas,letras,palavra)
    else:
        if len(letra) != 1:
            print('Somente 1 letra')
            return chute(secreta,corretas,erradas,totalcorretas,letras,palavra)
        else:
            if letra.isalpha():
                coloca_letra (secreta,corretas,erradas,totalcorretas,letras,palavra)
            else:
                print('Só pode ser usada letras!')
                chute(secreta,corretas,erradas,totalcorretas,letras,palavra)

def coloca_letra(secreta,corretas,erradas,totalcorretas,letras,palavra):
    count = 0
    while count < 6:
        if letra in secreta:
            corretas = corretas + letra
            print (forca[len(erradas)-1])
            posição = 0
            while posição < len(secreta):
                if letra == secreta[posição]:
                    totalcorretas = totalcorretas + letra
                posição = posição + 1
            print('\n\nAs letras corretas são: ', totalcorretas)
        else:
            erradas = erradas + letra
            count = count + 1
            if len(erradas) <= 6:
                print (forca[len(erradas)-1])
            else:
                print ('Fim de Jogo! O computador venceu, boa sorte na próxima!')
                print('A palavra é essa: ', secreta,' chefe!')
                jogar_novamente(palavra)
        for x in secreta:
            if x in corretas:
                print (x, end = ' ')
            else:
                print ('_', end = ' ')
        letras = corretas + erradas
        print ('\nAs letras já colocadas são: ', letras)
        if len(totalcorretas) == len(secreta)+1:
            ganhou(palavra)
        else:
            chute(secreta,corretas,erradas,totalcorretas,letras,palavra)
    jogar_novamente(palavra)
            
def jogar_novamente(palavra):
    jogar_novamente= input('Quer jogar novamente? sim ou não ')
    while jogar_novamente != 'sim' and jogar_novamente != 'não':
        print('Cara, é só sim ou não!')
        jogar_novamente = input ("Quer jogar mais uma vez? sim ou não: ")    
    if jogar_novamente == 'sim':
        return True
        print('Então bora pra mais um jogo')
        condição(palavra)
    elif jogar_novamente == 'não':
        return False
        print('Obrigado por jogar!')
        game_over()
    
def ganhou(palavra):
    print('Parabéns, você foi o ganhador dessa rodada!')
    jogar_novamente(palavra)

def game_over():
    import os
    print ('Game Over!')
    os.exit(0)
escolhe()