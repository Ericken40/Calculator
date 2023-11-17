var = ''
aux = ''
op = [ '+', '-', '÷', 'x']


def enter_key(n):
    global var
    var += n
    return var


def result():
    global var
    if 'x' in var:
        var = var.replace('x', '*')
    if '÷' in var:
        var = var.replace('÷', '/')
    var = str(eval(var))
    return var



def plus():
    global var
    global aux
    var = var + '+0'
    var = str(eval(var))
    if var[-1] == '+':
        var = var + '0'
        var = str(eval(var))
        return var
    else:
        return '+'
    

def minus():
    global var
    var = var + '-0'
    var = str(eval(var))
    if var[-1] == '-':
        var = var +'0'
        var = str(eval(var))
        return var
    else:
        return '-'
    
    
def times():
    global var
    global aux
    if var[-1] == 'x':
        aux = var.replace('x', '*') + '1'
        aux = str(eval(aux))
        clear(var)
        var = aux
        return var
    elif len(var) > 0 and var[-1] != 'x':
        var = var.replace('x', '*')
        var = str(eval(var))
        return 'x'
    var = var + '*1'
    var = str(eval(var))
    return 'x'    
    

def div():
    global var
    global aux
    if var[-1] == '÷':
        aux = var.replace('÷', '/') + '1'
        aux = str(eval(aux))
        clear(var)
        var = aux
        return var 
    elif len(var) > 0 and var[-1] != '÷':
        var = var.replace('÷', '/')
        var = str(eval(var))
        return '÷'
    var = var + '/1'
    var = str(eval(var))
    return '÷'
    
        

def clear():
    global var
    var = ''
    return var


def percent():
    global var
    global aux
    for i in op:
        if i in var:
            if i == 'x':
                var = var.replace(i, '*')
                var = var + '/100'
                return str(eval(var))
            elif i == '÷':
                aux = var.replace(i, '*')
                aux += '/100'
                aux = str(eval(aux))
                var = var[:var.index(i) + 1]
                var = var.replace(i, '/')
                var = var + aux
                return str(eval(var))
            else:
                aux = var.replace(i, '*')
                aux += '/100'
                aux = str(eval(aux))
                var = var[:var.index(i) + 1]
                var = var + aux
                return str(eval(var))
    if '+-x÷' not in var:
        var += '/100'
    return str(eval(var)) 
