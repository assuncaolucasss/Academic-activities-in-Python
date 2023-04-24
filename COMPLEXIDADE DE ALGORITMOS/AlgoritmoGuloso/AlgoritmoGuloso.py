 B def algoritmo_guloso(despesas, membros):
    despesas.sort(reverse=True)
    resultado = [0] * membros
    for i in range(len(despesas)):
        resultado[i % membros] += despesas[i]
    return resultado


def algoritmo_programacao_dinamica(despesas, membros):
    n = len(despesas)
    s = sum(despesas)
    if s % membros != 0:
        return None
    c = s // membros
    dp = [[False] * (c + 1) for _ in range(n + 1)]
    dp[0][0] = True
    for i in range(1, n + 1):
        for j in range(c + 1):
            dp[i][j] = dp[i - 1][j]
            if j >= despesas[i - 1]:
                dp[i][j] |= dp[i - 1][j - despesas[i - 1]]
    if not dp[n][c]:
        return None
    resultado = [0] * membros
    i, j = n, c
    while i > 0 and j >= 0:
        if j >= despesas[i - 1] and dp[i - 1][j - despesas[i - 1]]:
            resultado[i % membros] += despesas[i - 1]
            j -= despesas[i - 1]
        i -= 1
    return resultado


def main():
    despesas = list(map(int, input("Digite as despesas separadas por espaço: ").split()))
    membros = int(input("Digite o número de membros: "))
    resultado_guloso = algoritmo_guloso(despesas, membros)
    resultado_programacao_dinamica = algoritmo_programacao_dinamica(despesas, membros)
    print("Resultado com algoritmo guloso: ", resultado_guloso)
    print("Resultado com programação dinâmica: ", resultado_programacao_dinamica)


if __name__ == '__main__':
    main()

"""
Primeiramente, temos duas funções que implementam os algoritmos de
 divisão justa de despesas.
A primeira função, algoritmo_guloso, segue a abordagem gulosa para
 resolver o problema. Essa abordagem funciona da seguinte maneira:
  as despesas são ordenadas em ordem decrescente e então cada membro
   da divisão é alocado a cada uma das despesas, começando pelo valor
    mais alto. Essa estratégia é chamada de "pegar o que é maior
     primeiro". Essa função recebe duas entradas: a lista de despesas
      e o número de membros, e retorna uma lista com a soma de despesas
       de cada membro.

A segunda função, algoritmo_programacao_dinamica, segue a abordagem
 de programação dinâmica para resolver o problema. Essa abordagem 
 funciona da seguinte maneira: cria-se uma matriz dp de dimensões
  (n+1) x (s//membros+1), onde n é o número de despesas e s é
   a soma de todas as despesas. A ideia é preencher essa matriz
    de forma a identificar se é possível dividir as despesas
     entre os membros. Para cada posição (i,j) na matriz dp,
      representando a i-ésima despesa e uma soma de j, o valor
       de dp[i][j] é True se for possível obter a soma j com as
        primeiras i despesas. A partir dessa matriz, é possível
         determinar se é possível dividir as despesas entre os 
         membros. Se a resposta for sim, a função retorna uma
          lista com a soma de despesas de cada membro.

No programa principal, o usuário é solicitado a entrar com as
 despesas e o número de membros. Em seguida, as funções
  algoritmo_guloso e algoritmo_programacao_dinamica são 
  chamadas para calcular o resultado da divisão justa de 
  despesas usando ambas as abordagens. Por fim, os resultados
   são impressos na tela.
"""