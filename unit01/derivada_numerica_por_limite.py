import math

def calcular_derivada(f, x, h, ordem_derivada, ordem_erro, filosofia):
    """
    Calcula a derivada numérica de uma função usando diferenças finitas.
    
    Parâmetros:
    f              : Função a ser derivada (callable)
    x              : Ponto onde a derivada será avaliada (float)
    h              : Tamanho do passo (float)
    ordem_derivada : 1 (Primeira derivada) ou 2 (Segunda derivada)
    ordem_erro     : 1 (O(h)), 2 (O(h²)) ou 4 (O(h⁴))
    filosofia : 'progressiva', 'regressiva' ou 'central'
    
    Retorna:
    float: O valor numérico da derivada.
    """
    
    match ordem_derivada:
        case 1:
            # ==========================================
            # PRIMEIRA DERIVADA
            # ==========================================
            match filosofia:
                case 'progressiva':
                    match ordem_erro:
                        case 1:
                            return (f(x + h) - f(x)) / h
                        case 2:
                            return (-f(x + 2*h) + 4*f(x + h) - 3*f(x)) / (2*h)

                case 'regressiva':
                    match ordem_erro:
                        case 1:
                            return (f(x) - f(x - h)) / h
                        case 2:
                            return (3*f(x) - 4*f(x - h) + f(x - 2*h)) / (2*h)

                case 'central':
                    match ordem_erro:
                        case 2:
                            return (f(x + h) - f(x - h)) / (2*h)
                        case 4:
                            return (-f(x + 2*h) + 8*f(x + h) - 8*f(x - h) + f(x - 2*h)) / (12*h)

        case 2:
            # ==========================================
            # SEGUNDA DERIVADA
            # ==========================================
            match filosofia:
                case 'progressiva':
                    match ordem_erro:
                        case 1:
                            return (f(x + 2*h) - 2*f(x + h) + f(x)) / (h**2)
                        case 2:
                            return (-f(x + 3*h) + 4*f(x + 2*h) - 5*f(x + h) + 2*f(x)) / (h**2)

                case 'regressiva':
                    match ordem_erro:
                        case 1:
                            return (f(x) - 2*f(x - h) + f(x - 2*h)) / (h**2)
                        case 2:
                            return (2*f(x) - 5*f(x - h) + 4*f(x - 2*h) - f(x - 3*h)) / (h**2)

                case 'central':
                    match ordem_erro:
                        case 2:
                            return (f(x + h) - 2*f(x) + f(x - h)) / (h**2)
                        case 4:
                            return (-f(x + 2*h) + 16*f(x + h) - 30*f(x) + 16*f(x - h) - f(x - 2*h)) / (12 * h**2)

        case 3:
            # ==========================================
            # TERCEIRA DERIVADA
            # ==========================================
            match filosofia:
                case 'progressiva':
                    match ordem_erro:
                        case 1:
                            return (f(x + 3*h) - 3*f(x + 2*h) + 3*f(x + h) - f(x)) / (h**3)
                        case 2:
                            return (-f(x + 4*h) + 5*f(x + 3*h) - 10*f(x + 2*h) + 10*f(x + h) - 4*f(x)) / (h**3)

                case 'regressiva':
                    match ordem_erro:
                        case 1:
                            return (f(x) - 3*f(x - h) + 3*f(x - 2*h) - f(x - 3*h)) / (h**3)
                        case 2:
                            return (4*f(x) - 10*f(x - h) + 10*f(x - 2*h) - 5*f(x - 3*h) + f(x - 4*h)) / (h**3)

                case 'central':
                    match ordem_erro:
                        case 2:
                            return (f(x + 2*h) - 2*f(x + h) + 2*f(x - h) - f(x - 2*h)) / (2*h**3)
                        case 4:
                            return (-f(x + 3*h) + 8*f(x + 2*h) - 13*f(x + h) + 13*f(x - h) - 8*f(x - 2*h) + f(x - 3*h)) / (12 * h**3)

    # Caso a combinação não esteja mapeada
    raise ValueError(f"Combinação não suportada: Derivada {ordem_derivada}ª, Erro O(h^{ordem_erro}), Tipo {filosofia}")

# ==========================================
# EXEMPLO DE USO
# ==========================================

# 1. f(x) = sin(x)
f_x = lambda x: math.sin(x)

# 2. Parâmetros de entrada
x_val = math.pi / 4  # Ponto x
h_val = 0.01         # Tamanho do passo (h)

# 3. Testando as diferenças centrais para f'(x) com erro O(h²)
resultado_central = calcular_derivada(f_x, x=x_val, h=h_val, ordem_derivada=1, ordem_erro=2, filosofia='central')

# A derivada analítica de sin(x) é cos(x). Em x = pi/4, o valor exato é ~0.707106
valor_exato = math.cos(x_val)

print(f"Valor Exato (Analítico): {valor_exato:.6f}")
print(f"Diferença Central O(h²): {resultado_central:.6f}")
print(f"Erro Real: {abs(valor_exato - resultado_central):.8e}")