import unittest

from matrix import Matrix

# Tests adapted from `problem-specifications//canonical-data.json` @ v1.3.0


class MatrixTest(unittest.TestCase):
    def test_extract_row_from_one_number_matrix(self):
        matrix = Matrix("1")
        self.assertEqual(matrix.row(1), [1])

    def test_can_extract_row(self):
        matrix = Matrix("1 2\n3 4")
        self.assertEqual(matrix.row(2), [3, 4])

    def test_extract_row_where_numbers_have_different_widths(self):
        matrix = Matrix("1 2\n10 20")
        self.assertEqual(matrix.row(2), [10, 20])

    def test_can_extract_row_from_non_square_matrix_with_no_corresponding_column(self):
        matrix = Matrix("1 2 3\n4 5 6\n7 8 9\n8 7 6")
        self.assertEqual(matrix.row(4), [8, 7, 6])

    def test_extract_column_from_one_number_matrix(self):
        matrix = Matrix("1")
        self.assertEqual(matrix.column(1), [1])

    def test_can_extract_column(self):
        matrix = Matrix("1 2 3\n4 5 6\n7 8 9")
        self.assertEqual(matrix.column(3), [3, 6, 9])

    def test_can_extract_column_from_non_square_matrix_with_no_corresponding_row(self):
        matrix = Matrix("1 2 3 4\n5 6 7 8\n9 8 7 6")
        self.assertEqual(matrix.column(4), [4, 8, 6])

    def test_extract_column_where_numbers_have_different_widths(self):
        matrix = Matrix("89 1903 3\n18 3 1\n9 4 800")
        self.assertEqual(matrix.column(2), [1903, 3, 4])

    def test_mutable_row_whether_mutable_affects_matrix_object(self):
        matrix = Matrix("1 2\n3 4")
        r1 = matrix.row(1)
        r1[0] = 11
        r1_again = matrix.row(1)
        self.assertNotEqual(r1, r1_again)

    def test_mutable_column_whether_mutable_affects_matrix_object(self):
        matrix = Matrix("1 2\n3 4")
        c1 = matrix.column(1)
        c1[0] = 11
        c1_again = matrix.column(1)
        self.assertNotEqual(c1, c1_again)

if __name__ == "__main__":
    unittest.main()
