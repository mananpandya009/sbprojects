"""Python serial number generator."""


class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start=0):
        self.start = start
        self.new_start = start

    def generate(self):
        self.new_start = self.new_start + 1;
        return self.new_start - 1

    def reset(self):
        self.start = self.new_start


serial = SerialGenerator(start=100)

print(serial.generate())

print(serial.generate())

print(serial.generate())

print(serial.reset())
print(serial.generate())
