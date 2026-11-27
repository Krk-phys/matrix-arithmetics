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

        with self.assertRaises(ValueError):
            Matrix([[1,2], [3]])


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

        tpls = [(
                [ [19],
                [-22],
                [-7],
                [-19] ],

                6 ,

                [ [3.1666666666666665],
                [-3.6666666666666665],
                [-1.1666666666666667],
                [-3.1666666666666665] ],
                ),

                (
                [ [-10],
                [2],
                [-5] ],

                1 ,

                [ [-10.0],
                [2.0],
                [-5.0] ],
                ),

                (
                [ [4, -9],
                [17, 10],
                [-5, 10],
                [-1, 20] ],

                -1 ,

                [ [-4.0, 9.0],
                [-17.0, -10.0],
                [5.0, -10.0],
                [1.0, -20.0] ],
                ),

                (
                [ [1, -9, -7, -13],
                [-29, 23, 12, 1],
                [14, -24, -2, 14] ],

                -7 ,

                [ [-0.14285714285714285, 1.2857142857142858, 1.0, 1.8571428571428572],
                [4.142857142857143, -3.2857142857142856, -1.7142857142857142, -0.14285714285714285],
                [-2.0, 3.4285714285714284, 0.2857142857142857, -2.0] ],
                ),

                (
                [ [26, -23, 1, 9],
                [-6, 4, -12, 11],
                [7, 0, -18, -7],
                [-1, 25, -24, -29] ],

                -9 ,

                [ [-2.888888888888889, 2.5555555555555554, -0.1111111111111111, -1.0],
                [0.6666666666666666, -0.4444444444444444, 1.3333333333333333, -1.2222222222222223],
                [-0.7777777777777778, -0.0, 2.0, 0.7777777777777778],
                [0.1111111111111111, -2.7777777777777777, 2.6666666666666665, 3.2222222222222223] ],
                ),
                ]

        for tpl in tpls:
            mat1 = Matrix(tpl[0])
            s = tpl[1]
            matdiv = mat1 / s

            for i in range(mat1.get_m()):
                for j in range(mat1.get_n()):
                    self.assertEqual(matdiv.get(i, j), tpl[2][i][j])


    def test_division_with_invalid_arguments(self):

        with self.assertRaises(TypeError):
            mat1 = Matrix(2, 3)
            mat2 = Matrix(2, 4)
            mat1 / mat2

        with self.assertRaises(TypeError):
            mat1 = Matrix(2, 3)
            mat2 = []
            mat1 / mat2

        with self.assertRaises(TypeError):
            mat1 = Matrix(2, 3)
            mat2 = "sss"
            mat1 / mat2

        with self.assertRaises(ZeroDivisionError):
            mat1 = Matrix(1, 2)
            mat1 / 0
    

    def test_equal(self):

        data = [[ [-17, 5, -12, -1, -17],
                [-26, -18, 24, -24, 15],
                [-26, 2, -30, -24, 4],
                [-6, -17, 6, -23, -8] ],

                [ [15, -6, -16],
                [-30, -25, 22],
                [-5, 25, -8],
                [-5, 28, -10] ],

                [ [-24, -4, 23, 15, -4],
                [6, 19, 19, -1, -1],
                [28, -28, 28, -22, -8] ],

                [ [-29, -5, -20] ],

                [ [26, 12] ],

                [ [24, -1, 20, -12, -7],
                [14, 14, -16, -6, -5],
                [-12, -26, 21, 5, -15],
                [22, 6, -1, -13, -24] ],
                ]

        for mat in data:
            mat1 = Matrix(mat)
            mat2 = Matrix(mat)

            self.assertEqual(mat1, mat2)


    def test_equal_with_invalid_arguments(self):

        with self.assertRaises(ValueError):
            mat1 = Matrix(2, 2)
            mat2 = Matrix(1, 2)
            mat1 == mat2

        with self.assertRaises(TypeError):
            mat1 = Matrix(2, 2)
            mat2 = 0
            mat1 == mat2
            
        with self.assertRaises(TypeError):
            mat1 = Matrix(2, 2)
            mat2 = []
            mat1 == mat2

        with self.assertRaises(TypeError):
            mat1 = Matrix(2, 2)
            mat2 = "jsd"
            mat1 == mat2


    def test_determinant(self):
        tpls = [(
                [ [1, 8, 28, -9, -12],
                [8, -25, -30, -29, 14],
                [25, 10, -26, 0, -28],
                [27, -14, 7, 0, 10],
                [-16, 12, -7, 0, -9] ],

                2742683,
                ),

                (
                [ [13, -2],
                [-13, 22] ],

                260 ,
                ),

                (
                [ [2] ],

                2 ,
                ),

                (
                [ [-26, -22, 24, -13, 25],
                [-25, 24, 19, 0, 5],
                [-27, -29, -10, -17, 19],
                [-1, 25, -27, 12, -21],
                [13, 13, -18, -4, -21] ],

                -3553595 ,
                ),

                (
                [ [8] ],

                8 ,
                ),

                (
                [ [-25, -18],
                [26, 6] ],

                318 ,
                ),

                (
                [ [-15, 8880, 1],
                [100, 1, 0], 
                [0, 0, 0]],

                0 ,
                ),

                (
                [ [0, 1],
                [1, 0] ],

                -1,
                ),

                (
                [[0, 2, 0],
                 [1, 0, 0],
                 [0, 0, 3]],

                 -6,
                )
                ]

        for tpl in tpls:
            mat = Matrix(tpl[0])
            self.assertAlmostEqual(mat.determinant(), tpl[1])


    def test_determinant_with_invalid_arguments(self):

        with self.assertRaises(ValueError):
            mat = Matrix(1, 2)
            mat.determinant()


    def test_transpose(self):

        data = [[ [-15],
                [-2],
                [2] ],

                [ [9, 16, -2, -15],
                [2, -8, 21, -13],
                [18, -19, 21, 17] ],

                [ [2, 5, 12, -17],
                [8, -19, -25, -10],
                [14, -30, 28, -4] ],

                [ [-23, -30],
                [2, -15],
                [-7, 28],
                [10, -18],
                [19, -15] ],

                [ [21, 3, -7] ],

                [ [-3, 11, -10, 4],
                [-10, -14, -22, 14],
                [14, -24, 0, -26],
                [-18, -19, 8, -11],
                [-14, -18, -23, -26] ],

                ]

        for mat in data:
            mat1 = Matrix(mat)
            trmat = mat1.transpose()

            for i in range(mat1.get_m()):
                for j in range(mat1.get_n()):
                    self.assertEqual(trmat.get(j, i), mat[i][j])
       

    def test_invert(self):

        tpls = [(
                [ [1] ],

                [ [1] ]

                ),

                (
                [[1,1,1,0],[1,1,1,1],[0,-1,1,2],[3,4,5,0]],

                [[3.666666666666667,-0.666666666666667,0.333333333333333,-0.666666666666667],[-2.333333333333333,1.333333333333333,-0.666666666666667,0.333333333333333],[-0.333333333333333,-0.666666666666667,0.333333333333333,0.333333333333333],[-1,1,0,0]]

                ),

                (
                [ [4, -1, 4],
                [-3, 5, -1],
                [0, 0, -4] ],

                [[0.294117647058824,0.058823529411765,0.279411764705882],[0.176470588235294,0.235294117647059,0.117647058823529],[0,0,-0.25]]

                ),

                (
                [ [4] ],

                [ [0.25] ]

                ),

                (
                [ [4, 3, -5],
                [-3, -4, -5],
                [-2, 0, 5] ],

                [[-0.571428571428571,-0.428571428571429,-1],[0.714285714285714,0.285714285714286,1],[-0.228571428571429,-0.171428571428571,-0.2]]

                ),

                ]

        for tpl in tpls:
            mat = Matrix(tpl[0])
            matinv = mat.invert()

            for i in range(mat.get_m()):
                for j in range(mat.get_n()):
                    self.assertAlmostEqual(matinv.get(i, j), tpl[1][i][j])


    def test_invert_with_invalid_arguments(self):

        with self.assertRaises(ValueError):
            mat = Matrix(1, 2)
            mat.invert()


        with self.assertRaises(ValueError):
            mat = Matrix([[1, 2],
                          [1, 2]])   
            mat.invert()


if __name__ == "__main__":
    main()