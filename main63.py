

def equação(s1, s2, s3):
    soma = s1 + s2
    subtração = soma - s2
    divisão = subtração * soma
    return soma, subtração, divisão

x = equação(5, 10, 5)
print(x)