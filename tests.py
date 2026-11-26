from matrix import Matrix
from unittest import TestCase, main


class SimpleTests(TestCase):

    def test_initialization_by_dimensions(self):

        dims = [(1, 2), (2, 1), (5, 3), (2, 3), (10, 9)]

        for (m, n) in dims:
            mat = Matrix(m, n)

            self.assertEqual(mat.get_m(), m)
            self.assertEqual(mat.get_n(), n)
            self.assertEqual(mat.get_size(), (m, n))

            for i in range(m):
                for j in range(n):
                    self.assertEqual(mat.get(i, j), 0)
    def test_initialization_by_list(self):

        mats = [[ [24, -22, 27, 6],
                [-17, -22, -24, 0],
                [4, 7, 6, -7],
                [4, -13, -4, -17] ],

                [ [-26, -24],
                [25, 26] ],

                [ [-10, -29, -26],
                [-14, -18, -30],
                [6, 4, -25],
                [-10, -16, -16],
                [2, -30, -2] ],

                [ [24],
                [-27],
                [-4] ],

                [ [10, -26, -1, -23],
                [-15, -13, 5, 27],
                [-10, 16, 5, 13],
                [25, -3, -21, 5],
                [9, 10, -1, 27] ],

                [ [-15, 12, -28, 3],
                [21, 22, -14, -15],
                [0, 0, -9, 2] ],

                [ [16],
                [-28],
                [8],
                [26] ],

                [ [14, -11, 15, 16],
                [17, -18, 0, -1],
                [24, -11, 18, 22] ],

                [ [-5] ],

                [ [22, 28, 16, 6],
                [-4, 6, -28, -11],
                [20, -25, -3, 28],
                [9, 18, 2, -2] ]]


        for data in mats:
            mat = Matrix(data)

            self.assertEqual(mat.get_m(), len(data))
            self.assertEqual(mat.get_n(), len(data[0]))
            self.assertEqual(mat.get_size(), (len(data), len(data[0])))

            for i in range(mat.get_m()):
                for j in range(mat.get_n()):
                    self.assertEqual(mat.get(i, j), data[i][j])

        
    def test_initialization_with_invalid_arguments(self):

        with self.assertRaises(ValueError):
            Matrix(1, 0)

        with self.assertRaises(ValueError):
            Matrix(0, 1)
        
        with self.assertRaises(ValueError):
            Matrix(0, 0)

        with self.assertRaises(ValueError):
            Matrix([])

        with self.assertRaises(TypeError):
            Matrix([ [1] ], 1)

        with self.assertRaises(TypeError):
            Matrix("123")

        with self.assertRaises(TypeError):
            Matrix(1, [])

        with self.assertRaises(TypeError):
            Matrix(1.0, 1)

        with self.assertRaises(ValueError):
            Matrix(1, -1)

        with self.assertRaises(ValueError):
            Matrix(-1, 1)
        
        with self.assertRaises(TypeError):
            Matrix(1, 1.0)
        
        with self.assertRaises(TypeError):
            Matrix([], "s")


    def test_addition(self):
        tpls = [(
                [ [14, -30, -4],
                [26, -20, 25],
                [22, -2, -18] ],

                [ [-16, 20, 24],
                [-2, 18, 6],
                [-4, 8, 4] ],

                [ [-2, -10, 20],
                [24, -2, 31],
                [18, 6, -14] ],
                ),

                (
                [ [-16, -1, 13],
                [-14, -29, -16],
                [22, -7, -21],
                [17, 8, -29] ],

                [ [-26, -12, 17],
                [13, -8, -15],
                [2, -11, 28],
                [-21, -22, -5] ],

                [ [-42, -13, 30],
                [-1, -37, -31],
                [24, -18, 7],
                [-4, -14, -34] ],
                ),

                (
                [ [-26],
                [22],
                [-4] ],

                [ [14],
                [-16],
                [9] ],

                [ [-12],
                [6],
                [5] ],
                ),

                (
                [ [22],
                [9],
                [12] ],

                [ [-10],
                [-23],
                [7] ],

                [ [12],
                [-14],
                [19] ],
                ),
                ]

        for tpl in tpls:
            mat1 = Matrix(tpl[0])
            mat2 = Matrix(tpl[1])
            matsum = mat1 + mat2

            for i in range(mat1.get_m()):
                for j in range(mat2.get_n()):
                    self.assertEqual(matsum.get(i, j), tpl[2][i][j])


    def test_addition_with_invalid_arguments(self):

        with self.assertRaises(ValueError):
            mat1 = Matrix(1, 3)
            mat2 = Matrix(3, 3)
            mat1 + mat2

        with self.assertRaises(TypeError):
            mat1 = Matrix(1, 3)
            mat1 + 0

        with self.assertRaises(TypeError):
            mat1 = Matrix(1, 3)
            mat1 + []

        with self.assertRaises(TypeError):
            mat1 = Matrix(1, 3)
            mat1 + "mat2"

        with self.assertRaises(TypeError):
            mat1 = Matrix(1, 3)
            mat1 + 1.0

        with self.assertRaises(TypeError):
            mat1 = Matrix(1, 3)
            mat1 + 33678


    def test_substruction(self):

        tpls = [(
                [ [-4, -23, -10],
                [0, 21, -22],
                [-29, -23, -7] ],

                [ [14, -6, -15],
                [19, 27, -30],
                [-7, -26, 19] ],

                [ [-18, -17, 5],
                [-19, -6, 8],
                [-22, 3, -26] ],
                ),

                (
                [ [-25, 22, 1],
                [-1, 28, 9],
                [-24, -16, -9] ],

                [ [-12, -12, 25],
                [16, 18, 14],
                [2, -5, 15] ],

                [ [-13, 34, -24],
                [-17, 10, -5],
                [-26, -11, -24] ],
                ),

                (
                [ [2, 20],
                [-7, -4] ],

                [ [18, 21],
                [18, -16] ],

                [ [-16, -1],
                [-25, 12] ],
                ),

                (
                [ [9, 28],
                [-27, -25],
                [17, -20] ],

                [ [0, -18],
                [19, -28],
                [-9, 21] ],

                [ [9, 46],
                [-46, 3],
                [26, -41] ],
                ),
                ]

        for tpl in tpls:
            mat1 = Matrix(tpl[0])
            mat2 = Matrix(tpl[1])
            matsub = mat1 - mat2

            for i in range(mat1.get_m()):
                for j in range(mat2.get_n()):
                    self.assertEqual(matsub.get(i, j), tpl[2][i][j])


    def test_substruction_with_invalid_arguments(self):
        with self.assertRaises(ValueError):
                    mat1 = Matrix(1, 3)
                    mat2 = Matrix(3, 3)
                    mat1 - mat2
    
        with self.assertRaises(TypeError):
            mat1 = Matrix(1, 3)
            mat1 - 0

        with self.assertRaises(TypeError):
            mat1 = Matrix(1, 3)
            mat1 - []

        with self.assertRaises(TypeError):
            mat1 = Matrix(1, 3)
            mat1 - "mat2"

        with self.assertRaises(TypeError):
            mat1 = Matrix(1, 3)
            mat1 - 1.0

        with self.assertRaises(TypeError):
            mat1 = Matrix(1, 3)
            mat1 - 33678


    def test_multiplication_by_matrix(self):
        tpls = [(
                [ [20, -16],
                [-23, -30] ],

                [ [1],
                [2] ],

                [ [-12],
                [-83] ],
                ),

                (
                [ [-5, 28],
                [17, -9],
                [11, -1] ],

                [ [-17, -18],
                [-20, -3] ],

                [ [-475, 6],
                [-109, -279],
                [-167, -195] ],
                ),

                (
                [ [-25, 1, -10],
                [9, -18, 23],
                [4, 27, 20] ],

                [ [-3, -26, 11],
                [-10, -10, -15],
                [-22, 11, 26] ],

                [ [285, 530, -550],
                [-353, 199, 967],
                [-722, -154, 159] ],
                ),

                (
                [ [-14, -17, -14],
                [22, -26, 23] ],

                [ [26, 19, 14],
                [-12, -28, 25],
                [-21, -27, -21] ],

                [ [134, 588, -327],
                [401, 525, -825] ],
                ),
                ]

        for tpl in tpls:
            mat1 = Matrix(tpl[0])
            mat2 = Matrix(tpl[1])
            matmul = mat1 * mat2

            for i in range(mat1.get_m()):
                for j in range(mat2.get_n()):
                    self.assertEqual(matmul.get(i, j), tpl[2][i][j])


    def test_multiplication_by_scalar(self):

        tpls = [(
                [ [17, 21],
                [-25, -29],
                [-19, 8] ],

                -3 ,

                [ [-51, -63],
                [75, 87],
                [57, -24] ],

                ),
                (
                [ [-27, -9],
                [-2, 26],
                [-14, -20],
                [-8, 9] ],

                -7 ,

                [ [189, 63],
                [14, -182],
                [98, 140],
                [56, -63] ],

                ),
                (
                [ [27, -19],
                [-21, 27] ],

                -4 ,

                [ [-108, 76],
                [84, -108] ],

                ),
                (
                [ [15, 6, -13] ],

                7 ,

                [ [105, 42, -91] ],

                ),
                (
                [ [-6, -5, 16, -17],
                [-9, -5, 18, 14],
                [-4, -13, -8, 23] ],

                -1 ,

                [ [6, 5, -16, 17],
                [9, 5, -18, -14],
                [4, 13, 8, -23] ],

                ),
                ]
        
        for tpl in tpls:
            mat1 = Matrix(tpl[0])
            s = tpl[1]
            matmul = mat1 * s

            for i in range(mat1.get_m()):
                for j in range(mat1.get_n()):
                    self.assertEqual(matmul.get(i, j), tpl[2][i][j])


    def test_multiplication_with_invalid_arguments(self):

        with self.assertRaises(ValueError):
            mat1 = Matrix(2, 3)
            mat2 = Matrix(2, 4)
            mat1 * mat2

        with self.assertRaises(TypeError):
            mat1 = Matrix(2, 3)
            mat2 = []
            mat1 * mat2

        with self.assertRaises(TypeError):
            mat1 = Matrix(2, 3)
            mat2 = "sss"
            mat1 * mat2
      

    def test_division(self):
        pass


    def test_division_with_invalid_arguments(self):
        pass
    

    def test_equal(self):
        pass


    def test_equal_with_invalid_arguments(self):
        pass


    def test_determinant(self):
        pass


    def test_determinant_with_invalid_arguments(self):
        pass


    def test_transpose(self):
        pass


    def test_transpose_with_invalid_arguments(self):
        pass

    def test_invert(self):
        pass


    def test_invert_with_invalid_arguments(self):
        pass   


class BorderCaseTests(TestCase):
    pass


class PerformanceTests(TestCase):
    pass


if __name__ == "__main__":
    main()