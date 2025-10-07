'''Crie pelo menos dez testes. Tenha no mínimo cinco testes avaliados como
True e outros cinco avaliados como False'''

amo = ['pizza', 'internet', 'celular', 'doces', 'salgados','dormir']
coisas_que_gosto= amo
print(coisas_que_gosto == amo)
print( amo in coisas_que_gosto)

print('celular' in amo, 'dormir' in amo )
print('pizza' in amo)

odeio = ['humanos', 'modo claro', "tarefas domesticas",'barulho', 'trabalhar']
print('humanos' not in  odeio)
print('feliz' in odeio)