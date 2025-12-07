import unittest

from Head_line_app.Data_structure_and_algorithm.my_stack import MyStack


class MyTestCase(unittest.TestCase):
    def test_if_i_can_add_to_my_stack(self):
        stack = MyStack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        stack.push(4)
        self.assertEqual(4, stack.peek())


if __name__ == '__main__':
    unittest.main()
