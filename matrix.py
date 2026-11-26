class Matrix:


    def __init__(self, m: list[list] | list | int, n=None, EPS=1e-6):
        if n is None and type(m) is not list:
            raise TypeError(f"can't create a matrix from {type(m)}")
        if n is not None and type(n) is not int:
            raise TypeError(f"number of columns must be int, not {type(n)}") 
        if type(n) is int and type(m) is not int:
            raise TypeError(f"number of rows must be int, not {type(m)}")
        if m == []:
            raise ValueError(f"can't create a matrix from empty list")
        
        # zero-matrix from dimensions
        if n is not None:
            if n <= 0 or m <= 0:
                raise ValueError(f"dimensions of matrix must be positive, not ({m}, {n}) ") 
            self.data = [0] * (m * n)
            self.rows = m
            self.cols = n

        # matrix from list of lists
        elif type(m[0]) is list:
            self.data = []
            for row in m:
                for el in row:
                    self.data.append(el)
            self.rows = len(m)
            self.cols = len(m[0])
        
        # line-matrix
        else:
            self.data = []
            for el in m:
                self.data.append(el)
            self.rows = 1
            self.cols = len(m)
        
        self.EPS = EPS


    def __add__(self, other: Matrix) -> Matrix:
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError(f"matricies must have same dimentions, " + 
                             f"but have sizes {self.get_size()} and {other.get_size()}")

        out = Matrix(self.rows, self.cols)
        for i in range(self.rows*self.cols):
            out.data[i] = self.data[i] + other.data[i] 
        
        return out


    def __sub__(self, other) -> Matrix:
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError(f"matricies must have same dimentions, "
                             f"but have sizes {self.get_size()} and {other.get_size()}")

        out = Matrix(self.rows, self.cols)
        for i in range(self.rows*self.cols):
            out.data[i] = self.data[i] - other.data[i] 
        
        return out


    def __mul__(self, other: Matrix | int | float) -> Matrix:
        if not(type(other) is Matrix or type(other) is float or type(other) is int):
            raise TypeError(f"can only multiply matrix by matrix, "
                            f"int or float, not {type(other)}")

        if type(other) is Matrix:  
            if self.cols != other.rows:
                raise ValueError(f"multiplying matricies must have dimentions (a, x) (x, b), "
                                 f"not {self.get_size()} {other.get_size()}")

            out = Matrix(self.rows, other.cols)
            for i in range(self.rows):
                for j in range(other.cols):
                    for k in range(other.rows):
                        out.data[i * out.cols + j] += \
                            self.data[i * self.cols + k] * other.data[k * other.cols + j]

        if type(other) is not Matrix:
            out = Matrix(self.rows, self.cols)
            for i in range(self.rows*self.cols):
                out.data[i] = self.data[i] * other

        return out

    def __truediv__(self, other: int | float) -> Matrix:
        if not(type(other) is float or type(other) is int):
            raise TypeError("can only divide matrix by int or float, "
                            f"not {type(other)}")

        out = Matrix(self.rows, self.cols)
        for i in range(self.rows * self.cols):
            out.data[i] = self.data[i] / other

        return out


    def __eq__(self, other: Matrix) -> bool:
        if type(other) is not Matrix:
            return False
        
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError(f"can only compare matrices with the same size"+
                             f"not {self.get_size()}, {other.get_size()}")
        
        for i in range(self.rows*self.cols):
            if self.data[i] != other.data[i]:
                return False
            
        return True


    def transpose(self):
        out = Matrix(self.cols, self.rows)
        for i in range(self.rows):
            for j in range(self.cols):
                out.data[j * self.rows + i] = self.data[i * self.cols + j]

        return out



    def identity(self) -> Matrix:
        if self.rows != self.cols:
            raise ValueError(f"identity matrix can only be square" +
                             f"not {self.get_size()}")
        
        out = Matrix(self.rows, self.cols)
        for i in range(self.cols):
            out.data[i*self.cols + i] = 1

        return out


    def _lu_decomposition_for_det(self) -> tuple[Matrix, Matrix]:
        n = self.cols
        u = Matrix(n, n)
        u.data = self.data.copy()
        l = Matrix(n, n).identity()

        for i in range(n):
            # if diagonal element is 0 add other row to that row to make it non 0
            if abs(u.data[i*n + i]) < self.EPS:
                for k in range(i + 1, n):
                    if u.data[k*n + i]:
                        for j in range(n):
                            u.data[i*n + j] += u.data[k*n + j]
                        return (l, u)
                      
            for k in range(i + 1, n):
                # lower
                l.data[k*n + i] = u.data[k*n + i] / u.data[i*n + i]

                # upper
                for j in range(n):
                    u.data[k*n + j] -= l.data[k*n + i] * u.data[i*n + j]

        return (l, u)
    

    def invert(self) -> Matrix | None:
        if self.rows != self.cols:
            raise ValueError(f"can only invert square matrix"+
                             f"not {self.get_size()}")

        if abs(self.determinant()) < self.EPS:
            return None

        n = self.rows
        inp = Matrix(n, n)
        inp.data = self.data.copy()
        out = Matrix(n, n).identity()

        for i in range(n):
            # if diagonal element is 0 add other row to that row to make it non 0
            if abs(inp.data[i*n + i]) < self.EPS:
                for k in range(i + 1, n):
                    if inp.data[k*n + i]:
                        for j in range(n):
                            inp.data[i*n + j], inp.data[k*n + j] = inp.data[k*n + j], inp.data[i*n + j]
                            out.data[i*n + j], out.data[k*n + j] = out.data[k*n + j], out.data[i*n + j]
                        return None

            # normalise the diagonal element
            pivot = inp.data[i*n + i]
            for j in range(n):
                inp.data[i*n + j] /= pivot
                out.data[i*n + j] /= pivot

            # reduce all elements in a column to zero
            for k in range(n):
                if k == i:
                    continue
                tmp = inp.data[k*n + i]
                for j in range(n):
                    inp.data[k*n + j] -=  inp.data[i*n + j] * tmp
                    out.data[k*n + j] -=  out.data[i*n + j] * tmp

        return out


    def determinant(self):
        if self.cols != self.rows:
            raise ValueError(f"can only find determinant of a square matrix, " 
                             f"not {self.get_size()}")
        
        n = self.cols
        l, u = self._lu_decomposition_for_det()

        det = 1
        for i in range(n):
            det *= u.data[i * n + i]

        return det


    def set(self, i, j, value):
        self.data[i * self.cols + j] = value


    def get(self, i, j):
        return self.data[i * self.cols + j]


    def get_size(self):
        return (self.rows, self.cols)


    def get_m(self):
        return self.rows


    def get_n(self):
        return self.cols


    def __str__(self):
        out = ""
        for i in range(self.rows):
            for j in range(self.cols):
                out += '{:6}'.format(self.data[i * self.cols + j])
            if i != self.rows - 1:
                out += "\n"
        return out
