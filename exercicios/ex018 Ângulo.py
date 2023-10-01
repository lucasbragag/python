import math
an = float(input('Informe o ângulo para calcular:'))
ra = math.radians(an)
se = math.sin(ra)
co = math.cos(ra)
ta = math.tan(ra)
print('Ângulo de {}, o seno é {:.2f}, o cosseno é {:.2f} e a tangente {:.2f}'.format(an, se, co, ta))
