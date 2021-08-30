"""
Implementation of memory related components.
"""
from typing import Tuple

from src.logic_gates import NANDGate


class DTypeFlipFlop:
    """
    Implementation of a D-Type Flip Flop.

    https://www.101computing.net/random-access-memory-using-logic-gates/

    NOTE: This component is still ongoing work...
    """

    def __init__(self) -> None:
        """
        Constructor.
        """
        self.data = False
        self.enabler = False

        self.nand_gate_1 = NANDGate()  # Data 1
        self.nand_gate_2 = NANDGate()  # Enabler 1
        self.nand_gate_3 = NANDGate()  # Data 2
        self.nand_gate_4 = NANDGate()  # Enabler 2

    @property
    def output(self) -> Tuple[bool, bool]:
        """
        Get the state of the flip flop.
        """
        self.nand_gate_3.set_inputs(value_1=self.nand_gate_1.output, value_2=self.nand_gate_4.output)
        self.nand_gate_4.set_inputs(value_1=self.nand_gate_2.output, value_2=self.nand_gate_3.output)

        return self.nand_gate_3.output, self.nand_gate_4.output

    def set_data(self, value: bool) -> Tuple[bool, bool]:
        """
        Set the data pin.
        """
        self.data = value

        self.nand_gate_1.set_inputs(value_1=value, value_2=self.enabler)
        self.nand_gate_2.set_inputs(value_1=self.nand_gate_1.output, value_2=self.enabler)

        return self.output

    def set_enabler(self, value: bool) -> Tuple[bool, bool]:
        """
        Set the enabler pin.
        """
        self.enabler = value

        self.nand_gate_2.set_inputs(value_1=self.nand_gate_1.output, value_2=value)
        self.nand_gate_1.set_inputs(value_1=self.data, value_2=value)

        return self.output
