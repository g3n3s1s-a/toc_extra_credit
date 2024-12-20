import unittest
from sat_to_3sat import sat_to_3sat, read_formula_from_file, write_formula_to_file

class TestSatTo3Sat(unittest.TestCase):

    def test_sat_to_3sat_reduction(self):
        # Test for example_1.txt
        formula = read_formula_from_file('tests/example_inputs/example_1.txt')
        reduced = sat_to_3sat(formula)

        expected_reduced = [
            ['x1', 'x2', '-x3'],
            ['x1', '-x2', 'x3'],
            ['x4', 'x5', 'y0'],
            ['-y0', 'x6', 'x7']
        ]

        self.assertEqual(reduced, expected_reduced)

    def test_read_formula_from_file(self):
        # Read formula from a file and check its correctness
        formula = read_formula_from_file('tests/example_inputs/example_1.txt')
        self.assertEqual(len(formula), 4)  # Assuming there are 4 clauses in example_1.txt

    def test_write_formula_to_file(self):
        # Test writing to file (use a temporary file)
        formula = [['x1', 'x2', '-x3'], ['x4', 'x5', 'y0']]
        write_formula_to_file(formula, 'output.txt')

        # Read back from the file and check correctness
        written_formula = read_formula_from_file('output.txt')
        self.assertEqual(written_formula, formula)

if __name__ == '__main__':
    unittest.main()

