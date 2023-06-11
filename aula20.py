primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

print(primeiro_valor)
print(segundo_valor)

if primeiro_valor > segundo_valor:
    print(f'primeiro_valor={primeiro_valor} é maior do que segundo_valor={segundo_valor}')

elif primeiro_valor == segundo_valor:
    print(f'primeiro_valor={primeiro_valor} é igual ao segundo_valor{segundo_valor}')

elif primeiro_valor < segundo_valor:
    print(f'segundo_valor={segundo_valor} é maior do que primeiro_valor={primeiro_valor}')