"""
Transistors, the basic element for digital electronics.

In this module, we define how transistors behave at their lowest level, so everything else can be built on top of them.
This is the only place where abstract logic such as +, -, and, or, provided by the Python language, can be used (since
we need SOME way to simulate how a transistor behaves in the real world!).
"""
from abc import ABCMeta, abstractmethod
from typing import Union, List


class BaseTransistor(metaclass=ABCMeta):
    """
    Base class for all transistors.

    Transistors are composed by the base, emitter and collector pins.
    https://en.wikipedia.org/wiki/Transistor
    """

    def __init__(self) -> None:
        """
        Constructor.
        """
        self.emitter = False
        self.base = False

    @property
    @abstractmethod
    def collector(self) -> bool:
        """
        Get the state of the collector pin (output).

        Each type of transistor should implement its own.
        """
        raise NotImplementedError()

    def set_emitter(self, value: bool) -> bool:
        """
        Set the state of the emitter pin.
        """
        self.emitter = value
        return self.collector

    def set_base(self, value: bool) -> bool:
        """
        Set the state of the base pin.
        """
        self.base = value
        return self.collector

    def in_series_with(self, transistors: Union['BaseTransistor', List['BaseTransistor']]) -> bool:
        """
        Connect a transistor in series with one or more transistors.
        """
        if self.collector is False:
            return False

        if isinstance(transistors, self.__class__):
            transistors = [transistors]

        previous_transistor = self
        for transistor in transistors:  # type: ignore
            current_result = transistor.set_base(previous_transistor.collector)
            if current_result is False:
                return False

        return True

    def in_parallel_with(self, transistors: Union['BaseTransistor', List['BaseTransistor']]) -> bool:
        """
        Connect a transistor in parallel with one or more transistors.
        """
        if self.collector is True:
            return True

        if isinstance(transistors, self.__class__):
            transistors = [transistors]

        for transistor in transistors:  # type: ignore
            if transistor.collector is True:
                return True

        return False


class PNPTransistor(BaseTransistor):
    """
    Implementation of a PNP Transistor.

    https://en.wikipedia.org/wiki/Bipolar_junction_transistor#PNP
    """

    @property
    def collector(self) -> bool:
        """
        Please refer to the interface documentation.
        """
        return self.emitter and self.base


class NPNTransistor(BaseTransistor):
    """
    Implementation of a NPN Transistor.

    https://en.wikipedia.org/wiki/Bipolar_junction_transistor#NPN
    """

    @property
    def collector(self) -> bool:
        """
        Please refer to the interface documentation.
        """
        return not self.emitter if self.base is True else False
