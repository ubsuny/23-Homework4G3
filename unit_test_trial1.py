import unittest
import projectile

class TestProjectileMotion(unittest.TestCase):
    def test_calc_xy(self):
        # Test with known input values and expected output
        angle_degree = [30, 45]
        v_initial = 700
        x_start = 0
        y_start = 0
        x_list, y_list = calc_xy(angle_degree, [], [], v_initial, x_start, y_start)

        # Verify that the calculated x and y lists have the correct lengths
        self.assertEqual(len(x_list), len(angle_degree))
        self.assertEqual(len(y_list), len(angle_degree))

        # Verify that the calculated x and y lists contain numerical data
        for x, y in zip(x_list, y_list):
            self.assertTrue(all(isinstance(val, (int, float)) for val in x))
            self.assertTrue(all(isinstance(val, (int, float)) for val in y))

        # Verify that the final y positions are all approximately zero
        for y in y_list:
            self.assertAlmostEqual(y[-1], 0.0, places=2)

if __name__ == '__main__':
    unittest.main()
