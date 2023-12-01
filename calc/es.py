# função que lê dois números
def leitora_num() -> list:
    """Esta função cria uma lista e com dois números digitados e a grava"""
    i = 0
    numeros = []
    while i < 2:
        numeros.append(float(input(f"Digite o número {i+1} que deseja operar")))
        i+= 1
    return numeros

def leitora_operacao() -> str:
    """Esta função grava a operação digitada"""
    operacao = input("""Digite a operação que deseja realizar.
    Pressione: 
    + para adição; 
    - para subtração;
    * para multiplicação; 
    / para divisão""")
    return operacao

def leitora() -> list:
    """Esta função lê as funções leitora_num e leitora_operacao"""
    lista_numeros = leitora_num()
    operacao = leitora_operacao()
    return [lista_numeros, operacao]

def escritora(resultado):
    """Esta função coloca o resultado na tela"""
    print(f"O resultado da operação é igual a {resultado}")