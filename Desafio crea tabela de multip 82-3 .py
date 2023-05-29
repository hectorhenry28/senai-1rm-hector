numero = int(input("Digite um número par: "))

# Verifica se o número digitado é par
if numero % 2 == 0:
    print(f"Tabuada do {numero}:")
    
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")
else:
    print("O número digitado não é par.")
