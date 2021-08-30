from unittest import TestCase

from src.transistors import PNPTransistor, NPNTransistor


class PNPTransistorTests(TestCase):
    def setUp(self):
        self.transistor = PNPTransistor()

    def test_set_base_then_emitter(self):
        assert self.transistor.collector is False
        assert self.transistor.set_base(value=True) is False
        assert self.transistor.set_emitter(value=True) is True

    def test_set_emitter_then_base(self):
        assert self.transistor.collector is False
        assert self.transistor.set_emitter(value=True) is False
        assert self.transistor.set_base(value=True) is True

    def test_in_series_single_transistor(self):
        self.transistor_2 = PNPTransistor()
        self.transistor.set_base(value=True)

        assert self.transistor.in_series_with(transistors=self.transistor_2) is False

        self.transistor.set_emitter(value=True)
        assert self.transistor.in_series_with(transistors=self.transistor_2) is False

        self.transistor_2.set_emitter(value=True)
        assert self.transistor.in_series_with(transistors=self.transistor_2) is True

    def test_in_series_multiple_transistors(self):
        transistors = [PNPTransistor(), PNPTransistor(), PNPTransistor()]
        self.transistor.set_base(value=True)

        assert self.transistor.in_series_with(transistors=transistors) is False

        self.transistor.set_emitter(value=True)
        assert self.transistor.in_series_with(transistors=transistors) is False

        transistors[0].set_emitter(value=True)
        assert self.transistor.in_series_with(transistors=transistors) is False

        transistors[1].set_emitter(value=True)
        assert self.transistor.in_series_with(transistors=transistors) is False

        transistors[2].set_emitter(value=True)
        assert self.transistor.in_series_with(transistors=transistors) is True


class NPNTransistorTests(TestCase):
    def setUp(self):
        self.transistor = NPNTransistor()

    def test_set_base_then_emitter(self):
        assert self.transistor.collector is False
        assert self.transistor.set_base(value=True) is True
        assert self.transistor.set_emitter(value=True) is False

    def test_set_emitter_then_base(self):
        assert self.transistor.collector is False
        assert self.transistor.set_emitter(value=True) is False
        assert self.transistor.set_base(value=True) is False

    def test_in_series_single_transistor(self):
        self.transistor_2 = NPNTransistor()
        self.transistor.set_base(value=True)

        assert self.transistor.in_series_with(transistors=self.transistor_2) is True

        self.transistor.set_emitter(value=True)
        assert self.transistor.in_series_with(transistors=self.transistor_2) is False

        self.transistor_2.set_emitter(value=True)
        assert self.transistor.in_series_with(transistors=self.transistor_2) is False

    def test_in_series_multiple_transistors(self):
        transistors = [NPNTransistor(), NPNTransistor(), NPNTransistor()]
        self.transistor.set_base(value=True)

        assert self.transistor.in_series_with(transistors=transistors) is True

        self.transistor.set_emitter(value=True)
        assert self.transistor.in_series_with(transistors=transistors) is False

        transistors[0].set_emitter(value=True)
        assert self.transistor.in_series_with(transistors=transistors) is False

        transistors[1].set_emitter(value=True)
        assert self.transistor.in_series_with(transistors=transistors) is False

        transistors[2].set_emitter(value=True)
        assert self.transistor.in_series_with(transistors=transistors) is False
