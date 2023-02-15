import unittest
import tree_machine
import exp

class TestInterpreter(unittest.TestCase):
    def test_tree_machine(self):
        self.assertEqual(2,tree_machine.rewrite_loop(exp.test_exp1).value)
        self.assertEqual(21,tree_machine.rewrite_loop(exp.test_exp2).value)