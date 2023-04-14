a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if a < b + c and b < a + c and c < a + b:
    if a == b == c:
        print('Os segmentos acima PODEM FORMAR um triângulo EQUILÁTERO.')
    elif a != b != c != a:
        print('Os segmentos acima PODEM FORMAR um triângulo ESCALENO.')
    else:
        print('Os segmentos acima PODEM FORMAR um triângulo ISÓSCELES.')
else:
    print('Os Segmentos acima NÂO PODEM FORMAR triângulo!')