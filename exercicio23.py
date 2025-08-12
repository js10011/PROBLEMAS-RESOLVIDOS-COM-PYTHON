
try:
    horas = float(input("Digite as horas trabalhadas: "))
    taxa = float(input("Digite o valor da hora: "))
    pagamento = horas * taxa
    print(f"Pagamento: R$ {pagamento:.2f}")
except:
    print("Error: Utilize numero")
