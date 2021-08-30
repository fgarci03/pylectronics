"""
Implementation of mathematical adders.
"""
from typing import Tuple

from src.logic_gates import AndGate, XORGate, OrGate


class HalfAdder:
    """Implementation of a Half Adder."""

    def __init__(self) -> None:
        """Constructor."""
        self.input_1 = False
        self.input_2 = False

        self.and_gate = AndGate()
        self.xor_gate = XORGate()

    @property
    def output(self) -> Tuple[bool, bool]:
        """Get the result of the adder."""
        return self.xor_gate.output, self.and_gate.output  # (sum, carry out)

    def set_inputs(self, value_1: bool, value_2: bool) -> Tuple[bool, bool]:
        """Set the inputs of the adder."""
        self.input_1 = value_1
        self.input_2 = value_2

        self.xor_gate.set_inputs(value_1=self.input_1, value_2=self.input_2)  # Sum
        self.and_gate.set_inputs(value_1=self.input_1, value_2=self.input_2)  # Carry out

        return self.output


class FullAdder:
    """Implementation of a Full Adder."""

    def __init__(self) -> None:
        """Constructor."""
        self.input_1 = False
        self.input_2 = False
        self.carry_in = False

        self.or_gate = OrGate()
        self.half_adder_1 = HalfAdder()
        self.half_adder_2 = HalfAdder()

    @property
    def output(self) -> Tuple[bool, bool]:
        """Get the result of the adder."""
        half_adder_1_sum, half_adder_1_carry_out = self.half_adder_1.set_inputs(
            value_1=self.input_1, value_2=self.input_2
        )
        half_adder_2_sum, half_adder_2_carry_out = self.half_adder_2.set_inputs(
            value_1=self.carry_in, value_2=half_adder_1_sum
        )
        carry_out = self.or_gate.set_inputs(value_1=half_adder_1_carry_out, value_2=half_adder_2_carry_out)

        return half_adder_2_sum, carry_out

    def set_inputs(self, value_1: bool, value_2: bool, carry_in: bool) -> Tuple[bool, bool]:
        """Set the inputs of the adder."""
        self.input_1 = value_1
        self.input_2 = value_2
        self.carry_in = carry_in
        return self.output


class FourBitFullAdder:
    """Implementation of a 4bit Full Adder."""

    def __init__(self) -> None:
        """Constructor."""
        self.input_1 = False
        self.input_2 = False
        self.carry_in = False

        self.full_adder_1 = FullAdder()
        self.full_adder_2 = FullAdder()
        self.full_adder_3 = FullAdder()
        self.full_adder_4 = FullAdder()

    @property
    def output(self) -> Tuple[bool, bool, bool, bool, bool]:
        """Get the result of the adder."""
        return (
            self.full_adder_4.output[1],
            self.full_adder_4.output[0],
            self.full_adder_3.output[0],
            self.full_adder_2.output[0],
            self.full_adder_1.output[0],
        )

    def set_inputs(
        self, value_1: Tuple[bool, bool, bool, bool], value_2: Tuple[bool, bool, bool, bool], carry_in: bool
    ) -> Tuple[bool, bool, bool, bool, bool]:
        """Set the inputs of the adder."""
        self.full_adder_1.set_inputs(value_1=value_1[3], value_2=value_2[3], carry_in=carry_in)
        self.full_adder_2.set_inputs(value_1=value_1[2], value_2=value_2[2], carry_in=self.full_adder_1.output[1])
        self.full_adder_3.set_inputs(value_1=value_1[1], value_2=value_2[1], carry_in=self.full_adder_2.output[1])
        self.full_adder_4.set_inputs(value_1=value_1[0], value_2=value_2[0], carry_in=self.full_adder_3.output[1])

        return self.output
