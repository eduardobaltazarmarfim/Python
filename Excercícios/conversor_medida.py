'''
Converter medidas conforme o valor passado pelo usuário
'''

def retorno():

    resp=input('Deseja executar o programa novamente?[s/n]: ')

    if(resp=='s' or resp=='S'):

        print('#'*30)

        verificar()

    else:

        print('Processo finalizado com sucesso!')

    pass

def verificar():
    
    try:

        val=int(input('Digite um valor inteiro: '))

        calcular(val)

        retorno()

    except:

        print('Erro - Dados inseridos são invalidos!')

        retorno()

    pass

def calcular(x):

    c=x*100
    m=x*1000

    print('O valor em metro {} convertido em centímetro {} cm.'.format(x,c))

    print('O valor em metro {} convertido em milímitro {} mm.'.format(x,m))
    
    pass

verificar()