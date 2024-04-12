def calcular_media(valores):
  tamanho = len(valores)  # Use len(valores) para obter o tamanho da lista
  soma = 0.0
  for valor in valores:
    soma += valor
  media = soma / tamanho
  return media

continuar = True
valores = []
while continuar:
    valor = input('Digite um número para entrar na sua média ou "ok" para calcular o valor: ')
    if valor.lower() == 'ok':
        continuar = False
    else:
        try:
            valor = float(valor)
            valores.append(valor)
        except ValueError:
            print('Valor inválido. Digite um número ou "ok".')
media = calcular_media(valores)
print('A média calculada para os valores {} foi de {}'.format(valores, media))
