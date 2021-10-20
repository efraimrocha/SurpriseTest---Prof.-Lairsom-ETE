def adicionar_elemento(lista: list, elemento: str) -> bool:
    '''
    Verifica se o elemento começa com letra maiúscula
    Se ele passar na verificação, inserir na lista e retornar
    verdadeiro, caso contrário, retorne falso
    '''
    letra1 = elemento[0]
    if (letra1 == letra1.upper()):
        lista.append(elemento)
        return True
    else:
        return False
    
    
def buscar_elemento(lista: list, elemento: str) -> bool:

    if elemento in lista:
        return True
    else:
        return False
        

def remover_elemento(lista: list, elemento: str) -> bool:
    '''
    Verifica se a lista contém um elemento específico.
    Se ele estiver contido na lista, remover o elemento e
    retornar verdadeiro, caso contrário, retornar falso.
    '''
    nome = buscar_elemento(lista,elemento)
    if nome == True:
        lista.remove(elemento)
        return True
    else:
        return False
        



def limpar_lista(lista: list) -> None:
    '''
    Remove todos os elementos da lista.
    Função sem retorno.
    '''
    lista.clear()



def ordenar_lista(lista: list) -> None:
    '''
    Ordena todos os elementos da lista por ordem
    alfabética. A função não possui retorno
    '''
    lista.sort()


def pegar_quantidade(lista: list) -> int:
    '''
    Retorna a quantidade de elementos dentro
    da lista
    '''
    q = len(lista)
    return q


def converter_maiusculo(lista: list) -> list:
    '''
    Converte todos os elementos da lista para letra
    maiúscula e os retorna em uma nova lista
    '''
    lista2 = [i.upper() for i in lista]
    lista = lista2
    return lista



def eliminar_repetidos(lista: list) -> list:
    '''
    DESAFIO: 0.5 extra
    Remove todos os elementos repetidos na lista
    e retorna uma lista nova (não vale utilizar o set)
    '''
    nova_lista = []
    for i in lista:
        if i not in nova_lista:
            nova_lista.append(i)
    nova_lista.sort()
    return nova_lista
    
