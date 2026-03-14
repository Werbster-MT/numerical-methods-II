import numpy as np
import math

def derivada_numerica_taylor(f, x, h, filosofia, p, n):
    """
    Calcula a derivada numérica genérica de uma função.
    
    Parâmetros:
    f         : Função matemática (ex: np.sin)
    x         : Ponto onde a derivada será avaliada
    h         : Tamanho do passo
    filosofia : 'fw' (Forward), 'bw' (Backward), ou 'central'
    p         : Ordem da derivada (ex: 2 para derivada segunda)
    n         : Ordem do erro de truncamento (ex: 4 para erro O(h^4))
    """
    
    # 1. Determina a quantidade de pontos necessários para montar o sistema
    num_pontos = p + n - 1
    
    # 2. Define os índices dos pontos baseado na filosofia
    match filosofia:
        case 'central':
            # Para central, queremos um número ímpar de pontos para ter simetria.
            # Se for par, adicionamos 1.
            if num_pontos % 2 == 0:
                num_pontos += 1
            
            m = num_pontos // 2
            pontos = np.arange(-m, m + 1)
        
        case 'fw':
            # Pontos para frente: 0, 1, 2, ..., num_pontos - 1
            pontos = np.arange(0, num_pontos)
        
        case 'bw':
            # Pontos para trás: 0, -1, -2, ..., -(num_pontos - 1)
            pontos = np.arange(0, -num_pontos, -1)
        
        case _:
            raise ValueError("Filosofia inválida! Escolha 'fw', 'bw' ou 'central'.")

    # 3. Monta o sistema linear (Matriz de Vandermonde)
    A = np.zeros((num_pontos, num_pontos))
    B = np.zeros(num_pontos)
    
    for k in range(num_pontos):
        A[k, :] = pontos ** k
        
    # Na série de Taylor, a derivada 'p' que queremos isolar está dividida por p!
    B[p] = math.factorial(p)
    
    # 4. Resolve o sistema para encontrar os coeficientes (A, B, C, D, E...)
    coeficientes = np.linalg.solve(A, B)
    
    # 5. Aplica a combinação linear (Multiplica os coeficientes pela função nos pontos)
    soma = 0
    for i in range(num_pontos):
        soma += coeficientes[i] * f(x + pontos[i] * h)
        
    # 6. Divide tudo por h^p 
    derivada = soma / (h ** p)
    
    return derivada

def print_tabela_convergencia(f_x, x_alvo, delta, filosofia, p, n, tolerancia):
    # Calcular o valor de f(x) no ponto (que é constante para a coluna f(x))
    valor_fx = f_x(x_alvo)

    print("-" * 75)
    print(f"{'Δ(k)':<10} | {'f(x)':<15} | {'f\"(x)':<18} | {'e(x)':<15}")
    print("-" * 75)

    # Primeira iteração fora do ciclo 
    derivada_anterior = derivada_numerica_taylor(f_x, x_alvo, delta, filosofia, p, n)

    # Imprimir a primeira linha (o erro fica em branco ou usamos um traço)
    print(f"{delta:<10.5f} | {valor_fx:<15.5f} | {derivada_anterior:<18.8f} | {'-':<15}")

    erro_relativo = 1.0 # Iniciar com um erro grande para entrar no ciclo

    # Iniciar o estudo de convergência
    while erro_relativo >= tolerancia:
        # O passo é dividido por 2 a cada iteração (0.5 -> 0.25 -> 0.125 ...)
        delta = delta / 2 
        
        # Calcular a nova derivada com o novo delta
        derivada_atual = derivada_numerica_taylor(f_x, x_alvo, delta, filosofia, p, n)
        
        # Calcular o Erro Relativo Aproximado (fórmula da tabela)
        erro_relativo = abs((derivada_atual - derivada_anterior) / derivada_atual)
        
        # Imprimir a linha atual da tabela
        print(f"{delta:<10.5f} | {valor_fx:<15.5f} | {derivada_atual:<18.8f} | {erro_relativo:<15.8f}")
        
        # Atualizar a variável para a próxima iteração
        derivada_anterior = derivada_atual

    print("-" * 75)
    print(f"\nConvergência alcançada! O erro é: {erro_relativo:.8f} < 0.00001.")

# ==========================================
# TESTANDO O ALGORITMO
# ==========================================

f_x = lambda x: math.sqrt(math.e**(3*x) + 4*(x**2))
x_alvo = 2.0
tolerancia = 0.00001
delta = 0.5 
filosofia = 'central'
p = 2
n = 4

print_tabela_convergencia(f_x, x_alvo, delta, filosofia, p, n, tolerancia)
