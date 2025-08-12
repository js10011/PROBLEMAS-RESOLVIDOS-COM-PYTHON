#qual o volume de uma esfera com raio de 5
 #V = (4/3)πr³

v = 4 * 3.14 * (5**3)/3
print(v)

'''
Suponha	que	o	preço	de	capa	de	um	livro	seja	R$	24,95,	mas	as	livrarias	recebem	um
 desconto	de	40%.	O	transporte	custa	R$	3,00	para	o	primeiro	exemplar	e	75	centavos
 para	cada	exemplar	adicional.	Qual	é	o	custo	total	de	atacado	para	60	cópias?
'''
preco = 24.95
desconto = 0.40
preco_unitario = preco * (1 - desconto)

transporte = 3.00 + 0.75 * (60 - 1)

custo_total = 60 * preco_unitario + transporte
print(f"Custo total para 60 copias: R$ {custo_total:.2f}")
