import math
from numpy import double, sign, abs

N = 10

def Help():
    text = '''
        Library for solving equations by numerical methods

        Equations templates:
            1. a*x + b*cos(x) + c
            2. a*x^2 + b*x + c
            3. a*x * exp(b*x) + c

        Methods:
            1. Newton (tangent) method
            2. Dichotomy method
            3. Secant (chord) method

Common function parameters:
e: accuracy
template: number of equation template
args: list of equation parameters [a, b, c]
Newton( x,  e,  template, [] args)
x: init value
Dichotomy( a,  b,  e,  template, [] args)
a: left value of the erval in which the solution is located
b: right value of the erval in which the solution is located
Secant( x_2,  x_1,  e,  template, [] args)
x_1: previous value of x (Xn-1)
x_2: previous value of x_1 (Xn-2)
'''
    return text


def template_1( x, args):
    a = args[0]
    b = args[1]
    c = args[2]
    return (a * x + b * math.cos(x) + c)

def  template_1_derivate( x, args):
    a = args[0]
    b = args[1]
    return (a - b * math.sin(x))

def template_2( x, args):
    a = args[0]
    b = args[1]
    c = args[2]
    return (a * x * x + b * x + c)

def  template_2_derivate( x, args):
    a = args[0]
    b = args[1]
    return (2 * a * x + b)

def  template_3( x, args):
    a = args[0]
    b = args[1]
    c = args[2]
    return (a * x * math.exp(b * x) + c)

def  template_3_derivate( x, args):
    a = args[0]
    b = args[1]
    return (a * math.exp(b * x) + a * b * x * math.exp(b * x))


def ApplyTemplate( template, args):
    F = template_1   #default template
    text = ''
    if template == 1:
        text += f"{args[0]}x + {args[1]}cos(x) + {args[2]}\n"
    elif template == 2:
        F = template_2
        text += f"{args[0]}x^2 + {args[1]}x + {args[2]}\n"
    elif template == 3:
        F = template_3
        text += f"{args[0]}x * exp({args[1]}x) + {args[2]}\n"
    else:
        text += "Applied default template\n"
        text += f"{args[0]}x + {args[1]}cos(x) + {args[2]}\n"
    
    return F, text


def GetDerivate(template):
    F = template_1_derivate   #default template derivate

    if template == 1:
        pass
    elif template == 2:
        F = template_2_derivate
    elif template == 3:
        F = template_3_derivate
    
    return F


def Newton( x,  e,  template, args):
    text = ''
    text += "\tNewton (tangent) method\n"
    if (len(args) < 3):
        text += "Not enough arguments for template"
        return 0, 0, 0, text
    
    F, buf = ApplyTemplate(template, args)
    text += buf
    F_derivate = GetDerivate(template)

    f = F(x, args)
    f1 = F_derivate(x, args)
    i = 0
    text += f"{i}) \t x = {x:.{N}f}  \t f = {f:.{N}f} \n"
    while (abs(f) > e):
        x = x - (f / f1)

        f = F(x, args)
        f1 = F_derivate(x, args)
        i += 1
        text += f"{i}) \t x = {x:.{N}f}  \t f = {f:.{N}f} \n"
    
    text += f'Result:  x = {x:.{N}f}, F(x) = {f:.{N}f}\n\n'
    return i, x, f, text


def Dichotomy( a,  b,  e,  template, args):
    text = ''
    text += "\tDichotomy method\n"
    if (len(args) < 3):
        text += "Not enough arguments for template"
        return 0, 0, 0, text
    
    F, buf = ApplyTemplate(template, args)
    text += buf

    if (F(a, args) * F(b, args) > 0):
        text += "Bad erval\n"
        return 0, 0, 0, text
    

    x = (a + b) / 2
    f = F(x, args)
    i = 0
    text += f"{i}) \t a = {a:.{N}f} \t b = {b:.{N}f} \t x = {x:.{N}f} \t f = {f:.{N}f}\n"
    while (abs(f) > e):
        if (sign(F(a, args)) == sign(F(x, args))):
            a = x
        if (sign(F(b, args)) == sign(F(x, args))):
            b = x

        x = (a + b) / 2
        f = F(x, args)
        i += 1
        text += f"{i}) \t a = {a:.{N}f} \t b = {b:.{N}f} \t x = {x:.{N}f} \t f = {f:.{N}f}\n"
    
    text += f'Result:  x = {x:.{N}f}, F(x) = {f:.{N}f}\n\n'
    return i, x, f, text


def Secant( x_2,  x_1,  e,  template, args):
    text = ''
    text += "\tSecant (chord) method\n"
    if (len(args) < 3):
        text += "Not enough arguments for template"
        return 0, 0, 0, text
    
    F, buf = ApplyTemplate(template, args)
    text += buf

    x = x_1
    f = F(x, args)
    i = 0
    text += f"{i}) \t x-2 = {x_2:.{N}f} \t x-1 = {x_1:.{N}f} \t x = {x:.{N}f} \t f = {f:.{N}f}\n"
    while (abs(f) > e):
        x = x_1 - F(x_1, args) * ((x_1 - x_2) / (F(x_1, args) - F(x_2, args)))

        f = F(x, args)
        i += 1
        text += f"{i}) \t x-2 = {x_2:.{N}f} \t x-1 = {x_1:.{N}f} \t x = {x:.{N}f} \t f = {f:.{N}f}\n"
        x_2 = x_1
        x_1 = x
    
    text += f'Result:  x = {x:.{N}f}, F(x) = {f:.{N}f}\n\n'
    return i, x, f, text

def SolveFile(path):
    text = ''
    text += f'Processing input file {path}\n\n'
    try:
        with open(path) as sr:
            for line in sr:
                splited = line.strip().replace(',', '.').split()
                method = splited[0]
                args = list(map(double, splited[1:]))

                if method == 'Newton':
                    res = Newton(*args[:3], args[3:])
                elif method == 'Dichotomy':
                    res = Dichotomy(*args[:4], args[4:])
                elif method == 'Secant':
                    res = Secant(*args[:4], args[4:])
                
                text += res[-1]
    except Exception:
        text += 'An exception occured'
    
    return text

