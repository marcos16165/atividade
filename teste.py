def questao1():
    return 5**2, 9*5, 15/12, 12/15, 15//12, 12//15, 5%2, 9%5, 15%12, 12%15, 6%6, 0%7
    
def questao2():
    return('5 horas')

def questao3(h, e):
    resto=(h+e)%24
    return resto

def questao4(a,b):
    from datetime import date
    a = date.today()
    futuro = date.fromordinal(a.toordinal()+b)
    dias = ('segunda-feira','terça-feira','quarta-feira','quinta-feira','sexta-feira','sábado','domingo')

    return dias[futuro.weekday()]
    
def questao5():
    p1 = str('só')
    p2 = str('trabalho')
    p3 = str('sem')
    p4 = str('diversão')
    p5 = str('faz')
    p6 = str('de')
    p7 = str('João')
    p8 = str('em')
    p9 = str('chato')
    return('{} {} {} {} {} {} {} {} {}'.format(p1, p2, p3, p4, p5, p6, p7, p8, p9))
    
def questao6():
    return(6 * (1 - 2) )

def questao7(t):
    p = 10000
    r = 0.08
    n = 12
    a = p* (1 + (r/n))**(n*t)
    return a 

def questao8(raio):
    pi = 2 * 3.1415 * raio
    return pi

def questao9(al, la):
    x = al* la
    return x
    
def questao10(km,l):
    return (km/l)

def questao11(ce):
    return ((ce * 9) / 5) + 32

def questao12(fa):
    return ((fa - 32) * 5) / 9
    
