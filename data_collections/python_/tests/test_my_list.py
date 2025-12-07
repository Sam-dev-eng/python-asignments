import unittest

from Head_line_app.Data_structure_and_algorithm.array import Array


class MyTestCase(unittest.TestCase):
    def test_my_list(self):
        my_list = Array(10)
        my_list[1] = 1
        my_list[1] = 0
        print(my_list)

        for index in range(len(my_list)):
            my_list[index] = index + 1

        print(my_list)
        self.assertEqual(my_list[4], 5)

if __name__ == '__main__':
    unittest.main()
