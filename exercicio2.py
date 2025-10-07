

'''Escreva um programa que solicite ao usuário um número inteiro, um número float e uma string.
Em seguida, converta o número inteiro para float, o número float para string, e a string para número inteiro.
Exiba os resultados das conversões e seus tipos.'''

inteiro = int(18)
floati = float(12.5)
strin = str("17")

inte_para_float = float(inteiro)
float_para_str = str(floati)
stri_para_int = int(strin)

print(f"Inteiro para float: {inte_para_float}, {type(inte_para_float)}")
print(f"float para string: {float_para_str},  {type(float_para_str)}")
print(f"String para  inteiro: {stri_para_int},  {type(stri_para_int)}")