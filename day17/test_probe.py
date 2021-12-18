import unittest

from day17.probe import parse_target_area, contains_point, step_probe, multiple_steps_probe


class ProbeTestCase(unittest.TestCase):
    def test_parse_target_area(self):
        target_area = parse_target_area('target area: x=282..314, y=-80..-45')
        self.assertEqual(target_area, (282, -80, 314, -45))

    def test_point_is_in_target_area(self):
        target_area = (282, -80, 314, -45)
        self.assertTrue(contains_point((282, -80), target_area))
        self.assertTrue(contains_point((314, -45), target_area))
        self.assertTrue(contains_point((282, -45), target_area))
        self.assertTrue(contains_point((314, -80), target_area))
        self.assertTrue(contains_point((290, -70), target_area))

    def test_point_is_not_in_target_area(self):
        target_area = (282, -80, 314, -45)
        self.assertFalse(contains_point((220, -43), target_area))

    def test_zero_zero_move_down(self):
        initial_position = (0, 0)
        initial_velocity = (0, 0)
        new_position, new_velocity = step_probe(initial_position, initial_velocity)

        self.assertEqual((0, 0), new_position)
        self.assertEqual((0, -1), new_velocity)

    def test_zero_one_move_down(self):
        initial_position = (0, 0)
        initial_velocity = (0, 1)
        new_position, new_velocity = step_probe(initial_position, initial_velocity)

        self.assertEqual((0, 1), new_position)
        self.assertEqual((0, 0), new_velocity)

    def test_one_one_move_forward(self):
        initial_position = (0, 0)
        initial_velocity = (1, 1)
        new_position, new_velocity = step_probe(initial_position, initial_velocity)

        self.assertEqual((1, 1), new_position)
        self.assertEqual((0, 0), new_velocity)

    def test_ten_zero_move_up_forward(self):
        initial_position = (0, 0)
        initial_velocity = (10, 2)
        new_position, new_velocity = step_probe(initial_position, initial_velocity)

        self.assertEqual((10, 2), new_position)
        self.assertEqual((9, 1), new_velocity)

        new_position, new_velocity = step_probe(new_position, new_velocity)

        self.assertEqual((19, 3), new_position)
        self.assertEqual((8, 0), new_velocity)

    def test_multiple_steps(self):
        target_area = (282, -80, 314, -45)
        initial_position = (0, 0)
        initial_velocity = (10, 2)
        new_position, new_velocity, inside_area, y = multiple_steps_probe(initial_position, initial_velocity, 2,
                                                                          target_area)

        self.assertEqual((19, 3), new_position)
        self.assertEqual((8, 0), new_velocity)

    def test_check_if_in_target_area(self):
        target_area = (282, -80, 314, -45)
        initial_position = (0, 0)
        initial_velocity = (10, 2)
        new_position, new_velocity, inside_area, y = multiple_steps_probe(initial_position, initial_velocity, 10,
                                                                          target_area)

        self.assertFalse(inside_area)

    def test_is_target_area(self):
        pass


# print(find_highest_y())


if __name__ == "__main__":
    unittest.main()
