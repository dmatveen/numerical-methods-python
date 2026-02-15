'''numerical methods package - библиотека численных методов на python
с использованием стандартной библиотеки и минимальным подключением сторонних библиотек:
numpy - только для массивов.'''

from ..utils.errors import (
    BaseError,
    InvalidCounterError, 
    InvalidStepError, 
    InvalidSegmentBoundsError, 
    InvalidNumberOfPartitionsError, 
    InvalidIntegrationMethodError
)

from integrals import integration

__version__ = '0.1.0'
__all__ = [
    # Исключения
    'BaseError',
    'InvalidSegmentBoundsError',
    'InvalidStepError',
    'InvalidCounterError',
    'InvalidNumberOfPartitionsError',
    'InvalidIntegrationMethodError',
    
    # Методы интегрирования
    'rectangle_left_sum',
    'rectangle_right_sum',
    'rectangle_mid_sum',
    'trap_sum',
    'parabolic_sum',
    'integrate_adaptive'
]