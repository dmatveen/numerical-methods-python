from commons import MAX_ITER, MIN_STEP

class BaseError(Exception):
    '''Базовый класс для всех исключений пакета'''
    pass

class InvalidCounterError(BaseError):
    def __init__(self, counter, msg=f"Number if iterations more then {MAX_ITER}", error_code=-1):
        self.counter = counter
        self.msg = msg
        self.error_code = error_code
        super().__init__(self.msg)
    def __str__(self):
        return f"[Error Code {self.error_code}] {self.counter} -> {self.msg}"

class InvalidStepError(BaseError):
    def __init__(self, step, msg=f"dx seems to be less then {MIN_STEP}", error_code=-2):
        self.step = step
        self.msg = msg
        self.error_code = error_code
        super().__init__(self.msg)
    def __str__(self):
        return f"[Error Code {self.error_code}] {self.step} -> {self.msg}"

class InvalidSegmentBoundsError(BaseError):
    def __init__(self, x_left, x_right, msg=f"invalid segment boundaries. x_left need to be less then x_right", error_code=-3):
        self.x_left = x_left
        self.x_right = x_right
        self.msg = msg
        self.error_code = error_code
        super().__init__(self.msg)
    def __str__(self):
        return f"[Error Code {self.error_code}] {self.x_left} {self.x_right} -> {self.msg}"
      
class InvalidNumberOfPartitionsError(BaseError):
    def __init__(self, step, msg=f"number of partitions needs to be > 1", error_code=-4):
        self.number_of_partitions = step
        self.error_code = error_code
        super().__init__(self.msg)
    def __str__(self):
        return f"[Error Code {self.error_code}] {self.number_of_partitions} -> {self.msg}"

class InvalidIntegrationMethodError(BaseError):
    def __init__(self, msg=f"invalid integration method", error_code=-5):
        self.error_code = error_code
        super().__init__(self.msg)
    def __str__(self):
        return f"[Error Code {self.error_code}] -> {self.msg}"
    


# class InvalidDerivativeValue(Exception):
#     def __init__(self, df, msg=f"derivative value close to zero. so 1/df close to infinity", error_code=-4):
#         self.df = df
#         self.msg = msg
#         self.error_code = error_code
#         super().__init__(self.msg)
#     def __str__(self):
#         return f"[Error Code {self.error_code}] {self.df} -> {self.msg}"
    
# class InvalidMatrixSizesError(Exception):
#     def __init__(self, cols, rows, msg=f"number of cols of matrix 1 not equal to number of rows of matrix2", error_code=-5):
#         self.cols = cols
#         self.rows = rows
#         self.msg = msg
#         self.error_code = error_code
#         super().__init__(self.msg)
#     def __str__(self):
#         return f"[Error Code {self.error_code}] {self.cols} {self.rows} -> {self.msg}"
    
# class NonSquareMatrixError(Exception):
#     def __init__(self, cols, rows, msg=f"number of cols of matrix not equal to number of rows of the same matrix", error_code=-6):
#         self.cols = cols
#         self.rows = rows
#         self.msg = msg
#         self.error_code = error_code
#         super().__init__(self.msg)
#     def __str__(self):
#         return f"[Error Code {self.error_code}] {self.cols} {self.rows} -> {self.msg}"
    
# class InvalidMatrixDimensionsError(Exception):
#     def __init__(self, cols_a, rows_a, cols_b, rows_b, msg=f"dimensions of matrix1 and matrix2 must be the same", error_code=-7):
#         self.cols_a = cols_a
#         self.rows_a = rows_a
#         self.cols_b = cols_b
#         self.rows_b = rows_b
#         self.msg = msg
#         self.error_code = error_code
#         super().__init__(self.msg)
#     def __str__(self):
#         return f"[Error Code {self.error_code}] ({self.cols_a} {self.rows_a}) ({self.cols_b} {self.rows_b}) -> {self.msg}"
    
# class InvalidObservationsError(Exception):
#     def __init__(self, size_x, size_y, msg=f"sizes of observations of x and y must be the same", error_code=-8):
#         self.size_x = size_x
#         self.size_y = size_y
#         self.msg = msg
#         self.error_code = error_code
#         super().__init__(self.msg)
#     def __str__(self):
#         return f"[Error Code {self.error_code}] ({self.size_x} {self.size_y}) -> {self.msg}"

# class InvalidPolynomSizeError(Exception):
#     def __init__(self, size_poly, msg=f"size of polynom coefficients of array need to be >0", error_code=-9):
#         self.size_x = size_poly
#         self.msg = msg
#         self.error_code = error_code
#         super().__init__(self.msg)
#     def __str__(self):
#         return f"[Error Code {self.error_code}] ({self.size_poly}) -> {self.msg}"
    
# class UnknownError(Exception):
#     def __init__(self, msg=f"unknown error", error_code=-10):
#         self.msg = msg
#         self.error_code = error_code
#         super().__init__(self.msg)
#     def __str__(self):
#         return f"[Error Code {self.error_code}] {self.msg}"