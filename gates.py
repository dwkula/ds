from typing_extensions import runtime


class LogicGate:

    def __init__(self, label):
        self.label = label
        self.output = None

    def get_output(self):
        self.output = self.logic()
        return self.output

    def get_label(self):
        return self.label


class BinaryGate(LogicGate):
    def __init__(self, label):
        super().__init__(label)
        self.pinA = None
        self.pinB = None

    def get_pin_a(self):
        if self.pinA == None:
            return int(input(f'Enter Pin A for gate {self.label}: '))
        else:
            return self.pinA.get_from().get_output()

    def get_pin_b(self):
        if self.pinB == None:
            return int(input(f'Enter Pin B for gate {self.label}: '))
        else:
            return self.pinB.get_from().get_output()

    def set_next_pin(self, source):
        if self.pinA == None:
            self.pinA = source
        else:
            if self.pinB == None:
                self.pinB = source
            else:
                raise RuntimeError("no empty pins")


class UnaryGate(LogicGate):
    def __init__(self, label):
        super().__init__(label)
        self.pin = None

    def get_pin(self):
        return int(input(f'Enter Pin for gate {self.label}: '))

    def set_next_pin(self, source):
        if self.pin is None:
            self.pin == source
        else:
            raise RuntimeError("no empty pins")


class AndGate(BinaryGate):
    def __init__(self, label):
        super().__init__(label)

    def logic(self):
        a = self.get_pin_a()
        b = self.get_pin_b()
        if a == 1 and b == 1:
            return 1
        else:
            return 0


class OrGate(BinaryGate):

    def __init__(self, label):
        super().__init__(label)

    def logic(self):
        a = self.get_pin_a()
        b = self.get_pin_b()
        if a == 1 or b == 1:
            return 1
        else:
            return 0


class NotGate(UnaryGate):

    def __init__(self, label):
        super().__init__(label)

    def logic(self):
        pin = self.get_pin()
        if pin == 1:
            return 0
        else:
            return 1


class NorGate(OrGate):

    def logic(self):
        if super().logic() == 1:
            return 0
        else:
            return 1


class NandGate(AndGate):

    def logic(self):
        if super().logic() == 1:
            return 0
        else:
            return 1


class Connector:
    def __init__(self, fgate, tgate):
        self.fromgate = fgate
        self.togate = tgate

        tgate.set_next_pin(self)

    def get_from(self):
        return self.fromgate

    def get_to(self):
        return self.togate
