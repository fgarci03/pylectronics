"""
Implementation of the several logic gates we can use to build the world.
"""
from abc import ABCMeta, abstractmethod
from src.transistors import PNPTransistor, NPNTransistor


class _BaseLogicGate(metaclass=ABCMeta):
    """
    Base class for all transistors.
    """

    def __init__(self) -> None:
        """
        Constructor.
        """
        self.input_1 = False
        self.input_2 = False

    @property
    @abstractmethod
    def output(self) -> bool:
        """
        Get the state of the logic gate.
        """
        raise NotImplementedError()

    @abstractmethod
    def _map_connections(self) -> None:
        """
        Map the connections between the internal components (either transistors or other logic gates).
        """
        raise NotImplementedError()

    def set_inputs(self, value_1: bool, value_2: bool) -> bool:
        """
        Set the inputs of the gate.
        """
        self.input_1 = value_1
        self.input_2 = value_2

        self._map_connections()

        return self.output


class Inverter:
    """
    Implementation of an Inverter (NOT Gate).
    """

    def __init__(self) -> None:
        """
        Constructor.
        """
        self.transistor = NPNTransistor()

        self.input = False

        self.transistor.set_base(value=True)

    @property
    def output(self) -> bool:
        """
        Please refer to the interface documentation.
        """
        return self.transistor.set_emitter(value=self.input)

    def set_input(self, value: bool) -> bool:
        """
        Set the input of the gate.
        """
        self.input = value
        return self.output


class AndGate(_BaseLogicGate):
    """
    Implementation of an AND Gate using 2 transistors in series.
    """

    def __init__(self) -> None:
        """
        Constructor.
        """
        super().__init__()

        self.transistor_1 = PNPTransistor()
        self.transistor_2 = PNPTransistor()

        self.transistor_1.set_base(value=True)

    @property
    def output(self) -> bool:
        """
        Please refer to the interface documentation.
        """
        return self.transistor_1.in_series_with(transistors=self.transistor_2)

    def _map_connections(self) -> None:
        """
        Please refer to the interface documentation.
        """
        self.transistor_1.set_emitter(value=self.input_1)
        self.transistor_2.set_emitter(value=self.input_2)


class OrGate(_BaseLogicGate):
    """
    Implementation of an OR Gate using 2 transistors in parallel.
    """

    def __init__(self) -> None:
        """Constructor."""
        super().__init__()

        self.transistor_1 = PNPTransistor()
        self.transistor_2 = PNPTransistor()

        self.transistor_1.set_base(value=True)
        self.transistor_2.set_base(value=True)

    @property
    def output(self) -> bool:
        """
        Please refer to the interface documentation.
        """
        return self.transistor_1.in_parallel_with(transistors=self.transistor_2)

    def _map_connections(self) -> None:
        """
        Please refer to the interface documentation.
        """
        self.transistor_1.set_emitter(value=self.input_1)
        self.transistor_2.set_emitter(value=self.input_2)


class NANDGate(_BaseLogicGate):
    """
    Implementation of a NAND Gate using an AND Gate and an Inverter.
    """

    def __init__(self) -> None:
        """Constructor."""
        super().__init__()

        self.and_gate = AndGate()
        self.inverter = Inverter()

    @property
    def output(self) -> bool:
        """
        Please refer to the interface documentation.
        """
        return self.inverter.output

    def _map_connections(self) -> None:
        """
        Please refer to the interface documentation.
        """
        and_result = self.and_gate.set_inputs(value_1=self.input_1, value_2=self.input_2)
        self.inverter.set_input(value=and_result)


class NORGate(_BaseLogicGate):
    """
    Implementation of a NOR Gate using an OR Gate and an inverter.
    """

    def __init__(self) -> None:
        """
        Constructor.
        """
        super().__init__()

        self.or_gate = OrGate()
        self.inverter = Inverter()

    @property
    def output(self) -> bool:
        """
        Please refer to the interface documentation.
        """
        return self.inverter.output

    def _map_connections(self) -> None:
        """
        Please refer to the interface documentation.
        """
        or_result = self.or_gate.set_inputs(value_1=self.input_1, value_2=self.input_2)
        self.inverter.set_input(value=or_result)


class XORGate(_BaseLogicGate):
    """
    Implementation of a XOR Gate using an AND, OR, and NAND Gates.
    """

    def __init__(self) -> None:
        """
        Constructor.
        """
        super().__init__()

        self.and_gate = AndGate()
        self.or_gate = OrGate()
        self.nand_gate = NANDGate()

    @property
    def output(self) -> bool:
        """
        Please refer to the interface documentation.
        """
        return self.and_gate.output

    def _map_connections(self) -> None:
        """
        Please refer to the interface documentation.
        """
        or_result = self.or_gate.set_inputs(value_1=self.input_1, value_2=self.input_2)
        nand_result = self.nand_gate.set_inputs(value_1=self.input_1, value_2=self.input_2)
        self.and_gate.set_inputs(value_1=or_result, value_2=nand_result)


class XNORGate(_BaseLogicGate):
    """
    Implementation of a XNOR Gate using a XOR Gate and an inverter.
    """

    def __init__(self) -> None:
        """
        Constructor.
        """
        super().__init__()

        self.xor_gate = XORGate()
        self.inverter = Inverter()

    @property
    def output(self) -> bool:
        """
        Please refer to the interface documentation.
        """
        return self.inverter.output

    def _map_connections(self) -> None:
        """
        Please refer to the interface documentation.
        """
        xor_result = self.xor_gate.set_inputs(value_1=self.input_1, value_2=self.input_2)
        self.inverter.set_input(value=xor_result)
