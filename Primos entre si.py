num1 = int(input('Digite um numero: '))
num2 = int(input('Digite mais um numero: '))

divisao = 0

if num1 <= num2:
    menornumero = num1
    maiornumero = num2
else:
    menornumero = num2
    maiornumero = num1

for i in range(1,menornumero+1):
    if menornumero % i == 0:
        if maiornumero % i == 0:
            divisao += 1

print('Os numeros (',num1,',',num2,') são divisiveis',divisao,'vez(es)')

if divisao == 1:
    print('Por isso eles são primos')
else:
    print('Por isso eles não são primos')
