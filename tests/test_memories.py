from unittest import TestCase

from src.memories import DTypeFlipFlop


class DTypeFlipFlopTests(TestCase):

    TRUTH_TABLE = (
        # D      E       Q      ~Q
        ((False, True), (False, True)),
        ((True, True), (True, False)),
        ((False, False), (False, True)),
        ((True, False), (False, True)),
    )

    def setUp(self):
        self.flip_flop = DTypeFlipFlop()

    def test_truth_table(self):
        for test_case in self.TRUTH_TABLE:
            self.flip_flop.set_data(value=test_case[0][0])
            self.flip_flop.set_enabler(value=test_case[0][1])
            assert self.flip_flop.output == test_case[1]
