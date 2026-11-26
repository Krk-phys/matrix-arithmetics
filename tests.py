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
            pass


        def test_addition_with_invalid_arguments(self):
            pass


        def test_substruction(self):
            pass


        def test_substruction_with_invalid_arguments(self):
            pass


        def test_multiplication(self):
            pass


        def test_multiplication_with_invalid_arguments(self):
            pass


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