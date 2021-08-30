from unittest import TestCase

from src.logic_gates import Inverter, AndGate, OrGate, NANDGate, NORGate, XORGate, XNORGate


class InverterTests(TestCase):
    def setUp(self):
        self.inverter = Inverter()

    def test_inverter(self):
        assert self.inverter.set_input(value=True) is False
        assert self.inverter.set_input(value=False) is True


class AndGateTests(TestCase):

    TRUTH_TABLE = (
        ((False, False), False),
        ((False, True), False),
        ((True, False), False),
        ((True, True), True),
    )

    def setUp(self):
        self.and_gate = AndGate()

    def test_truth_table(self):
        for test_case in self.TRUTH_TABLE:
            assert self.and_gate.set_inputs(*test_case[0]) is test_case[1]


class OrGateTests(TestCase):

    TRUTH_TABLE = (
        ((False, False), False),
        ((False, True), True),
        ((True, False), True),
        ((True, True), True),
    )

    def setUp(self):
        self.or_gate = OrGate()

    def test_truth_table(self):
        for test_case in self.TRUTH_TABLE:
            assert self.or_gate.set_inputs(*test_case[0]) is test_case[1]


class NANDGateTests(TestCase):

    TRUTH_TABLE = (
        ((False, False), True),
        ((False, True), True),
        ((True, False), True),
        ((True, True), False),
    )

    def setUp(self):
        self.nand_gate = NANDGate()

    def test_truth_table(self):
        for test_case in self.TRUTH_TABLE:
            assert self.nand_gate.set_inputs(*test_case[0]) is test_case[1]


class NORGateTests(TestCase):

    TRUTH_TABLE = (
        ((False, False), True),
        ((False, True), False),
        ((True, False), False),
        ((True, True), False),
    )

    def setUp(self):
        self.nor_gate = NORGate()

    def test_truth_table(self):
        for test_case in self.TRUTH_TABLE:
            assert self.nor_gate.set_inputs(*test_case[0]) is test_case[1]


class XORGateTests(TestCase):

    TRUTH_TABLE = (
        ((False, False), False),
        ((False, True), True),
        ((True, False), True),
        ((True, True), False),
    )

    def setUp(self):
        self.xor_gate = XORGate()

    def test_truth_table(self):
        for test_case in self.TRUTH_TABLE:
            assert self.xor_gate.set_inputs(*test_case[0]) is test_case[1]


class XNORGateTests(TestCase):

    TRUTH_TABLE = (
        ((False, False), True),
        ((False, True), False),
        ((True, False), False),
        ((True, True), True),
    )

    def setUp(self):
        self.xnor_gate = XNORGate()

    def test_truth_table(self):
        for test_case in self.TRUTH_TABLE:
            assert self.xnor_gate.set_inputs(*test_case[0]) is test_case[1]
