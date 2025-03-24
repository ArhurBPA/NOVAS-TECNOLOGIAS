import math

#Questao 1
print("""                                
                                                     *
        * * *  * * *             *   *             * * *            *
        *          *         *           *        * * * *         *   *
        *          *         *           *           *          *       *
        * * *  * * *             *   *               *            *   *
                                                     *              *
""")

#Questao 2

num = int(input('Digite cinco núeros: '))
if 10000 <= num <= 99999:
    dig1 = num // 10000
    dig2 = (num % 1000) // 10
    dig3 = (num % 100) // 10
    dig4 = (num % 10) // 10
    dig5 =  num // 10
else:
    print("Numero invalido")
#Questao 3
xA = int(input('Digite o valor da a coordenada x no ponto A: '))
yA = int(input('Digite o valor da a coordenada y no ponto A: '))

xB= int(input('Digite o valor da a coordenada x no ponto B: '))
yB = int(input('Digite o valor da a coordenada y no ponto B: '))

distancia = math.sqrt((xB - xA) ** 2 + (yB - yA) ** 2)

print(f'O resultado é {distancia:.2f}')
#Questao 4


#Questao 5
msg = input("Digite a mensagem: ")
msgCript=""
for digito in msg:
    msgCript +=str((int(digito) + 7) %10)

print("Criptografada: " + msgCript [2] + msgCript [3] +msgCript [0] + msgCript [1])

msgDesCript=""
for digito in msgCript:
    msgDesCript+=str((int(digito) + 3)%10)
print("Descriptografada: " + msgDesCript)