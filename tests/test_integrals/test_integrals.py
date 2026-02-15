from pathlib import Path
import sys
import json
import numpy as np
import math

path_root=Path(__file__).parents[2]
print(path_root)
sys.path.append(str(path_root))

from integrals import integration
from commons import IntegrationType
from commons import EPS
from errors import InvalidMatrixSizesError


list_of_tests=None

def almost_equal(a,b,eps):
    result=False
    if abs(a-b)<eps:
        result=True
    return result

def integrals_test():
    with open('./numerical_methods/tests/test_integrals/data/integrals.json','r') as file:
        list_of_tests=json.load(file)
    
    # def f(x):
        #     return eval(func_str,{"x":x,"math":math,"np":np})
        
    def create_function_fast(func_str):
        '''Создает функцию через eval lambda выражения'''
        lambda_str=f'lambda x: {func_str}'
        return eval(lambda_str,{"math":math,"np":np})

    for method in IntegrationType:
        print(f'=====testing for {method.name} method:=====\n')
        for test in list_of_tests:
            des=None
            func_str=test["f"]
            x_left=float(test["x_left"])
            x_right=float(test["x_right"])
            solution=float(test["solution"])
            f=create_function_fast(func_str)
            des=integration(f,x_left,x_right,method)
            print(des)
            if almost_equal(des,solution,EPS):
                print('OK!\n')
            else:
                print('ERR!\n')

def main():
    integrals_test()

if __name__=="__main__":
    main()

