# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.

num1 = int(input("Digite o primeiro número: "));
num2 = int(input("Digite o segundo número: "));
operacao = input("Digite a operação (+, -, *, /): ");

if operacao == "+":
    print(num1 + num2);
elif operacao == "-":
    print(abs(num1 - num2));
elif operacao == "*":
    print(num1 * num2);
elif operacao == "/":
    if num2 != 0 and num1 != 0:
        print(num1 / num2);
    else:
        print("Erro: Divisão por zero não é permitida.");
else:
    print("Erro: Operação inválida.");
