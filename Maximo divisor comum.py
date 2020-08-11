num1 = int(input('Digite um numero: '))
num2 = int(input('Digite mais um numero: '))

if num1 <= num2:
    menornumero = num1
    maiornumero = num2
else:
    menornumero = num2
    maiornumero = num1

resto = maiornumero % menornumero

while(resto != 0):
    maiornumero = menornumero
    menornumero = resto
    resto = maiornumero % menornumero

if menornumero == 1:
    print('Os numeros (',num1,',',num2,') são divisiveis apenas por 1, por isso, são primos')
else:
    print('Os numeros (',num1,',',num2,') Não são primos')