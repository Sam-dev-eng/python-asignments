import unittest

from Head_line_app.Data_structure_and_algorithm.MyHashMap import HashMap


class MyTestCase(unittest.TestCase):
    def test_my_HashMap(self):
        hash_map = HashMap()
        hash_map['ONE'] = "january"
        print(hash_map)
        # self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
