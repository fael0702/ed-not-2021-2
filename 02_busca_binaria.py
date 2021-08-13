<<<<<<< HEAD
# ALGORITMO DE BUSCA BINÁRIA
#
# Dada uma lista, que deve estar PREVIAMENTE ORDENADA, e um valor de
# busca, divide a lista em duas metades e procura pelo valor de busca
# apenas na metade onde o valor poderia estar. Novas subdivisões são
# feitas até que se encontre o valor de busca ou que reste apenas uma
# sublista vazia, quando se conclui que o valor de busca não existe na
# lista.

from time import time
from data.lista_nomes import nomes

comps = 0   # Declarando uma variável global

def busca_binaria(lista, valor_busca):
    """
        Função que implementa o algoritmo de busca binária

        Retorna a posição onde valor_busca foi encontrado ou
        o valor convencional -1 se valor_busca não existir na lista
    """
    global comps # Indica que estamos usando a variável declarada na linha 13
    comps = 0

    ini = 0                 # Primeira posição
    fim = len(lista) - 1    # Última posição

    while ini <= fim:
        meio = (ini + fim) // 2     # Operador // é divisão inteira

        # 1º caso: lista[meio] é igual a valor_busca
        if lista[meio] == valor_busca:  # ENCONTROU!
            comps += 1
            return meio     # meio é a posição onde valor_busca está na lista

        # 2º caso: valor_busca é menor que lista[meio]
        elif valor_busca < lista[meio]:
            comps += 2
            fim = meio - 1  # Descarta a 2ª metade da lista

        # 3º caso: valor_busca é maior que lista[meio]
        else:
            comps += 2
            ini = meio + 1  # Descarta a 1ª metade da lista

    # 4º caso: valor_busca não encontrado na lista
    return -1


hora_ini = time()
print(f"Posição de FAUSTO: {busca_binaria(nomes, 'FAUSTO')} {comps} comparações")
hora_fim = time()
print(f"Tempo gasto procurando FAUSTO: {(hora_fim - hora_ini) * 1000}ms")

hora_ini = time()
print(f"Posição de ZULEICA: {busca_binaria(nomes, 'ZULEICA')} {comps} comparações")
hora_fim = time()
print(f"Tempo gasto procurando ZULEICA: {(hora_fim - hora_ini) * 1000}ms")

hora_ini = time()
print(f"Posição de NOEMIA: {busca_binaria(nomes, 'NOEMIA')} {comps} comparações")
hora_fim = time()
print(f"Tempo gasto procurando LUNISVALDO: {(hora_fim - hora_ini) * 1000}ms")
        
print(f"Nome exatamente no meio da lista: {nomes[len(nomes) // 2]}")

hora_ini = time()
print(f"Posição de JERDESON: {busca_binaria(nomes, 'JERDESON')} {comps} comparações")
hora_fim = time()
print(f"Tempo gasto procurando JERDESON: {(hora_fim - hora_ini) * 1000}ms")
=======
# ALGORITMO DE BUSCA BINÁRIA 
#
# Dada uma lista, que deve estar PREVIAMENTE ORDENADA, e um valor de 
# busca, divide a lista em duas metades e procura pelo valor de busca 
# apenas na metade onde o valor poderia estar. Novas subdivisões são
# feitas até que se encontre o valor debusca ou que reste apenas uma 
# sublista vazia, quando se conclui que o valor de busca não existe na
# lista.

from time import time 
from data.lista_nomes import nomes 

comps = 0

def busca_binaria(lista, valor_busca): 
      """
          Função que implementa o algoritmo de busca sequencial 

          Retorna a posição onde valor_busca foi encontrado ou 
          o valor convencional -1 se valor_busca não existir na lista
      """
      ini = 0                  # Primeira posição 
      fim = len(lista) - 1     # Última posição 

      while ini <= fim:
           meio = (ini + fim) // 2       # Operador // é divisão inteira

          # 1º caso: lista[meio] é igual a valor_busca
           if lista[meio] == valor_busca: # ENCONTROU! 
                return meio      # meio é a posição onde valor_busca está na lista
      
          # 2º caso: valor_busca é menor que lista[meio]
           elif valor_busca < lista[meio]:
                fim = meio - 1  # Descarta a 2º metade da lista

          # 3º caso: valor_busca é maior que lista[meio]
           else:
                ini = meio + 1 # Descarta a 1º metade da lista

      # 4º caso: valor_busca não encontrado na lista
      return -1

hora_ini = time()
print(f"Posição de FAUSTO: {busca_binaria(nomes, 'FAUSTO')}")
hora_fim = time()
print(f"Tempo gasto procurando FAUSTO: {hora_fim - hora_ini}s")

hora_ini = time()
print(f"Posição de ZULEICA: {busca_binaria(nomes, 'ZULEICA')}")
hora_fim = time()
print(f"Tempo gasto procurando ZULEICA: {hora_fim - hora_ini}s")

hora_ini = time()
print(f"Posição de  {busca_binaria(nomes, 'ORKUTILSON')}")
hora_fim = time()
print(f"Tempo gasto procurando ORKUTILSON: {hora_fim - hora_ini}s")
>>>>>>> 54ffed3d3754de2178b647191b2db34be2fb0953
