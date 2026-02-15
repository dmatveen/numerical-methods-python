from ..utils.commons import EPS,MAX_ITER,MIN_STEP
from ..utils.commons import IntegrationType, Callable, Optional
from ..utils.errors import InvalidCounterError, InvalidStepError, InvalidSegmentBoundsError, InvalidNumberOfPartitionsError, InvalidIntegrationMethodError

def rectangle_left_sum(
    f:Callable[[float],float],
    x_left:float,
    x_right:float,
    n:int=10
    )->float:
    '''
    Вычисляет интегральную сумму методом левых прямоугольников для функции f 
    на промежутке [x_left,x_right], разбитом на n частей
    
    :param f: интегрируемая на отрезке [x_left,x_right] функция f(x)
    :type f: Callable[[float], float]
    :param x_left: левая граница отрезка интегрирования
    :type x_left: float
    :param x_right: правая граница отрезка интегрирования
    :type x_right: float
    :param n: число отрезков, на которые разбивается отрезок [x_left,x_right] 
    :type n: int
    :return: Значение интегральной суммы или None
    :rtype: float
    '''
    dx=(x_right-x_left)/n
    if dx<MIN_STEP:
        raise InvalidStepError
    x=x_left
    result=f(x)*dx
    for i in range(1,n):
        x=x_left+i*dx
        result=result+f(x)*dx
    return result

def rectangle_right_sum(
    f:Callable[[float],float],
    x_left:float,
    x_right:float,
    n:int=10
    )->float:
    '''
    Вычисляет интегральную сумму методом правых прямоугольников для функции f 
    на промежутке [x_left,x_right], разбитом на n частей
    
    Аргументы:
    :param f: интегрируемая на отрезке [x_left,x_right] функция f(x)
    :type f: Callable[[float], float]
    :param x_left: левая граница отрезка интегрирования
    :type x_left: float
    :param x_right: правая граница отрезка интегрирования
    :type x_right: float
    :param n: число отрезков, на которые разбивается отрезок [x_left,x_right] 
    при интегрировании
    :type n: int
    :return: Значение интегральной суммы или None
    :rtype: float
    '''
    dx=(x_right-x_left)/n
    if dx<MIN_STEP:
        raise InvalidStepError
    x=x_left+dx
    result=f(x)*dx
    for i in range(1,n):
        x=x_left+i*dx
        result=result+f(x)*dx
    return result

def rectangle_mid_sum(
    f:Callable[[float],float],
    x_left:float,
    x_right:float,
    n:int=10
    )->float:
    '''
    Вычисляет интегральную сумму методом средних прямоугольников для функции f 
    на промежутке [x_left,x_right], разбитом на n частей
    
    :param f: интегрируемая на отрезке [x_left,x_right] функция f(x)
    :type f: Callable[[float], float]
    :param x_left: левая граница отрезка интегрирования
    :type x_left: float
    :param x_right: правая граница отрезка интегрирования
    :type x_right: float
    :param n: число отрезков, на которые разбивается отрезок [x_left,x_right] 
    :type n: int
    :return: Значение интегральной суммы или None
    :rtype: float | None
    '''
    dx=(x_right-x_left)/n
    if dx<MIN_STEP:
        raise InvalidStepError
    x=x_left+dx/2
    result=f(x)*dx
    for i in range(1,n):
        x=x_left+i*dx
        result=result+f(x)*dx
    return result

def trap_sum(
    f:Callable[[float],float],
    x_left:float,
    x_right:float,
    n:int=10
    )->float:
    '''
    Вычисляет интегральную сумму методом трапеций для функции f 
    на промежутке [x_left,x_right], разбитом на n частей
    
    :param f: интегрируемая на отрезке [x_left,x_right] функция f(x)
    :type f: Callable[[float], float]
    :param x_left: левая граница отрезка интегрирования
    :type x_left: float
    :param x_right: правая граница отрезка интегрирования
    :type x_right: float
    :param n: число отрезков, на которые разбивается отрезок [x_left,x_right] 
    :type n: int
    :return: Значение интегральной суммы или None
    :rtype: float | None
    '''
    dx=(x_right-x_left)/n
    if dx<MIN_STEP:
        raise InvalidStepError
    x0=x_left
    f0=f(x0)
    result=0
    for i in range(1,n):
        x1=x_left+i*dx
        f1=f(x1)
        result=result+(f0+f1)*dx/2
        x0=x1
        f0=f1
    return result

def parabolic_sum(
    f:Callable[[float],float],
    x_left:float,
    x_right:float,
    n:int=10
    )->float:
    '''
    Вычисляет интегральную сумму методом парабол для функции f 
    на промежутке [x_left,x_right], разбитом на n частей
    
    :param f: интегрируемая на отрезке [x_left,x_right] функция f(x)
    :type f: Callable[[float], float]
    :param x_left: левая граница отрезка интегрирования
    :type x_left: float
    :param x_right: правая граница отрезка интегрирования
    :type x_right: float
    :param n: число отрезков, на которые разбивается отрезок [x_left,x_right] 
    :type n: int
    :return: Значение интегральной суммы или None
    :rtype: float
    '''
    dx=(x_right-x_left)/n
    if dx<MIN_STEP:
        raise InvalidStepError
    x0=x_left
    f0=f(x0)
    result=0
    for i in range(1,n):
        x1=x_left+i*dx
        f1=f(x1)
        x_mid=(x0+x1)/2
        f_mid=f(x_mid)
        result=result+(f0+4*f_mid+f1)*dx/6
        x0=x1
        f0=f1
    return result

def func_type_choise(type_of_integration:IntegrationType):
    '''
    Выбирает функцию интегрирования в зависимости от аргумента (типа интегрирования)
    
    :param type_of_integration: перечислительная переменная, предятавляющая собой
    тип интегрирования
    :type type_of_integration: IntegrationType
    '''
    if type_of_integration==IntegrationType.rectangle_left:
        return rectangle_left_sum
    elif type_of_integration==IntegrationType.rectangle_mid:
        return rectangle_mid_sum
    elif type_of_integration==IntegrationType.rectangle_right:
        return rectangle_right_sum
    elif type_of_integration==IntegrationType.trapezoid:
        return trap_sum
    elif type_of_integration==IntegrationType.parabolic:
        return parabolic_sum
    else:
        return None

def integration(
    f:Callable[[float],float],
    x_left:float,
    x_right:float,
    type_of_integration:IntegrationType,
    n:int=10,
    max_iter:int=MAX_ITER,
    eps:float=EPS
    )->Optional[float]:
    '''
    Вычисляет приближенное значение интеграла с точностью до eps методом 
    прямоугольников, трапеций, парабол на отрезке [x_left,x_right] в 
    зависимости от значения переменной type_of_integration типа IntegrationType.
        
    :param f: интегрируемая на отрезке [x_left,x_right] функция f(x)
    :type f: Callable[[float], float]
    :param x_left: левая граница отрезка интегрирования
    :type x_left: float
    :param x_right: правая граница отрезка интегрирования
    :type x_right: float
    :param type_of_integration: Тип интегрирования (перечислительный тип)
    :type type_of_integration: IntegrationType
    :param n: первичное число частей разбиения отрезка [x_min,x_max]
    :type n: int
    :param max_iter: максимальное число итераций. Вычисления прервутся после 
    его превышения.
    :type max_iter: int
    :param eps: Точность вычислений. Если отличия интегральных сумм на двух соседних 
    итерациях меньше eps, то вычисления прервутся.
    :type eps: float
    :return: Приближенное значение определенного интеграла на отрезке 
    [x_min,x_max] от функции f(x)
    :rtype: float | None
    '''
    if x_right <= x_left:
        raise InvalidSegmentBoundsError
    if n <= 0:
        raise InvalidNumberOfPartitionsError
    integration_method_function=func_type_choise(type_of_integration)
    if integration_method_function is None:
        raise InvalidIntegrationMethodError
    integral_sum_present=integration_method_function(f,x_left,x_right,n)
    integral_sum_next=None
    counter=0
    while True:
        counter=counter+1
        if counter > max_iter:
            raise InvalidCounterError
        #
        #Здесь надо трай валуеэррор
        #
        n=n*2
        integral_sum_next=integration_method_function(f,x_left,x_right,n)
        if abs(integral_sum_next-integral_sum_present)<eps:
            return integral_sum_next
        integral_sum_present=integral_sum_next
