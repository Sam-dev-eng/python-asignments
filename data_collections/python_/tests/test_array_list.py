import unittest

from Head_line_app.Data_structure_and_algorithm.array_list import ArrayList


class MyTestCase(unittest.TestCase):
    def test_my_arrayListFunction(self):
        my_list = ArrayList()
        my_list.append(1)
        my_list.append(2)
        print(my_list)
        # self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
