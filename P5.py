import sympy as sym
from math import sin, pi, exp, sqrt


def trapezoidal_compuesta(funcion, a, b, N):
    h = (b - a)/(N + 1)
    sumatoria = sum(map(lambda y: sym.sympify(funcion).subs({"x": a + y*h}),
    range(1, N+1)))
    return h*((sym.sympify(funcion).subs({"x": a}) + sym.sympify(funcion).subs(
        {"x": a + (N+1)*h}) / 2) + sumatoria)


def error(integral_real_num, aprox):
    return abs(integral_real_num - aprox)


def integral_real(funcion, a, b):
    integral_real = sym.integrate(funcion, x)
    print(integral_real)
    integral_real_num = sym.sympify(integral_real).subs({"x": b}) - \
                        sym.sympify(
                            integral_real).subs({"x": a})
    return integral_real_num


x = sym.symbols("x")
funcion1 = (1/(2*pi))*sym.exp(sym.sin(x)/sqrt(2))
a1 = 0
b1 = pi/4
N = 1
aprox1 = trapezoidal_compuesta(funcion1, a1, b1, N)
error1 = 1

a2 = 0
b2 = 2*pi
aprox2 = trapezoidal_compuesta(funcion1, a2, b2, 1)
error2 = 2

while error1 > 0.0001:
    N += 1
    aux = trapezoidal_compuesta(funcion1, a1, b1, N)
    print(error1)
    error1 = error(aux, aprox1)
    aprox1 = aux
    print(N)

N = 1

while error2 > 0.0001:
    N += 1
    aux = trapezoidal_compuesta(funcion1, a2, b2, N)
    print(error2)
    error2 = error(aux, aprox2)
    aprox2 = aux
    print(N)